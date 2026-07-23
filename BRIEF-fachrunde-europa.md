# BRIEF: Fachrunde „Europas Rolle" (Double-Eight-Lauf) — 23.7.2026

**Auftraggeber:** Jay (Go 23.7. ~2:00, „dann kann es losgehen").
**Ziel:** Aus Jays HACCP/Schweiz-These einen belastbaren Text destillieren,
der als Kommentar/Leserbrief Richtung FAZ o. ä. taugt.
**Werkzeug:** `files/story-recherche/recherche.py` (Praktis unseres Gratis-LLM-Gateways,
8 Blickwinkel × 2 Themen + Tausch-Runde = 18 Calls, EIN Lauf).

## Die zwei Themen (Double Eight) — geschärft nach Sol-Meeting 23.7.

- **A:** „Kann die EU für geschlossene US-Modelle und offene chinesische
  Modellgewichte ein einheitliches, technisch prüfbares Nachweissystem
  durchsetzen — und an welchen Kontrollpunkten, Zuständigkeiten,
  Umgehungswegen und Wettbewerbskosten entscheidet sich dessen Erfolg?"
- **B:** „Wie sähe ein HACCP-artiges KI-Regime (dokumentierte kritische
  Kontrollpunkte, unabhängige Prüfung, Sanktionen) konkret aus — welche
  Schäden könnte es besser begrenzen als Verhaltensverbote, welche
  ausdrücklich nicht?"
- **Matrix-Pflicht (Sol):** Jeder Blickwinkel liefert zusätzlich EINEN
  überprüfbaren Hauptsatz, den stärksten Einwand dagegen und EIN konkretes
  Entscheidungskriterium — nur vollständige Dreier zählen als Substanz.

## Rollen

| Rolle | Wer | Aufgabe |
|---|---|---|
| 8 Blickwinkel je Thema | Praktis unseres Gratis-LLM-Gateways (auto/best-free) | Rohmaterial: Fakten, Gegenposition, Geschichte, Betroffene, Technik, Geld, Risiken, Zukunft |
| Tausch-Runde | Praktis | Thema A mit Bs Material querlesen + umgekehrt |
| Planung/Blindstellen | Sol (gpt-5.6-sol) | Meeting DAVOR: Gremium-Design prüfen |
| Gegenprüfung | Terra (gpt-5.6-terra) | Meeting DAVOR: Angriff auf Thesen + Lauf-Design; DANACH: Synthese-Review |
| Synthese + FAZ-Destillat | Fable | Aus 18 Berichtsteilen EINEN Text (≤ 1 Seite), Fakten markiert prüfen |
| Abnahme | Jay | Liest nur das Destillat; Rohberichte optional |

## Regeln (EISERN)

1. Nur öffentliche Inhalte an die Praktis — nichts Privates, keine Session-Details.
2. KEINE Test-Pings an den Pool. Start erst, wenn der reguläre Prakti-Blick
   (3:20/9:20) im cron.log Erfolg meldet („neue bewertet").
3. Alles Unsichere im Rohmaterial trägt (?); jedes Zitat/jede Zahl wird vor dem
   FAZ-Destillat von Fable gegen echte Quellen geprüft — Praktis liefern
   Denkrichtungen, keine Belege.
4. EIN Lauf. Wiederholung/Ausweitung nur auf neues Jay-Go (schwere Läufe-Regel).
5. Fehler sichtbar: fehlgeschlagene Blickwinkel stehen als FEHLER im Bericht.

## Abbruchkriterien (verschärft nach Sol: Substanz statt Call-Zählung)

- Phase 1 liefert bei einem Thema < 5/8 Blickwinkel MIT vollständiger
  Dreier-Matrix (nicht bloß erfolgreiche Calls) → keine Synthese;
  Meldung an Jay.
- Prakti-Blick meldet bis 11:00 keinen Erfolg → Lauf verschieben, Meldung an Jay.
- Widersprechen sich Rohmaterial-„Fakten": ERST Quellencheck durch Fable
  (echte Quellen entscheiden); These-Text nur, wenn der Check nichts klärt.

## Synthese-Checkliste (aus dem Meeting davor — Destillat gilt nur damit als fertig)

1. **Souveränitäts-Einwand vorwegnehmen (Terra):** Nachlesbarkeit schafft
   keine Souveränität, wenn Europa Gewichte/Daten/Rechenzugang nicht
   erzwingen kann — sonst klingt „Prüfinstanz" nach Selbstaufwertung.
2. **Kollisionsfall-Test (Sol):** Die These an EINEM konkreten Fall zeigen —
   derselbe riskante KI-Dienst kommt einmal als geschlossene US-API, einmal
   mit offenen China-Gewichten nach Europa; welche Nachweise an welchen
   Kontrollpunkten?
3. **AI Act ehrlich einordnen (Terra):** HACCP-Ansatz als Ergänzung/Schärfung,
   nicht als Gegenentwurf verkaufen.
4. **Echo-Rabatt (Terra):** Talking Points, die über viele Blickwinkel
   identisch wiederkehren, zählen als EIN Signal, nicht als Konsens-Beweis.
5. Europas Machtlücke (keine Frontier-Modelle, Chips, Cloud) ausdrücklich
   benennen.
6. **Konstruktiver Schluss (Jay, 23.7. ~2:30):** Nicht für/gegen den AI Act
   positionieren — Angebot statt Schiedsrichter-Pose: ein neutrales,
   lab-übergreifendes Forschungs-Lab für Nachlesbarkeit (CERN-Muster, aber
   Prüf-Forschung statt Konkurrenz-Modell), an dem OpenAI und Anthropic
   teilnehmen WOLLEN. Der Anreiz muss benannt sein (Vertrauen als
   Marktzugang, geteilte Prüfkosten, Legitimität, und — Jay: der stärkste —
   Ziele MITentscheiden statt Regeln empfangen) — sonst bleibt es
   Einladungsprosa.
7. **Aufhänger (Jay):** Der Sol/METR-Schummel-Befund als Zeitfenster —
   entweder die Labs kommen jetzt mit nachlesbarer Prüfung an den Tisch,
   oder die EU greift reflexhaft zum Regelkatalog. Anthropic als Beleg,
   dass ein Frontier-Lab bereits offen mit Interpretierbarkeit arbeitet
   (Fakten-Check vor Verwendung: METR-Befund korrekt zitieren).

## Ablauf

1. ✅ Brief (dieses Dokument)
2. Team-Meeting DAVOR: Sol + Terra parallel, Berichte nach
   `plans/fachrunde-europa/` — Einwände einfalten
3. Watcher wartet auf Pool-Lebenszeichen im cron.log → feuert
   `recherche.py "A" "B"` genau EINMAL
4. Fable-Synthese: FAZ-Destillat (≤ 1 Seite) + Kennzeichnung „KI-gestützte
   Recherche" — Veröffentlichung entscheidet allein Jay
5. Team-Meeting DANACH: Terra reviewt Destillat, Sol bewertet Prozess;
   Berichte gleiche Stelle
6. Alles committen + pushen, Jay bekommt EINE Fertig-Meldung

## Abnahme & Risiken

- **Vorschau ≠ Start:** Der Watcher startet den Lauf erst bei Log-Beweis,
  nicht auf Verdacht. Feuert genau einmal, dann Exit.
- **In-flight-Race:** Läuft der Prakti-Blick 9:20 während unser Lauf feuert,
  teilen sich beide den Pool — akzeptiert, Retry-Logik (3×, 15/30 s) fängt es.
- **Qualitätsrisiko:** Gratis-Praktis halluzinieren Zahlen. Gegenmittel:
  Regel 3 (Fakten-Check vor Destillat) + Terra-Review danach.
- **Abnahmebeleg:** 2 Rohberichte in `files/story-recherche/berichte/`,
  4 Team-Berichte in `plans/fachrunde-europa/`, 1 FAZ-Destillat ebenda.
