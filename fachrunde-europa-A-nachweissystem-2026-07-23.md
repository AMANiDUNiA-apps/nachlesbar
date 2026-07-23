# Vorrecherche: EU-Nachweissystem für geschlossene US-Modelle und offene China-Gewichte (2026-07-23)

*Rohmaterial — Fakten VOR Verwendung pruefen!*
*Engine: Claude-Sonnet-Subagenten (16×, Plan-Limits) statt unserem Gratis-LLM-Gateway — Pool war leer (Fachrunde Europa, Brief in claude-orchestration/plans/).*

Thema: Kann die EU für geschlossene US-Modelle und offene chinesische Modellgewichte ein einheitliches, technisch prüfbares Nachweissystem durchsetzen — und an welchen Kontrollpunkten, Zuständigkeiten, Umgehungswegen und Wettbewerbskosten entscheidet sich dessen Erfolg?

## fakten (claude-sonnet-5)

- AI Act GPAI-Pflichten (Art. 53) gelten für alle Anbieter unabhängig vom Sitz, sobald das Modell im EU-Markt angeboten wird — extraterritorial angelegt, Vollzug aber auf Marktzugang gestützt.
- Schwellenwert „systemisches Risiko" (Art. 51): 10^25 FLOPs kumulierter Trainings-Compute als widerlegbare Vermutung; Trainings-FLOPs einzelner Modelle selten offiziell bestätigt (?).
- Open-Source-Ausnahme (Art. 53 Abs. 2): offene Gewichte ohne systemisches Risiko von Doku-Pflichten befreit, NICHT von Copyright-Policy + Trainingsdaten-Zusammenfassung; bei systemischem Risiko entfällt die Ausnahme — zentraler Hebel für DeepSeek/Qwen & Co.
- Code of Practice for GPAI (freiwillig, Compliance-Nachweis): unterzeichnet von Anthropic, Google, Microsoft, Mistral, OpenAI; Meta NICHT, chinesische Anbieter NICHT (https://artificialintelligenceact.eu/introduction-to-code-of-practice/). Das einzige „technisch prüfbare" Instrument ist ein Opt-in.
- Art. 50 (Kennzeichnung KI-Inhalte, Wasserzeichen) ab 2.8.2026 anwendbar; technische Standards noch in Ausarbeitung (?).
- Wasserzeichen bei offenen Gewichten durch Fine-Tuning entfernbar (?) — Fachdiskussion, nicht EU-amtlich belegt.
- Zuständigkeit: AI Office (EU) für GPAI, nationale Marktaufsicht für Deployer — Doppelstruktur, Kapazität unbeziffert (?).

HAUPTSATZ: Die EU-Pflichten nach Art. 53 treffen offene chinesische Gewichte nur bei nachgewiesenem Überschreiten der 10^25-FLOP-Schwelle voll, während geschlossene US-Modelle über den freiwilligen Code of Practice bereits teilweise erfasst sind.
EINWAND: Ein Schwellenwert, der an selbstberichteten Compute-Zahlen hängt, ist bei Open-Weight-Modellen praktisch nicht verifizierbar.
KRITERIUM: Etabliert die EU eine anbieterunabhängige Compute-Schätzung (Cloud-Meldepflichten, Chip-Exportdaten)? Ohne sie bleibt das System selbstauskunftsbasiert.

## gegenposition (claude-sonnet-5)

- Offene Gewichte nach Veröffentlichung technisch nicht mehr an EU-Attestierung bindbar: Hash/Signatur bricht bei jedem Fork/Fine-Tune — Vollzug erreicht nur den Erstupload, nicht Millionen Derivate.
- Geschlossene US-Modelle liefern „Prüfbarkeit" faktisch nur als Selbstauskunft (Model Cards, freiwilliger CoP); echte Verifikation der Trainingsläufe bislang nicht durchgesetzt (?).
- „Einheitlich" zwingt zwei inkompatible Regime zusammen: Output-Wasserzeichen bei Closed vs. Gewichts-Signierung bei Open — beide unabhängig umgehbar.
- Wettbewerbsasymmetrie/Adverse Selection: volle Compliance-Last trägt, wer kooperiert; Nutzer laden chinesische Gewichte direkt von Hugging Face — kein Vertriebsakt in der EU als Ansatzpunkt.
- Zuständigkeit fragmentiert (AI Office vs. nationale Behörden, DSA-Erfahrung: Ressourcenmangel bei technischen Audits) (?).

HAUPTSATZ: Die EU kann über Art. 53 ff. ein einheitliches Nachweissystem durchsetzen, das beide Modellwelten gleichermaßen erfasst.
EINWAND: Offene Gewichte entziehen sich nach Erstveröffentlichung jeder fortlaufenden Attestierung — der Kontrollpunkt „Marktzugang" existiert für sie nicht.
KRITERIUM: Können EU-Behörden Sanktionen gegen Downstream-Verbreiter ohne EU-Niederlassung durchsetzen? Ohne das bleibt das System bei offenen Gewichten wirkungslos.

## geschichte (claude-sonnet-5)

- IAEA-Safeguards: funktionierten, weil der Kontrollpunkt physisch war (spaltbares Material). KI-Gewichte sind kopierbare Software → analoger Kontrollpunkt fehlt; Kandidat wäre Trainings-Compute/Chips (vgl. US-Exportkontrollen 2022ff.).
- Basel-II/III: einheitliche Kennzahlen via Selbstauskunft + Prüfer-Testat, nicht Rohdaten-Zugriff; zeigte aber Metrik-Arbitrage (?).
- HACCP: Prozess- statt Produktkontrolle, weil Endprodukt nicht rückwirkend prüfbar — im Kern der Ansatz des GPAI-Code-of-Practice.
- ICAO/EASA-Flugsicherheit: global durchgesetzt über Marktzugang (kein Zertifikat → kein Landerecht) — der einzige EU-Hebel auch hier.
- Wassenaar/Krypto-Kriege: sobald ein Gut nicht mehr physisch grenzüberschreitet, bricht das Kontrollregime; offene China-Modelle strukturell wie Verschlüsselungssoftware der 1990er.
- DSGVO: einziges Beispiel erzwungener globaler Compliance — via Marktzugang + Bußgelder; stark bei zentralisierten Diensten, schwach bei frei kopierbaren Artefakten.

HAUPTSATZ: Alle bisherigen erfolgreichen Nachweisregime (IAEA, ICAO, GDPR) setzten am Marktzugang oder einem physischen Flaschenhals an, nie am Produkt selbst.
EINWAND: Offene Gewichte sind kein Marktzugangsgut mehr, sobald sie einmal veröffentlicht sind.
KRITERIUM: Gibt es einen prüfbaren Kontrollpunkt VOR dem Kopiervorgang (Trainings-Compute, Erstinverkehrbringung) — oder nur danach (Nutzung in der EU)?

## betroffene (claude-sonnet-5)

- Startup-Entwickler (Berliner SaaS): bei geschlossenen US-Modellen prüft der Anbieter zentral; bei offenen China-Gewichten trifft die Nachweispflicht faktisch den Downloader (?).
- Behörden-Beschaffung: für US-Anbieter mit EU-Bevollmächtigtem adressierbar; für rein chinesische Anbieter fehlt die greifbare Rechtsperson — Beschaffung weicht de facto auf „geprüfte" US/EU-Modelle aus.
- Forscher/OSS-Community: werden je nach Ableitungstiefe selbst „Anbieter" — Kaskadeneffekt, Rechtsunsicherheit (?).
- Endnutzer: merken Prüfmechanik nur indirekt — verzögerte EU-Rollouts, Feature-Downgrades, Nichtangebot.
- Compliance-Abteilungen: bei offenem Modell + eigenem Fine-Tuning ZWEI Nachweisketten statt einer — mehr Aufwand trotz „transparenterer" Gewichte.

HAUPTSATZ: Offene Gewichte sind lokal auditierbar, geschlossene nur via Selbstauskunft — ein einheitliches System bräuchte zwei Vollzugslogiken statt einer.
EINWAND: Gerade weil offene Gewichte einsehbar sind, könnte die EU dort strenger prüfen (Reproduzierbarkeit) als bei Blackbox-APIs — die Asymmetrie liefe technisch ZUGUNSTEN offener Modelle.
KRITERIUM: Hat die EU durchsetzbare Sanktionen gegen Anbieter ohne EU-Niederlassung? Ohne das bleibt das System für diese Gruppe freiwillig.

## technik (claude-sonnet-5)

- Evals: zeigen Verhalten im Test, nicht im Feld — Kontamination, Gaming, Sampling-Varianz. Eval bestanden ≠ sicher.
- Interpretierbarkeit/„Linsen" (SAEs, Probing): brauchen Weißbuch-Zugriff — nur bei offenen Gewichten oder freiwillig kooperierendem Anbieter. Geschlossene API = Blackbox.
- Audit-Logs/Attestierung (signierte Trainingsläufe, TPM/Confidential Computing): technisch noch unreif, selten produktiv (?).
- Missverständnisse: Eval-Zertifikat ≠ TÜV-Siegel (Stichprobe!); Erklärbarkeit ≠ Auditierbarkeit; „offen = transparent" kippt nach Download in „offen = unkontrollierbar".
- EU-Hebel: bei US-Anbietern die API/der Marktzugang; bei offenen China-Gewichten zwangsläufig der EU-Deployer. Umgehung: Mirrors, Fine-Tuning entfernt Marker, Self-Hosting ohne Telemetrie.
- Wettbewerbskosten: Compliance trifft kleine/offene Anbieter härter als kapitalstarke Closed-Labs.

HAUPTSATZ: Die EU kann geschlossene US-Modelle über den API-Kontrollpunkt zwingen, hat aber gegenüber frei herunterladbaren Gewichten ohne EU-Herausgeber keinen äquivalenten Hebel.
EINWAND: Auch bei geschlossenen APIs bleibt der Nachweis Selbstauskunft — echte Interpretierbarkeitsprüfung bräuchte Weißbuch-Zugriff, den keine Behörde erzwingen kann.
KRITERIUM: Setzt der Mechanismus am EU-Deployer an (durchsetzbar unabhängig vom Ursprungsland) statt am Hersteller?

## geld (claude-sonnet-5)

- Marktlücke Provenienz-Infrastruktur: Wasserzeichen/C2PA-Zertifizierung als neuer Prüfmarkt (TÜV-artige Player) (?).
- Regulatory Moat: Große (OpenAI, Anthropic, Google) tragen Compliance leichter als EU-Startups/OSS — Muster seit DSGVO.
- Anreize fürs MITMACHEN: (a) EU-Marktzugang teurer zu verlieren als Compliance kostet; (b) Standard-Setzung — wer früh liefert, macht die eigene Lösung zur Referenz (C2PA-Muster); (c) Vertrauens-Differenzierung ggü. Anbietern ohne Nachweis als Verkaufsargument in Behörden-/Enterprise-Deals; (d) serverseitige Kennzeichnung ist für API-Anbieter technisch billig.
- Wackelt: Geschäftsmodell offener Gewichte — serverseitige Kennzeichnung dort umgehbar (lokal ausführen, Wasserzeichen raus-trainieren); Nachweispflicht nur für APIs verschiebt Nutzung zu offenen Modellen (?).
- Kontrollpunkt-Ökonomie: erzwingbar eher an Distribution (App Stores, Cloud, Plattformen) als an der Modell-Quelle — Gatekeeper gewinnen Durchsetzungsmacht (?).
- Quellen: urbanstudio.de/blog/ki/ki-kennzeichnungspflicht-eu-ai-act/, kileague.de/blog/artikel-50-eu-ai-act-kennzeichnungspflicht-it-dienstleister, rethink.consulting (Art. 50 ab Aug. 2026).

HAUPTSATZ: Der freiwillige EU-Transparenz-Code (Juni 2026) baut auf serverseitiger Wasserzeichen-Kennzeichnung nach Art. 50 auf.
EINWAND: Serverseitige Kennzeichnung ist bei offenen Gewichten nicht erzwingbar — das System trifft strukturell nur geschlossene Anbieter.
KRITERIUM: Gilt die Norm auch für Distributionskanäle offener Gewichte (App Stores, Cloud-Marktplätze, HF-Downloads) — oder nur für API-Endpunkte?

## risiken (claude-sonnet-5)

- Papier-Compliance: GPAI-Kodex freiwillig, Lücke bis harmonisierte Normen ~2027 (?) — Doku ohne Verhaltensprüfung, Analogie DSGVO-Compliance-Theater.
- Gaming: Modelle auf Testfragen optimiert oder „eval-aware". Gegenmittel: verdeckte/rotierende Red-Team-Sets, Forscherzugang (Vorbild DSA Art. 40).
- Offene Gewichte: kein Kontrollpunkt nach Veröffentlichung; Zertifikat der Ursprungsversion sagt nichts über Forks.
- Marktrückzug als Umgehung: Meta verzögerte multimodale Llama-Modelle in der EU — EU-Nutzer bekommen ältere Versionen, unregulierte Gewichte sickern trotzdem ein.
- Prüfstellen-Kapture (Parallele Rating-Agenturen vor 2008); selektive Durchsetzbarkeit (Geschäftsgeheimnis; Sonderbehandlung bekannter Prüf-IPs); Threshold-Gaming (FLOP-Schwelle splitten; DeepSeek-Debatte über Schwellenanpassung, pinsentmasons.com).
- Was hilft: Ex-post-Stichproben statt Selbstdeklaration, Forscherzugang, Sanktionen an nachweisbaren Schaden koppeln.

HAUPTSATZ: Die aktuelle EU-Regelung beruht überwiegend auf Selbstauskunft, nicht auf unabhängiger technischer Prüfung.
EINWAND: Auch Selbstauskunft erzeugt Haftungs- und Reputationskosten — Papier-Compliance ist nicht wirkungslos, nur schwächer.
KRITERIUM: Bekommen unabhängige Dritte verdeckten Zugriff auf nicht vorab bekannte Testfälle? Nur dann ist Gaming strukturell erschwert.

## zukunft (claude-sonnet-5)

- PLAUSIBEL — Zwei-Klassen-Nachweis: US-Anbieter via API-Nachweise erfasst; offene China-Gewichte nach Download unkontrollierbar; Verifikation wird faktisch Deployment-Pflicht („wer in der EU anbietet, labelt"). WENDEPUNKT: erste große Bußgeld-Causa gegen US-Anbieter + öffentlich gescheiterter Vollzug gegen Reseller eines offenen Modells (?).
- ÜBERRASCHEND — Compute-Infrastruktur statt Modell-Ebene: Attestierung über Cloud-KYC + Secure-Enclave/TPM bei EU-Rechenzentren; erfasst auch offene Gewichte, sofern Training/Serving EU-Infrastruktur berührt; chinesische Anbieter übernehmen den Standard für Exportmärkte (Hardware-Lock-in wirkt stärker als Gesetzestext). WENDEPUNKT: NVIDIA-/Hyperscaler-getriebener Attestierungs-Standard aus dem Exportkontroll-Rennen (?).

HAUPTSATZ: Technisch prüfbarer Nachweis ist bei geschlossenen Modellen über API-Kontrollpunkte durchsetzbar, bei veröffentlichten offenen Gewichten nicht mehr.
EINWAND: Auch API-Nachweise sind umgehbar (Shadow-Deployments, Proxys) — die Trennung ist graduell, nicht kategorisch.
KRITERIUM: Wird die erste EU-Enforcement-Aktion gegen einen Open-Weight-Anbieter je vollstreckbar?

## Tausch-Runde (mit Kondensat Thema B)

1. **Sanktion bei Falschdokumentation heilt das Selbstauskunft-Problem** — nicht „ist das Modell sicher" (ex ante unprüfbar), sondern „war die Meldung wahr" (justiziabel wie Bilanzbetrug/SOX). Bricht aber bei offenen Gewichten: nach Release existiert kein haftender Adressat mehr — der Straftatbestand verpufft genau am Kontrollverlust-Punkt.
2. **„Einheitlich" ist konzeptionell falsch, nicht nur schwer:** Zwei Sanktionslogiken nötig — Falschdokumentation beim Anbieter (Closed) vs. Pflichten beim EU-Deployer (Open).
3. **CCP-Kriterium als Diagnose für Art. 53:** FLOP-Schwelle ist messbar, aber nicht unabhängig — verfehlt den CCP-Standard strukturell (?). Als Prüfraster auf jede Code-of-Practice-Klausel anwendbar: echte CCPs vs. Papier-Compliance.
4. **Versicherer-Pfad als Deployer-Hebel:** Versicherungspflicht für Deployer (Kfz-Haftpflicht-Analogie) verlagert den Audit-Anreiz auf private Versicherer — die EU muss nur die Versicherungspflicht durchsetzen, das kann sie territorial ohne Anbieterzugriff.
5. **Konsortium vertieft die Spaltung:** Ein Lab-Prüfkonsortium bestünde vermutlich aus den CoP-Unterzeichnern — Meta + China blieben draußen; der private Standard verschärft die Zwei-Klassen-Struktur und schafft Kartellrisiko.
6. **Rückruf-Unmöglichkeit macht es kategorial:** Ohne durchsetzbare Letzt-Sanktion ist ein Nachweissystem für offene Gewichte keine Aufsicht, sondern Beobachtung.

SYNTHESE-THESE: Ein technisch prüfbares EU-Nachweissystem kann nur existieren, wo Falschdokumentation justiziabel UND eine Sanktion vollstreckbar ist — bei geschlossenen Modellen beides über den Anbieter, bei offenen Gewichten beides nur über versicherungspflichtige EU-Deployer; „einheitlich" ist strukturell unmöglich, die EU muss zwei gekoppelte, aber getrennte Regime bauen.
