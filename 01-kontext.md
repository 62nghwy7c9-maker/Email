# 01-kontext.md — Phase 0 abgeschlossen (Stand 16.07.2026)

Verantwortliche Nutzerin: Kira Moewes — einzige Leserin/Beantworterin aller 4 Postfächer.

---

## 1. Infrastruktur (verifiziert über öffentliche DNS-/Verzeichnisdaten + Bestätigung)

| # | Postfach | Firma / Zweck | Rechtsform | Anbieter | Tenant-ID | Besonderheit |
|---|---|---|---|---|---|---|
| 1 | moewes@planvoller.de | Neubau / Sanierung | GmbH | Microsoft 365 | f9032dff-… | Hornetsecurity vorgeschaltet |
| 2 | hm@aim-wohnbau.de | Hausbau (andere Firmen) | GmbH | Microsoft 365 | 5be4e792-… | Hornetsecurity vorgeschaltet |
| 3 | hm@durchgeplant.de | Einzelperson | Einzelfirma | Microsoft 365 | ad2158ae-… | direkt |
| 4 | hm@burk-keller.de | Maklerbüro | GmbH | Microsoft 365 | 592d3aa8-… | direkt |

- **4 getrennte Tenants** (bestätigt: „alles einzeln") → 4 separate App-Registrierungen für den Agenten nötig.
- **Alle 4 = eigene Postfächer** mit eigenem Login. Keine Aliasse, keine Shared Mailboxes.
- **Admin-Zugriff: Kira selbst bei allen 4** → Graph-API-Einrichtung ohne Dritte möglich.
- Lesegeräte: Outlook PC (primär), iPhone teilweise (zentrale Ansicht, nur bei Eingang / vor Terminen).
- Antwortverhalten heute: immer von der korrekten Firmenadresse. **Kein** Ist-Problem mit Absender-Vermischung.

## 2. Volumen & Baseline

- **~50 Mails/Werktag** gesamt; **~70 % handlungsrelevant** (sehr hoher Nutzanteil, wenig klassisches Rauschen).
- Postfach-Checks: zu festen Zeiten, 1–15×/Tag, schwankend.
- **Durchgerutscht in 6 Monaten (= Baseline für Phase 4):**
  1. Kaufinteresse eines Kunden an Objekt nicht bemerkt → entgangenes Geschäft
  2. Kundennachfrage unbeantwortet
  3. Rechnungen in falschem Outlook-Ordner → auf iPhone nicht sichtbar → übersehen

## 3. Prioritätsdefinition (Rohmaterial für das Regelwerk in Phase 3)

**Grundcharakter: kunden-/umsatzgetrieben.** Höchstes Risiko = verpasster Interessent/unzufriedener Kunde, nicht primär Behördenfrist.

| Priorität | Definition |
|---|---|
| **Prio 1** | Kunden & Geschäftspartner — insbesondere: Bestandskunde mit Rückfrage/Problem im Bauablauf (Eskalationsgefahr) · Kaufinteressent in Verhandlung („Was kostet?", „wollen Vertrag machen") → braucht schnelle Antwort |
| **Prio 2** | Behörden, Finanzen, Rechtliches |
| **Unwichtig** | Werbung · Info-/CC-Mails — **aber: nicht verwerfen, sondern komprimiert zusammenfassen** (Recall-Schutz: falls doch etwas Wichtiges dabei ist) |

- **Signalwörter „sofort ansehen": alle** aus dem Katalog (Frist/Termin, Mahnung, Mangel/Schaden/Havarie, Nachtrag/Mehrkosten, Kündigung/Rücktritt/Anwalt, Abnahme/Übergabe).
- **Wiederkehrende Pflicht-Mails:** Rechnungen (monatlich/quartalsweise), BWA-Auswertungen (Monats-/Quartalsende) — Ausbleiben oder Übersehen ist ein Fehler.
- Konsequenz: Der Agent braucht **Kontaktkontext** (wer ist Kunde/Interessent, welche Firma, welches Projekt) — Absenderrolle schlägt Inhalt.

## 4. Datenschutz

- **E1 (Datenabfluss): noch NICHT entschieden.** Kira will zuerst eine Risiko-Gegenüberstellung (lokal vs. EU-Cloud+AVV vs. US+AVV) → **Pflichtbestandteil von Phase 2 (03-optionen.md)**. Architektur bis dahin so auslegen, dass alle drei Wege möglich bleiben (austauschbares Modell-Backend).
- Rechtsstruktur: 3× GmbH + 1× Einzelfirma = **4 Verantwortliche** → bei gemeinsamem System: AVV je Einheit bzw. Vereinbarung nach Art. 26 DSGVO (Standardformular). Mildernd: nur eine Person liest.
- Kein Datenschutzbeauftragter vorhanden (bei der Größe keine Pflicht).
- Keine Tabu-Inhalte: alles in den 4 Postfächern darf von der KI gelesen werden.

## 5. Ausgabe & Arbeitsweise (Soll)

- **Briefing:** 1×/Tag um **7:30 Uhr** als E-Mail an Kira selbst, **+ Excel-Anhang** (Übersicht/Liste). Zusätzlich **Sofort-Alarm** bei erkannten Fristen/Notfällen.
- **Todos:** kein bestehendes System, keine Präferenz („was am besten ist") → Empfehlung folgt in Phase 3 (Kandidat: Microsoft To Do — in M365 enthalten, synct aufs iPhone, keine neue Insel).
- **Kalender:** Outlook-Kalender vorhanden → Terminabgleich für spätere Entwurfsstufe möglich.
- **Anhänge/Fotos (Zusatzwunsch):** Fotos/Dateien aus Mails automatisch sortieren — **nur für das Pilot-Postfach durchgeplant.de**. Wird als eigene Ausbaustufe in die Roadmap (06) aufgenommen, nicht Teil des ersten Piloten.

## 6. Entwürfe (spätere Stufe)

- Ton: **kundenabhängig**, nicht firmenabhängig → Kontaktkontext muss Anredeform/Ton je Kontakt speichern.
- Signaturen: alle 4 vorhanden und gepflegt.
- **Niemals von der KI entwerfen:** alles mit Preisen / Angeboten / Nachträgen. (Weitere Tabu-Typen in Phase 3 vorschlagen — Kira hat nur diesen einen markiert; rechtswirksame Mails und Terminzusagen zur Bestätigung erneut vorlegen.)

## 7. Pilot & Rahmen

| Punkt | Entscheidung |
|---|---|
| **Pilot-Postfach** | **hm@durchgeplant.de** (Einzelfirma, direkter M365-Zugang, überschaubares Risiko) |
| Eval-Daten | ~100 alte Mails verfügbar, Labeling durch Kira ok (H1) |
| Budget | offen nach oben — „egal, wenn es nachweislich Zeit spart und nichts mehr durchrutscht" (H3) |
| Feedback | ~10 Min/Tag in den ersten 4 Wochen (H4) |
| Umsetzung | Kira selbst mit Anleitung (H5) — Anleitungen müssen non-technical formuliert sein |

## 8. Offene Punkte (nicht blockierend)

- A5 Domain-Registrar (unkritisch, bei Bedarf in der Umsetzung klären)
- E1-Entscheidung fällt nach Risikovergleich in Phase 2

---

**→ Nächster Schritt: Phase 1 — „Ordnung vor Intelligenz": Was lösen Microsoft-Bordmittel nativ, was bleibt als echtes Problem für einen Agenten übrig? (Ergebnis: 02-nativ-vs-rest.md)**
