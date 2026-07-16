# 03-optionen.md — Phase 2: Architektur-Optionen & E1-Risikovergleich (Stand 16.07.2026)

Zwei Entscheidungen stecken in diesem Dokument:
**Teil 1:** *Was* darf der Agent tun? (Optionen A–D)
**Teil 2:** *Wo* denkt die KI? (lokal / EU-Cloud / US-Anbieter) — dein offener Punkt E1, mit dem zugesagten Risikovergleich.

---

## Teil 1 — Die vier Architektur-Optionen

*(Zur Erinnerung: R1–R9 sind die Rest-Probleme aus Phase 1 — das, was Microsoft-Bordmittel nicht können.)*

### Option A — Read-only-Triage (der Agent liest nur)

**Was passiert:** Der Agent bekommt je Firma eine „Schlüsselkarte", die **ausschließlich Lesen** erlaubt (Graph-API-Berechtigung `Mail.Read` — technisch ist Senden/Löschen/Ändern damit unmöglich, nicht nur verboten). Er liest neue Mails, ordnet ein, und erzeugt:
- das **7:30-Briefing** als Mail an dich + Excel-Anhang (Handlungsbedarf heute / diese Woche / FYI / Rauschen-Zusammenfassung)
- den **Sofort-Alarm** bei Kaufsignal, Eskalation, Frist

| | |
|---|---|
| Rechte | Nur Lesen — die niedrigste Stufe, die es gibt |
| Löst | R1 (Erkennung), R2 (Überblick/Briefing), R3 (Zusammenfassen statt Löschen), R4 (Fristen), R6 (Kontaktkontext), R7 (Wiederkehr-Überwachung) |
| Risiko | Minimal. Schlimmster Fall: Das Briefing ist falsch — deine Postfächer bleiben unberührt. Selbst bei Prompt Injection (bösartige Mail versucht, die KI umzuprogrammieren) kann nichts gesendet oder gelöscht werden — die Schlüsselkarte passt nicht ins Schloss |
| Aufwand | 4 App-Registrierungen (je Tenant eine, mit Anleitung machbar), Pilot startet mit 1 |

### Option B — Kategorisierung (der Agent darf Etiketten kleben)

**Was passiert:** Zusätzlich zu A darf der Agent **Kategorien und Flags setzen** — die farbigen Etiketten aus Phase 1 (🔴 Eskalation, 🟢 Interessent, 🔵 Rechnung, 🟣 Behörde) erscheinen direkt in deinem Outlook, am PC und in der Handy-App. Geflaggte Mails landen automatisch in Microsoft To Do (R5).

| | |
|---|---|
| Rechte | Lesen + Ändern von Metadaten (`Mail.ReadWrite`). Ehrlicherweise: Diese Berechtigung *könnte* technisch auch Mails verschieben/löschen — das begrenzen wir organisatorisch (Protokollierung, Stichproben) und im Code |
| Löst | R5 (Todos), macht A im Alltag sichtbar — du siehst die Priorisierung *in* Outlook, nicht nur im Briefing |
| Risiko | Klein. Schlimmster Fall: falsches Etikett. Mails selbst bleiben unversehrt; Kategorien sind mit einem Klick korrigierbar (und deine Korrektur ist zugleich Trainings-Feedback) |
| Aufwand | Wie A plus Kategorien-Logik |

### Option C — Eigene Oberfläche (eine fünfte App) — VERWORFEN

**Was es wäre:** Ein eigenes Dashboard/Webseite, auf der du deine priorisierten Mails siehst.

**Warum nicht:** Das Argument dagegen ist ernst — du hast heute *vier* Orte und übersiehst Dinge; ein *fünfter* Ort löst das Gegenteil aus. Jede neue Oberfläche konkurriert mit Outlook um deine Aufmerksamkeit, veraltet, und stirbt nach drei Wochen Begeisterung. Dein eigenes Kriterium („keine neue Insel") schließt C aus. Alles, was C könnte, leisten Briefing-Mail (A) + Etiketten in Outlook (B) an Orten, wo du ohnehin bist.

### Option D — Entwurfs-Agent (die KI schreibt vor, du sendest) — SPÄTER

**Was passiert:** Der Agent legt für geeignete Mails fertige Antwortentwürfe in den **Entwürfe-Ordner** der jeweils richtigen Firma. Senden kannst nur du. Ton kundenabhängig (aus dem Kontaktkontext), Signatur je Firma.

| | |
|---|---|
| Rechte | Schreiben in den Entwürfe-Ordner — die höchste Stufe, die wir je vergeben (Senden bleibt technisch ausgeschlossen) |
| Löst | R8 |
| Harte Regeln (aus deinem G3 + Original-Constraints) | **Nie entwerfen:** Preise/Angebote/Nachträge · Zusagen · Termine ohne Kalenderabgleich · rechtswirksame Erklärungen. Solche Mails werden nicht entworfen, sondern im Briefing **eskaliert**: „Hier musst du selbst ran" |
| Risiko | Mittel: Ein Entwurf könnte versehentlich ungeprüft gesendet werden oder erfundene Fakten enthalten. Deshalb erst nach Vertrauensnachweis aus A+B (Phase 5 regelt die Freischalt-Kriterien) |

### Empfehlung Teil 1

**Pilot = A + B auf hm@durchgeplant.de.** Read-only-Briefing als Fundament, Kategorien als sichtbarer Alltagsnutzen. D folgt frühestens nach 4–6 Wochen nachgewiesener Qualität (Messung in Phase 4). C bleibt verworfen.

**Wann diese Empfehlung falsch wäre:** Wenn du feststellst, dass du das Briefing nicht liest (dann ist B allein besser) — oder wenn 90 % deiner Zeit im *Antworten* steckt statt im *Sichten* (dann müsste D früher kommen, mit engeren Leitplanken).

---

## Teil 2 — Der E1-Risikovergleich: Wo darf die KI denken?

**Die Ausgangslage ehrlich benannt:** Deine Mails liegen *heute schon* vollständig bei Microsoft — einem US-Konzern mit EU-Rechenzentren, abgesichert über einen AVV (Auftragsverarbeitungsvertrag = der Vertrag, der einen Dienstleister verpflichtet, deine Daten nur für dich zu verarbeiten und zu schützen). Die E1-Frage ist also nicht „Cloud ja/nein" — diese Entscheidung ist mit Microsoft 365 längst gefallen. Die echte Frage ist: **Welcher ZUSÄTZLICHE Dienst darf die Mails zum Zweck der Auswertung lesen?**

### Weg 1 — Nur lokal (eigener Rechner, z. B. Ollama mit Mistral- oder Qwen-Modell)

*Ollama = kostenloses Programm, das KI-Modelle auf deinem eigenen Rechner laufen lässt. Mistral (Frankreich) und Qwen sind solche frei verfügbaren Modelle.*

| Aspekt | Bewertung |
|---|---|
| Datenschutz | ⭐⭐⭐ Kein Byte Mailinhalt verlässt dein Haus. Kein zusätzlicher AVV nötig, keine Drittland-Frage. Rechtlich die bequemste Position |
| Qualität | ⭐ **Hier muss ich ehrlich sein — und das trifft genau dich:** Deine Kernaufgabe ist R1, *feine* semantische Erkennung („klingt diese höfliche Mail nach Eskalation?", „ist ‚können wir nochmal telefonieren' ein Kaufsignal?"). Genau bei solchen Zwischentönen sind lokale Modelle am schwächsten. Grobe Sortierung: ok. Deine zwei teuersten Fehlerfälle zuverlässig erkennen: fraglich. Das Risiko wandert vom Datenschutz in die **übersehene wichtige Mail** — dein teuerster Fehler laut Constraint |
| Kosten | Hardware einmalig ca. 1.500–4.000 € (Rechner mit starker Grafikkarte, läuft 24/7) |
| Betrieb | ⭐ Updates, Ausfälle, Modellpflege — bei „ich selbst mit Anleitung" (H5) realistisch die höchste Hürde. Kein Anbieter-Support |

### Weg 2 — EU-Cloud mit AVV (z. B. Mistral La Plateforme/Frankreich, IONOS AI, Azure OpenAI mit EU-Datenresidenz)

| Aspekt | Bewertung |
|---|---|
| Datenschutz | ⭐⭐ Daten verlassen dein Haus, bleiben aber in der EU unter EU-Recht. AVV nach Art. 28 DSGVO ist Standard-Papierkram (vorformuliert, online abschließbar). Rechtsgrundlage: berechtigtes Interesse (Art. 6 Abs. 1 lit. f — effiziente Bearbeitung eingehender Geschäftspost; gut begründbar, einmal dokumentieren). Kein Drittlandtransfer |
| Qualität | ⭐⭐ Gut. Für Briefing, Zusammenfassung, klare Kaufsignale völlig ausreichend. Bei den feinsten Zwischentönen etwas hinter Weg 3 |
| Kosten | ca. 5–30 €/Monat bei deinen ~50 Mails/Tag (nur Text, keine Anhänge nötig für Triage) |
| Betrieb | ⭐⭐⭐ Kein eigener Server, Anbieter wartet. Sonderfall Azure OpenAI: läge sogar im Microsoft-Kosmos, wo deine Mails ohnehin sind — minimaler „neuer" Vertragspartner |

### Weg 3 — US-Anbieter mit AVV + Standardvertragsklauseln (z. B. Anthropic/Claude, OpenAI)

*Standardvertragsklauseln (SCC) = von der EU vorgegebene Vertragsbausteine, die Datenübermittlung in Nicht-EU-Länder rechtlich absichern; ergänzt durch das EU-US Data Privacy Framework.*

| Aspekt | Bewertung |
|---|---|
| Datenschutz | ⭐ bis ⭐⭐ Rechtlich machbar und weit verbreitet (dieselbe Konstruktion, über die auch Microsoft 365 selbst abgesichert ist!) — aber: Drittlandtransfer muss dokumentiert werden, theoretisches Zugriffsrisiko von US-Behörden, und die Rechtslage zu EU-US-Transfers wackelt historisch alle paar Jahre. Bei 4 Verantwortlichen (3 GmbH + Einzelfirma) heißt das: 4× AVV, 4× Transfer-Dokumentation |
| Qualität | ⭐⭐⭐ Beste verfügbare Modelle — den Unterschied merkst du genau bei R1-Zwischentönen und später bei der Entwurfsqualität (D) |
| Kosten | ca. 10–40 €/Monat |
| Betrieb | ⭐⭐⭐ Wie Weg 2 |

### Entscheidungstabelle

| Kriterium (gewichtet nach DEINEN Constraints) | Lokal | EU-Cloud | US+AVV |
|---|---|---|---|
| Übersieht keine wichtige Mail (dein teuerster Fehler!) | ⚠️ schwächste | ✅ gut | ✅ am besten |
| Datenminimierung / DSGVO-Position | ✅ perfekt | ✅ solide | ⚠️ machbar, mehr Doku |
| Betreibbar von dir allein (H5) | ⚠️ nein, ehrlich nicht | ✅ ja | ✅ ja |
| Laufende Kosten | 0 € (nach 1,5–4 T€ invest) | ~5–30 €/M | ~10–40 €/M |
| Papierkram | keiner | 1× AVV je Firma | AVV + SCC je Firma |

### Empfehlung Teil 2 — und wann sie falsch ist

**Empfehlung: Weg 2, EU-Cloud mit AVV.** Begründung entlang deiner eigenen Prioritäten: Dein Constraint sagt, eine übersehene wichtige Mail ist teurer als alles andere — das disqualifiziert lokal (Qualitätsrisiko genau bei R1) UND es rechtfertigt zugleich den Datenabfluss sauber nach Art. 6: Die Verarbeitung dient der zuverlässigen Bearbeitung von Geschäftspost, mildere Mittel (Bordmittel, lokal) sind nachweislich ungeeignet — diese Abwägung haben wir mit Phase 1 schwarz auf weiß. EU-Cloud hält die Datenschutz-Doku schlank (kein Drittland) und den Betrieb bei dir machbar. Innerhalb von Weg 2 prüfen wir in Phase 3 zuerst **Azure OpenAI mit EU-Datenresidenz**, weil deine Daten dann im selben Microsoft-Vertragskosmos bleiben, in dem sie ohnehin liegen.

**Wann diese Empfehlung falsch ist:**
- Wenn dir nach dem Pilot die Erkennungsqualität bei Zwischentönen nicht reicht → Upgrade auf Weg 3 (US), der Wechsel ist dank austauschbarem Modell-Backend ein Konfigurations-, kein Umbauprojekt
- Wenn ein Großkunde/eine Behörde dir vertraglich „keine Cloud-KI" diktiert → Downgrade auf Weg 1 (lokal) für dieses Postfach, mit bewusst akzeptiertem Qualitätsverlust
- Wenn du doch jemanden für IT-Betrieb einstellst UND maximale Datenhoheit willst → Weg 1 wird realistisch

**Architektur-Prinzip (fest, egal wie du entscheidest):** Das KI-Modell ist ein **austauschbares Bauteil**. Briefing-Logik, Regelwerk, Guardrails, Kontaktkontext — alles bleibt gleich, nur der „Denk-Motor" ist per Einstellung wechselbar. Deine E1-Entscheidung ist damit revidierbar, kein Beton.

---

## Deine Entscheidung für Phase 3

Bitte wähle jetzt E1 final:
- **a) EU-Cloud mit AVV** ⭐ Empfehlung
- **b) US-Anbieter mit AVV** (beste Qualität, mehr Doku)
- **c) Nur lokal** (beste Datenposition, spürbar schwächere Erkennung, Hardware + Betrieb)

**→ Danach: Phase 3 — Detail-Design des Piloten (A+B auf durchgeplant.de): Kriterienkatalog aus deinen Beispielen, Briefing-Format, Guardrails gegen die vier Fehlermodi. Ergebnis: 04-design.md + Schaubild.**
