# Nachtlauf Teil 2: Eigene J-lens für Ornith-1.0-9B fitten (Dauerläufer, checkpointed).
# Läuft so lange die Nacht reicht; Wiederaufnahme über ornith-ckpt.pt.
import time, traceback

import datasets, torch, transformers, jlens

jlens.configure_logging()
MODEL = "deepreinforce-ai/Ornith-1.0-9B"

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

# Echtheits-Test: erst wenn das Sprachrohr stimmt, darf gefittet werden.
_pt = tok.apply_chat_template([{"role": "user", "content": "What is 2+2? Answer with just the number."}],
                              tokenize=False, add_generation_prompt=True, enable_thinking=False)
_inp = tok(_pt, return_tensors="pt").to("mps")
_out = hf.generate(**_inp, max_new_tokens=30, do_sample=False)
_ans = tok.decode(_out[0][_inp["input_ids"].shape[1]:], skip_special_tokens=True)
print("Echtheits-Test 2+2:", repr(_ans))
if "4" not in _ans:
    print("SPRACHROHR-TEST FEHLGESCHLAGEN — Fitten abgebrochen.")
    raise SystemExit(4)
model = jlens.from_hf(hf, tok)
print(f"Ornith geladen: n_layers={model.n_layers}")

ds = datasets.load_dataset("Salesforce/wikitext", "wikitext-103-raw-v1", split="train", streaming=True)
prompts = []
for ex in ds:
    t = ex["text"].strip()
    if len(t) > 400 and not t.startswith("="):
        prompts.append(t[:1200])
    if len(prompts) == 300:
        break
print(f"{len(prompts)} Fitting-Prompts geladen")

t0 = time.time()
lens = jlens.fit(model, prompts=prompts, max_seq_len=128, checkpoint_path="ornith-ckpt.pt")
lens.save("ornith-jlens.pt")
print(f"ORNITH-LENS FERTIG nach {(time.time()-t0)/3600:.1f} h")
