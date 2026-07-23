# Vorrecherche: HACCP-artiges KI-Regime — was es kann und was nicht (2026-07-23)

*Rohmaterial — Fakten VOR Verwendung pruefen!*
*Engine: Claude-Sonnet-Subagenten (16×, Plan-Limits) statt unserem Gratis-LLM-Gateway — Pool war leer (Fachrunde Europa, Brief in claude-orchestration/plans/).*

Thema: Wie sähe ein HACCP-artiges KI-Regime (dokumentierte kritische Kontrollpunkte, unabhängige Prüfung, Sanktionen) konkret aus — welche Schäden könnte es besser begrenzen als Verhaltensverbote, welche ausdrücklich nicht?

## fakten (claude-sonnet-5)

- HACCP: 1959 Pillsbury/NASA für Astronautenkost; seit VO (EG) 852/2004 für jeden EU-Lebensmittelbetrieb Pflicht. 7 Prinzipien; Dokumentationspflicht ist das Kernmerkmal, nicht Verbote.
- Wirksamkeits-Zahlen (% Rückgang Vergiftungen) und Kosten pro Betrieb in Kurzrecherche NICHT belegbar gefunden (?) — über EFSA/FDA-Studien nachprüfen.
- AI Act: Hochrisiko-Pflichten ab 2.8.2026; Bußgelder bis 35 Mio. €/7 % (verbotene Praktiken), 15 Mio. €/3 % (Hochrisiko), 7,5 Mio. €/1,5 % (Falschangaben). Strukturell näher an HACCP-Prozesskontrolle als an Verbotslisten (mittelsicher).
- CCP-Grenze: trägt nur, wo Gefahr an identifizierbaren, messbaren Punkten auftritt; für emergente/Post-Deployment-Schäden fehlt das Äquivalent zum physischen Grenzwert.
- Quellen: boerse-express.com (Bußgelder, Juli 2026), IHK-Merkblatt HACCP.

HAUPTSATZ: Der AI Act führt ab August 2026 ein dokumentations- und prüfpflichtiges Regime ein, das strukturell näher an HACCP liegt als an reinen Verhaltensverboten.
EINWAND: Bei KI fehlen oft eindeutige, vorab identifizierbare Kontrollpunkte — Scheinpräzision droht.
KRITERIUM: Ein KI-CCP muss (a) vor Schadenseintritt messbar und (b) unabhängig nachprüfbar sein — sonst ist es ein verkleidetes Verhaltensverbot.

## gegenposition (claude-sonnet-5)

- KI ist kein linearer Prozess mit stabilen Gefahrenpunkten; Verhalten driftet mit jedem Fine-Tune — man kontrolliert, was man kennt, nicht was neu auftaucht (?).
- HACCP funktioniert, weil Gefahrenklassen abschließend bekannt sind (Pathogene); bei KI ist die Schadensmenge offen — Katalog wird unvollständig oder uferlos.
- Modell ist zum Zertifizierungszeitpunkt schon nicht mehr identisch mit dem im Einsatz (RLHF, Retrieval) — Audit-Trail bricht strukturell.
- Verantwortung verwischt in Ketten (Foundation-Anbieter/Fine-Tuner/Deployer) — HACCP hat EINEN Betrieb pro Kontrollpunkt.
- Verbote sind bei akuten Schäden (CSAM, Biowaffen) schneller; HACCP-Logik überlegen bei chronischen/systemischen Risiken — verschiedene Schadensklassen, kein Ersatzverhältnis (?).

HAUPTSATZ: Ein HACCP-Regime setzt reproduzierbare, vorab definierbare Kontrollpunkte voraus, die ein sich veränderndes Modell strukturell nicht liefert.
EINWAND: Auch Lebensmittel kennen Drift (neue Erreger) und werden über periodische Re-Validierung kontrolliert — das Argument beweist zu viel.
KRITERIUM: Kann ein unabhängiger Dritter ohne Trainingsdaten-Zugriff eine Kontrollpunkt-Verletzung reproduzierbar feststellen?

## geschichte (claude-sonnet-5)

- 1959–60er Pillsbury/NASA: Nullfehler durch Endprodukttests unmöglich → Kontrolle auf Prozessebene. 1971 öffentlich, 1993 Codex Alimentarius (7 Prinzipien), EU-Pflicht via VO 852/2004 — Selbstdokumentation + behördliche Audits, kein Vorab-Genehmigungsverfahren.
- Wirkung stark abhängig von Prüfintensität — HACCP-Papier ohne echte Audits = Feigenblatt (?).
- Parallelen: Luftfahrt-SMS (ICAO ~2006), Pharma-GMP, SOX 2002 — gemeinsames Muster: Prozesstransparenz + unabhängige Drittprüfung + **Sanktion bei Falschdokumentation, nicht beim Fehler an sich**.
- Lehre: funktioniert, wo Kausalketten physisch nachvollziehbar sind; bei KI am ehesten für Pipeline-Schritte (Datenherkunft, Eval-Gates, Red-Teaming-Protokolle), nicht fürs Modellverhalten selbst.
- Quellen: en.wikipedia.org/wiki/Hazard_analysis_and_critical_control_points, fooddocs.com/post/history-of-haccp, EUR-Lex 852/2004.

HAUPTSATZ: HACCP wurde erst durch verpflichtende, unabhängig geprüfte Dokumentation wirksam (EU 2004), nicht durch die Existenz der Methode seit 1959.
EINWAND: Bei generativer KI fehlt die physische Diskretheit der Gefahrenpunkte — Prozess-Theater droht.
KRITERIUM: Haben unabhängige Prüfer Sanktionsmacht UND Zugriff auf reale Betriebsdaten (nicht Selbstauskunft)?

## betroffene (claude-sonnet-5)

- Gastronom mit KI-Kasse (Allergen-Erkennung): Kontrollpunkt „Allergenwarnung ja/nein" macht Haftung klärbar; lästig für Kleinbetriebe (?).
- Entwicklerin im Mittelstand: CCP „KI-Code in Sicherheitsmodul" → Review-Nachweis, Audit-Trail pro Commit; bremst Iteration.
- Behördensachbearbeiter: „automatisierte Vorentscheidung übergeben" als CCP mit Stichproben — für Bürger nachweisbare Fehlerquote statt Blackbox; für Sachbearbeiter Rückendeckung („Fehler lag im Kontrollpunkt X, nicht bei mir").
- Endnutzer: sieht Zertifikat, nicht Prozess — wie Kühlkette-Siegel.
- Fängt gut: bekannte, wiederkehrende Fehlerklassen. Fängt nicht: emergente Muster ohne vordefinierten Punkt.

HAUPTSATZ: Ein HACCP-Regime verlagert Verantwortung von Verhaltensvorschriften auf dokumentierte, prüfbare Prozess-Kontrollpunkte beim Einsatz.
EINWAND: Kritische Punkte lassen sich bei offenem Aufgabenraum oft erst NACH dem Schadensfall definieren.
KRITERIUM: Gibt es einen wiederkehrenden, lokalisierbaren Fehlerpunkt (→ HACCP trägt) oder ist das Potenzial diffus/neuartig (→ andere Mechanismen nötig)?

## technik (claude-sonnet-5)

- Übersetzungstabelle: Wareneingang→Trainingsdaten-Herkunft (Provenienz, Lizenz, Kontamination; Chargen-Rückverfolgung fehlt bei Daten (?)); Prozessgefahr→Eval-Gates vor Deployment (existiert als RSP/Frontier-Safety, aber Selbstauskunft); Temperaturmessung→Laufzeit-Logging (intern vorhanden (?), keine extern einsehbare „Temperaturkurve"); Laborprobe→Interpretierbarkeits-Checks (Forschung, nicht Routine-QS); Rückruf→API-Sperre/Weight-Rollback — bei offenen Gewichten **strukturell unmöglich**.
- Analogie trägt bei Prozessfehlern mit Kausalkette; bricht bei emergentem Verhalten (kein Bakterienwachstum, keine physikalische Kette) (?).

HAUPTSATZ: Für API-gebundene Modelle sind Eval-Gates und Logging als CCPs umsetzbar; für offen verteilte Gewichte fehlt das Rückruf-Äquivalent strukturell.
EINWAND: Auch geschlossene Modelle sind vor dem Rückruf kopierbar (Distillation) — der Schutz ist graduell.
KRITERIUM: Ist ein Modell nach Deployment technisch vollständig zurückholbar (Gewichte + Distillate)? Wenn nein, ersetzt HACCP dort keine vorgelagerten Verbote.

## geld (claude-sonnet-5)

- Verdienen: Zertifizierer/Auditoren (TÜV/DEKRA-analog, wiederkehrende Audits (?)), Tooling (Eval-Suiten, Interpretability-Dashboards), Beratung (Big Four schon im AI-Governance-Geschäft), große Labs (Moat-Effekt).
- Zahlen: GMP-Zertifizierung real 10.000–100.000 USD/Betrieb, ISO 9001 ab ~5.000 € für KMU (iasiso-europe.com, gmpplus.org) — KI-Audits vermutlich teurer (?); Fixkosten treffen Kleine unverhältnismäßig; OSS-Verteiler: unklar wer „Betreiber" ist — Haftungslücke oder Startup-Killer (?).
- Wackelt: freizügige Wrapper ohne Kontrollpunkt-Infrastruktur.
- Lücken: KI-Auditoren, gestaffelte Haftpflicht-Produkte (?), Compliance-as-a-Service für Mittelstand.
- HACCP-Kritik als Warnung: begünstigt Konzentration (kleine Metzgereien schließen) — bei KI naheliegend, nicht zwingend (?).

HAUPTSATZ: Ein HACCP-artiges KI-Regime schafft eine neue Prüfbranche, deren Fixkosten kleine Anbieter relativ stärker belasten.
EINWAND: Genau dieses Argument instrumentalisieren Etablierte strategisch gegen jede Regulierung.
KRITERIUM: Sind Anforderungen umsatz-/risikogestaffelt (safe harbor für Kleine) oder einheitlich?

## risiken (claude-sonnet-5)

- Scheinsicherheit: Zertifikat als Haftungsschild; Betriebe bestehen Audits und haben trotzdem Ausbrüche (?); Zertifizierer-Kapture (Rating-Agenturen vor 2008).
- Checklisten-Theater: Kontrollpunkte verengen sich aufs Messbare; Proxy-Metriken (Benchmark-Scores) werden Selbstzweck; Doku-Last begünstigt Konzentration.
- Innovations-Abwanderung: hohe Audit-Kosten verschieben Forschung in regelfreie Jurisdiktionen (empirisch offen (?)); offene Gewichte nach Release nicht an CCPs rückbindbar.
- Kontrollpunkt am falschen Ort: Modell-Ebene übersieht System-Ebene (Orchestrierung, Tool-Zugriff, Agentenketten) — dort entstehen viele reale Schäden.
- Gegenmittel: Ergebnis- statt Prozessmetriken, Zufalls-Audits, Zertifizierer-Rotation/-Unabhängigkeit, Kontrollpunkte auf mehreren Ebenen, Sunset-Klauseln; Revisionsrate der CCPs als Kennzahl.

HAUPTSATZ: Ein CCP-Regime verlagert Risiko von „unentdecktem Schaden" zu „entdecktem, aber durch bestandene Prüfung legalisiertem Schaden".
EINWAND: Ohne Regime gibt es gar keine dokumentierte Angriffsfläche für Aufsicht — Theater ist mehr Transparenz als Verbote ex post.
KRITERIUM: Zertifizierer strukturell unabhängig von Anbieterfinanzierung UND CCPs werden bei Vorfällen nachweislich revidiert.

## zukunft (claude-sonnet-5)

- PLAUSIBEL — Versicherer als Treiber: großer Schadensfall → Prämien für „unkontrollierte" KI explodieren → Deckung nur mit dokumentierten Gates/Logging/Human-in-loop; Prüf-Ökosystem zertifiziert Kontrollpunkte, nicht Modelle; Sanktion = Unversicherbarkeit (Marktdruck > Regulierung). Tempo hängt am Schlagzeilen-Fall (?).
- ÜBERRASCHEND — Konsortium nach erstem „KI-Rückruf": Labs gründen selbst gemeinsamen Kontrollpunkt-Standard (schneller als Gesetzgebung); Durchsetzung über Enterprise-Einkaufsvoraussetzung, privater Standard mit Marktmacht; Risiko: Kartell, Markteintrittsblockade (?).
- Kann besser begrenzen: belegbare Prozessfehler, kumulative Ketten kleiner Fehler. Kann nicht: emergente Muster, intentionale Doku-Manipulation, Fähigkeitssprünge schneller als Katalog-Updates.

HAUPTSATZ: Ein HACCP-Regime verlagert Kontrolle von Verhaltensverboten auf dokumentierte, auditierbare Prozessschritte vor kritischen KI-Aktionen.
EINWAND: Kontrollpunkte lassen sich auf dem Papier erfüllen (Compliance-Theater).
KRITERIUM: Zeigt eine unabhängige Stichprobe reale Übereinstimmung zwischen dokumentiertem und tatsächlichem Verhalten?

## Tausch-Runde (mit Kondensat Thema A)

1. **Prüftisch-Ort:** Interpretierbarkeits-Proben brauchen Gewichts-Zugang (A) → die „Laborstichprobe" aus B bricht: Blackbox-API-Tests prüfen Verhalten, nie Prozess. NEUE THESE: CCP „Interpretierbarkeit" verlangt einen **Treuhänder-Auditor mit privilegiertem, vertraulichem Zugang** — IAEA-Inspektor-Modell (Zugang zu geheimen Anlagen), nicht HACCP-Modell (Chargenprobe). Dritter institutioneller Typ, den keiner der 16 Blickwinkel benannt hatte.
2. **CCP-Kollaps bei offenen Gewichten:** radikaler als B annahm — offene Gewichte verteilen das „Kochen" auf Millionen Privatküchen; kein Restaurant mehr prüfbar, nur die Rezeptveröffentlichung. Konzept-Kollaps, nicht graduelle Schwächung.
3. **Versicherer + Marktzugang als Vollzugspaar:** Prämie↔Marktzugang↔Audit-Nachweis als privates Doppel-Scharnier (SOX-Wirtschaftsprüfer-Muster: Haftung statt Behördenpersonal).
4. **Goodhart-Linie:** Threshold-Gaming (A) = eval-aware Gaming = Checklisten-Theater (B) — dieselbe Lücke. Wirksam/unwirksam trennt sich nicht entlang „Verbot vs. HACCP", sondern entlang „Metrik vom Auditor vs. vom Geprüften erzeugt".
5. **Hardware-Attestierung** (A-Zukunft) repariert Bs schwächsten CCP: Laufzeit-Logging wird vom selbstprotokollierenden Kühlschrank zum echten Drittmesspunkt (?).

SYNTHESE-THESE: Wirksame KI-Aufsicht entsteht nicht aus der Wahl zwischen Verhaltensverbot und HACCP-Regime, sondern daraus, ob jeder einzelne Kontrollpunkt auf einen Flaschenhals außerhalb der Selbstauskunft des Geprüften verlagert werden kann (Compute/Hardware bei offenen Gewichten, Treuhänder-Zugang bei Interpretierbarkeit, Versicherungsprämie bei Marktzugang) — wo diese Verlagerung misslingt, bleiben beide Regimetypen gleichermaßen zahnlos.
