# Teilstand-Demo: Lese-Test der unfertigen Ornith-Jlens (10/300 Fit-Prompts)
# auf Holdout-Prompts. ornith-ckpt.pt ist das fit()-Zwischenformat
# (jacobian_sum/n_done/next_idx), NICHT JacobianLens.save()-Format (J/...) —
# wird hier manuell in eine JacobianLens umgebaut. Rührt nacht_ornith.py und
# den Checkpoint nicht an; nur lesend.
import json, time, traceback

import datasets, torch, transformers, jlens
from jlens.lens import JacobianLens
from jlens.vis import compute_slice

jlens.configure_logging()
MODEL = "deepreinforce-ai/Ornith-1.0-9B"
CKPT = "ornith-ckpt.pt"
OUT_JSONL = "teilstand-demo-2026-07-23.jsonl"
OUT_MD = "teilstand-demo-2026-07-23.md"

# --- Modell laden (identisch zu nacht_ornith.py, damit es zum Checkpoint passt) ---
try:
    try:
        hf = transformers.AutoModelForCausalLM.from_pretrained(MODEL, dtype=torch.bfloat16)
    except Exception:
        hf = transformers.AutoModelForImageTextToText.from_pretrained(MODEL, dtype=torch.bfloat16)
    hf = hf.to("mps")
except Exception:
    print(f"ORNITH-LADEN FEHLGESCHLAGEN:\n{traceback.format_exc()}")
    raise SystemExit(3)

tok = transformers.AutoTokenizer.from_pretrained(MODEL)
model = jlens.from_hf(hf, tok)
print(f"Ornith geladen: n_layers={model.n_layers} d_model={model.d_model}")

# --- Teilstand-Checkpoint -> JacobianLens ---
state = torch.load(CKPT, map_location="cpu", weights_only=True)
n_done = state["n_done"]
next_idx = state["next_idx"]
source_layers = state["source_layers"]
target_layer = state["target_layer"]
print(f"Checkpoint: n_done={n_done} next_idx={next_idx} "
      f"source_layers={source_layers[0]}..{source_layers[-1]} ({len(source_layers)}) "
      f"target_layer={target_layer}")
jacobians = {l: state["jacobian_sum"][l] / n_done for l in source_layers}
lens = JacobianLens(jacobians=jacobians, n_prompts=n_done, d_model=model.d_model)
print(f"Teilstand-Lens gebaut: {lens!r}")

# --- Gleiche Prompt-Liste wie im Fit rekonstruieren (deterministisches Streaming, kein Shuffle) ---
ds = datasets.load_dataset("Salesforce/wikitext", "wikitext-103-raw-v1", split="train", streaming=True)
prompts = []
for ex in ds:
    t = ex["text"].strip()
    if len(t) > 400 and not t.startswith("="):
        prompts.append(t[:1200])
    if len(prompts) == 300:
        break
print(f"{len(prompts)} Prompts rekonstruiert (identischer Filter wie nacht_ornith.py)")

# --- Holdout: Indizes >= next_idx (10), NICHT im Fit gesehen ---
HOLDOUT_IDX = [10, 50, 150]
assert all(i >= next_idx for i in HOLDOUT_IDX), "Holdout-Index überschneidet sich mit Fit-Prompts"

out_f = open(OUT_JSONL, "w")
md_lines = [
    f"# Teilstand-Linsen-Lese-Demo — Ornith-1.0-9B ({time.strftime('%Y-%m-%d %H:%M')})",
    "",
    f"Checkpoint `{CKPT}`: {n_done}/300 Fit-Prompts abgeschlossen (next_idx={next_idx}), "
    f"{len(source_layers)} Quell-Layer ({source_layers[0]}..{source_layers[-1]}), Ziel-Layer L{target_layer}.",
    "",
    "**Holdout-Beleg**: Prompt-Liste 1:1 identisch zu `nacht_ornith.py` reproduziert "
    "(`Salesforce/wikitext`, `wikitext-103-raw-v1`, split `train`, `streaming=True`, "
    "Filter `len(text)>400 and not text.startswith('=')`, erste 300 Treffer, `t[:1200]`). "
    "HF-Streaming ohne `.shuffle()` liefert deterministisch dieselbe Reihenfolge wie im Nachtlauf. "
    f"Checkpoint-`next_idx`={next_idx} → der Fit hat ausschließlich `prompts[0:{next_idx}]` gesehen. "
    f"Gewählte Holdout-Indizes: {HOLDOUT_IDX} — alle ≥ next_idx, also disjunkt vom Fit-Set.",
    "",
]

for idx in HOLDOUT_IDX:
    prompt = prompts[idx]
    t0 = time.time()
    try:
        sd = compute_slice(model, lens, prompt, layer_stride=5, top_n=8, max_tracked=40,
                            max_seq_len=128, mask_display=True)
    except Exception:
        print(f"FEHLER bei Holdout-Prompt {idx}:\n{traceback.format_exc()}")
        continue
    dt = round(time.time() - t0)

    # Repräsentative Positionen: erste "gültige" (skip_first=16 wie im Fit), Mitte, letzte.
    valid_start = min(16, sd.seq_len - 1)
    positions = sorted(set([valid_start, sd.seq_len // 2, sd.seq_len - 2]))
    readings = []
    for p in positions:
        if not (0 <= p < sd.seq_len):
            continue
        ctx_tok = sd.context_token_strs[p + sd.ctx_offset]
        per_layer = {}
        for li, layer in enumerate(sd.layers):
            toks = [sd.vocab_fragment.get(int(t), "?") for t in sd.top_ids[p, li, :5]]
            per_layer[str(layer)] = toks
        readings.append({"pos": p, "token_at_pos": ctx_tok, "per_layer_top5": per_layer})

    rec = {"prompt_index": idx, "holdout": True, "prompt_preview": prompt[:200],
           "seq_len": sd.seq_len, "layers": sd.layers, "sekunden": dt, "readings": readings}
    out_f.write(json.dumps(rec, ensure_ascii=False) + "\n"); out_f.flush()
    print(f"[holdout {idx}] {dt}s, {len(readings)} Positionen gelesen")

    md_lines.append(f"## Holdout-Prompt {idx} ({dt}s, seq_len={sd.seq_len})")
    md_lines.append(f"> {prompt[:200]}...")
    md_lines.append("")
    for r in readings:
        md_lines.append(f"- Position {r['pos']} (Token `{r['token_at_pos']!r}`):")
        for layer, toks in r["per_layer_top5"].items():
            md_lines.append(f"  - L{layer}: {toks}")
    md_lines.append("")

out_f.close()
with open(OUT_MD, "w") as f:
    f.write("\n".join(md_lines) + "\n")
print("TEILSTAND-DEMO FERTIG")
