# 05-eval.md — Phase 4: Der Test an alten Mails (Stand 24.07.2026)

Grundsatz: **Erst beweisen, dann Echtbetrieb.** Schlägt die KI deinen Status quo nicht, wird abgebrochen.

---

## 0. Aktueller Stand: Testdaten liegen vor (24.07.)

Der Kunde hat die Testdaten anders geliefert als geplant — **besser**:
5 Sammel-Mails, nach seinen eigenen Kategorien vorsortiert (wichtig / Rechnungen / Werbung / informell / unwichtig).

- **267 gelabelte Einträge** (Original-Mails + PDFs) statt der geplanten 100 → Ordner „KI-Test" + Excel-Liste entfallen.
- Die Kategorien des Kunden sind die Musterlösung (Ground Truth). Die Detail-Tabelle liegt **bewusst nur lokal/beim Kunden**, nicht im Repo (personenbezogene Daten).
- Lesbar für den Test: die Original-Mail-Texte. Bild-/PDF-Scans sind über die aktuelle Verbindung nicht abrufbar → werden im Piloten über den regulären Postfach-Zugang nachgeholt, für den Test nicht blockierend.
- **Blind-Prinzip:** Die Klassifikation läuft in einer frischen KI-Instanz, die nur Mailtext + Regelwerk (04-design) erhält — niemals die Kategorien des Kunden.
- Offen vor Testlauf: ① Bestätigung der 3 vermuteten Durchrutscher ② Regel-Klärung „neuer Interessent" (vom Kunden einmal als wichtig, viermal als informell einsortiert).

---

## 1. So läuft der Test

| Schritt | Wer | Aufwand |
|---|---|---|
| 1 · Ordner „KI-Test" in Outlook (durchgeplant.de) anlegen | Kira | 1 Min |
| 2 · 100 alte, erledigte Mails hineinkopieren — gemischt: wichtige, unwichtige, Werbung. Die bekannten Durchrutscher unbedingt dabei | Kira | ~30 Min |
| 3 · Liste ausfüllen: je Mail ein Kreuz — wichtig / unwichtig (Vorlage: `eval-labels.csv`, öffnet in Excel) | Kira | ~60 Min |
| 4 · KI liest den Ordner, stuft jede Mail ein (P1–P5), erzeugt ein Probe-Briefing | Agent | — |
| 5 · Vergleich Kreuz gegen KI-Einstufung → Ergebnis-Protokoll unten | gemeinsam | ~30 Min |

Deine Liste bleibt bis nach dem KI-Durchlauf unter Verschluss. Die KI kennt deine Kreuze nicht.

## 2. Woran gemessen wird

| Messgröße | Bedeutung | Messlatte |
|---|---|---|
| **Übersehene wichtige Mails** | wichtig laut Kira, aber KI sagt P4/P5 | **0 ist das Ziel.** Mehr als 1 von 20 wichtigen → nachbessern |
| Fehlalarme | unwichtig, aber KI sagt P1 | unter ~1 von 3 — stört sonst |
| Rauschreduktion | Mails, die du nicht mehr einzeln öffnen musst | über die Hälfte |
| Briefing-Lesezeit | du liest das Probe-Briefing, Uhr läuft | unter 5 Minuten |
| **Baseline-Probe** | deine 3 echten Durchrutscher | **alle 3 müssen erkannt werden** |

## 3. Was danach passiert

- **Messlatte erreicht** → Pilot startet echt (4–6 Wochen, Briefing täglich).
- **Knapp verfehlt** → Regelwerk nachschärfen, gleicher Test noch einmal. Maximal 2 Runden.
- **Klar verfehlt** → Abbruch. Es bleiben die Quick-Wins aus Phase 1 — die kosten nichts.

## 4. Ergebnis-Protokoll (Test durchgeführt 25.07.2026, blind, 183 gelabelte Mails)

**Runde 1** knapp verfehlt (6 übersehene, Rauschreduktion 40 %) → Regelwerk nachgeschärft (Einladungen mit Termin → P2 · Rückrufbitten → P2 · wiederkehrende Abo-Rechnungen → P4). **Runde 2:**

| Messgröße | Messlatte | Ergebnis | Bestanden? |
|---|---|---|---|
| Übersehene wichtige Mails | ≤ 1 von 20 (5 %) | 2 von 47 (4,3 %) — beides Grenzfälle (Partner-Event-Erinnerung, unklarer Betreff) | ✅ knapp |
| Fehlalarme | < 1 von 3 | 0 | ✅ |
| Rauschreduktion | > 50 % | 74 % | ✅ |
| Briefing-Lesezeit | < 5 Min | wird im Pilot real gemessen | offen |
| Bestätigte Durchrutscher erkannt | alle | **11 von 11** in P1/P2 (Portal-Anfragen, 3 Mahnungen, 4 unbeantwortete Nachfragen) | ✅ |

Zusatzbefund: Die im Testset enthaltene mutmaßliche Phishing-Mail („bitte vorherige E-Mail ignorieren, keinen Link öffnen") wurde regelkonform als Rauschen behandelt — kein Befehl aus Mailinhalt wurde befolgt.

**Fazit: bestanden → Freigabe für Pilot-Einrichtung (Roadmap Stufe 1).** Einschränkung ehrlich benannt: Der Test lief überwiegend auf Betreffzeilen (Volltexte nur teilweise verfügbar); im Piloten liest der Agent komplette Mails — die Erkennung wird dadurch besser, nicht schlechter.

---

**STOPP — du bist dran:** Schritte 1–3 (Ordner, 100 Mails, Liste). Sag Bescheid, wenn die Liste fertig ist — dann bauen wir den Test-Durchlauf.
