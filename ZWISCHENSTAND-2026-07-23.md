# Ornith-Nachtlauf — Zwischenstand beim Stopp (23.7. ~3:55, Jay-Go „auslaufen lassen")

- Modell: Ornith-1.0-9B (offene Gewichte, MIT), jlens-Fit Ziel-Layer L31, 31 Quell-Layer.
- Gelaufen: 10/300 Prompts in ~10h17m (Start ~17:30) — ~1h/Prompt, torch/MPS-Fallback
  (flash-linear-attention-Kernel nur CUDA; auf dem Mac kein schneller Pfad).
- Werte: max||J||/sqrt(d) zwischen 8.1 und 26.9; max_d_mean fällt tendenziell
  (0.55 → ~0.2-0.4) = Fit arbeitet; Prompt 1 nan (bekannt, Ausreißer).
- Checkpoint: ornith-ckpt.pt (1984 MB) — Teilstand-Linse daraus testbar.
- Ökonomie-Kontrast (aus PLAN-lesbare-ki): gleiche Volllinse auf gemieteter
  A6000/A100 geschätzt Stunden statt Wochen, 10-30 € ☑️.

## Team-Urteil (Terra, ~4:05)
EIN Artikel jetzt: A „Interpretierbarkeit am Küchentisch" als WERKSTATTBERICHT
(„Vorversuch", nicht validiertes Prüfwerkzeug) + B-Ökonomie als Absatz/Kasten.
Mindestbar vor Veröffentlichung: (1) Teilstand-Linse gesichert, (2) EINE
reproduzierbare Lese-Demo auf gehaltenen Prompts, (3) Methodenkasten
(Holdout-Trennung; was die fallende Fit-Metrik aussagt und was nicht);
ideal: Replikationscode + Checkpoint veröffentlichen. Einwand vorwegnehmen:
„Linse gefittet ≠ kausal erklärt ≠ generalisiert". Reihenfolge: nach dem
FAZ-Text, als bescheidene Demonstration dessen, was ein Nachlesbarkeits-Labor
ermöglichen soll. Volllinse = Follow-up.
