# Team-Meeting DANACH — Fachrunde Europa, 23.7.2026 ~3:30

Teilnehmer: Terra (Destillat-Review), Sol (Prozess-Review), Fable (Protokoll).

## Lauf-Fakten

- Engine-Wechsel: unser Gratis-LLM-Gateway-Pool leer (auch um 2:30, kein Mitternacht-UTC-Reset)
  → 16 Claude-Sonnet-Subagenten + 2 Tausch-Runden auf Plan-Limits (Jay-Go).
- Substanz: 16/16 Blickwinkel mit vollständiger Dreier-Matrix (Abbruchkriterium
  klar übererfüllt). ~660k Subagent-Tokens.
- Tausch-Runde lieferte Thesen, die kein Einzel-Blickwinkel hatte:
  **Treuhänder-Auditor mit vertraulichem Gewichts-Zugang (IAEA-Inspektor-Modell)**,
  **zwei gekoppelte Regime statt „einheitliches" Nachweissystem**,
  **Goodhart-Linie „Metrik vom Auditor vs. vom Geprüften"**,
  **Versicherungspflicht als Deployer-Hebel**.

## Terra — Destillat-Review (FERTIG-TERRA-DANACH)

- Verdikt: **REIF NACH KLEINER KORREKTUR.** Machtlücke benannt, HACCP eingehegt;
  aber (1) Absolut-Behauptung „keine Spitzenmodelle/Chips/Hyperscaler" mit
  Mistral/OVHcloud/SAP angreifbar, (2) Lab-Anreiz war Wunschdenken — an
  Marktzugang/Beschaffung/Haftungsprivilegien koppeln, Verweigerung ehrlich
  benennen, (3) HACCP gilt risikoabgestuft (VO 852/2004 Art. 5), nicht pauschal.
- ✅ Alle drei Korrekturen in v2 eingefaltet (Commit nach diesem Protokoll).

## Sol — Prozess-Review (FERTIG-SOL-DANACH)

- **Note 2.** Matrix-Pflicht messbar ausgezahlt (16/16 vollständig, vergleichbar,
  tauschfähig) — misst aber Disziplin, nicht Unabhängigkeit.
- Engine-Monokultur (16× dasselbe Modell) verschärft Konsensrauschen-Risiko;
  entschärft dafür Halluzinations-/Leerlaufrisiko der Gratis-Modelle. Die echten
  Tausch-Neuthesen zeigen: Reibung blieb produktiv.
- **Prozess-Verbesserung für nächsten Lauf:** blinde Gegenprüfung durch ein
  ANDERES Modell, das die zwei stärksten neuen Thesen gezielt zu widerlegen
  versucht (nicht weiter synthetisiert). Teilweise heute schon geschehen —
  Terras Review lief auf GPT-5.6 — aber als eigener Refutations-Schritt
  formalisieren. → In den Brief der nächsten Fachrunde übernehmen.

## Beschlüsse

- Destillat v2 = Abnahme-Stand für Jay (Veröffentlichung entscheidet er).
- Nächste Fachrunde: Refutations-Schritt (Fremdmodell, blind) fest einplanen;
  wenn unser Gratis-LLM-Gateway voll: Mischbetrieb Sonnet + Pool für Engine-Diversität prüfen.
- Rohberichte: files/story-recherche/berichte/fachrunde-europa-{A,B}-*.md
- Rohausgaben Reviews: ~/z/Agents/Codex/{terra,sol}-danach-out.md

## Nachtrag ~3:30 — Sols Refutations-Schritt SOFORT umgesetzt (Jays Anstoß: OpenCode)

Blinder Angreifer: **gemma4:12b lokal** (OpenCode/Ollama — maximale
Engine-Diversität, 0 €). Nur die zwei Kern-Thesen, null Kontext. Ergebnis:
beide Thesen überleben; 3 von 4 Angriffen treffen Behauptungen, die das
Destillat gar nicht aufstellt (Zugang≠Verständnis, offen≠sicher). EIN echter
Treffer: „Versicherungspflicht setzt quantifizierbare Risiken voraus" →
Destillat v3 pariert mit dem Kfz-Präzedenz-Satz (Risiko wurde erst durch die
Pflicht messbar). Gemma4-Urteil „These 2 schwächer (binäre Kategorisierung)"
notiert — Kollisionsfall-Rahmung im Text fängt das bereits ab.
