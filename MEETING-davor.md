# Team-Meeting DAVOR — Fachrunde Europa, 23.7.2026 ~2:05

Teilnehmer: Sol (gpt-5.6-sol, Planung), Terra (gpt-5.6-terra, Gegenprüfung),
Fable (Orchestrierung/Protokoll). Grundlage: BRIEF-fachrunde-europa.md.

## Sol — Design-Prüfung (8.186 Tokens, FERTIG-SOL)

1. **Fehlende Regel:** These–Gegenthese–Entscheidungs-Matrix pro Blickwinkel
   (überprüfbarer Hauptsatz + stärkster Einwand + Entscheidungskriterium);
   Substanz-Messung statt Call-Zählung.
2. **Themen zu unscharf** → beide neu formuliert (siehe Brief, übernommen).
3. **Banalitäts-Risiko:** „europäischer dritter Weg" als folgenlose Formel.
   Gegenzug: Kollisionsfall-Test (US-API vs. China-Gewichte, gleicher Dienst,
   konkrete Nachweise an konkreten Kontrollpunkten).
4. **Abbruchkriterien zu lasch:** 5 formal erfolgreiche, aber redundante
   Antworten reichten bisher; Faktenwiderspruch sprang zu schnell auf
   „Was-wäre-wenn" statt auf Quellencheck.

## Terra — Adversarial-Prüfung (6.771 Tokens, FERTIG-TERRA)

1. **Stärkste Einwände gegen die Kernthese:** (a) AI Act ist schon mehr als
   ein Nachweisregime — HACCP kann ergänzen, nicht ersetzen; (b) ohne eigene
   Frontier-Modelle/Chips/Cloud bleibt Europa Prüfer fremder Systeme, abhängig
   von deren Zugang; (c) Brüssel-Effekt ist kein Geschäftsmodell — zu strenge
   Auflagen führen zu Marktrückzug oder Papier-Compliance.
2. **Muss vorweggenommen werden:** Nachlesbarkeit ≠ Souveränität — sonst
   klingt „Prüfinstanz" nach moralischer Selbstaufwertung eines abhängigen
   Marktes.
3. **Schwächste Prozess-Stelle:** Gleicher Gratis-Pool × 16 Prompts =
   Schein-Vielfalt mit recycelten Talking Points; Tausch-Runde kann
   Konsensrauschen verstärken; Faktencheck hängt allein an Fable.
4. **Review-Maßstab danach:** Destillat benennt Europas Machtlücke, bläht
   HACCP nicht zur Metapher auf, beschreibt eine politisch realistische Rolle.

## Beschlüsse (eingefaltet)

- ✅ Themen A/B durch Sols Formulierungen ersetzt (Brief + themen.txt des Watchers).
- ✅ Matrix-Pflicht in jeden Blickwinkel-Prompt (über den Themen-Text, kein
  Code-Eingriff in recherche.py).
- ✅ Abbruchkriterien: Substanz-Zählung (vollständige Dreier-Matrix) statt
  Call-Zählung; Faktenwiderspruch → erst Quellencheck.
- ✅ Synthese-Checkliste im Brief (Souveränitäts-Einwand, Kollisionsfall,
  AI-Act-Einordnung, Echo-Rabatt, Machtlücke).
- Terras Punkt „Faktencheck hängt an Fable": akzeptiert als Design — Fable
  prüft Zahlen/Zitate gegen echte Quellen (WebSearch) VOR dem Destillat;
  Terra reviewt danach als zweite Barriere.

Rohausgaben: ~/z/Agents/Codex/{sol,terra}-fachrunde-out.md
