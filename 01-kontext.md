# 01-kontext.md — ENTWURF (Stand 15.07.2026, Phase 0 zu ~60 % abgeschlossen)

## A. Gesichert: Infrastruktur (öffentliche Daten + Bestätigung durch Kira)

| Domain | Firma/Zweck | Anbieter | Tenant-ID | Besonderheit |
|---|---|---|---|---|
| planvoller.de | Neubau / Sanierung | Microsoft 365 | f9032dff-… | Hornetsecurity vorgeschaltet |
| aim-wohnbau.de | Hausbau (andere Firmen) | Microsoft 365 | 5be4e792-… | Hornetsecurity vorgeschaltet |
| durchgeplant.de | Einzelperson | Microsoft 365 | ad2158ae-… | direkt |
| burk-keller.de | Maklerbüro | Microsoft 365 | 592d3aa8-… | direkt |

- **4 getrennte Tenants**, von Kira bestätigt („alles einzeln") → Agent braucht 4 separate App-Registrierungen / Read-only-Berechtigungen.
- **Admin-Zugriff: Kira selbst, bei allen 4** (A3) → kein IT-Dienstleister nötig für die Einrichtung; Graph-API-Weg ist frei.
- Alle 4 Adressen sind **eigene Postfächer** mit eigenem Login (B1).
- **Nur Kira** liest und beantwortet alle 4 (B2) → keine Mitleser, vereinfacht Datenschutz erheblich.
- Antworten erfolgen heute **immer von der richtigen Firmenadresse** (B3) → das Vermischungsrisiko liegt v.a. in der Zukunft (Entwurfs-Phase), nicht im Ist.

## B. Gesichert: Arbeitsweise & Volumen

- **~50 Mails/Werktag** über alle 4 (C1); **~70 % brauchen eine Handlung** (C2) — ungewöhnlich hoher Nutzanteil, wenig klassisches Rauschen.
- Lesegeräte (A4): **Outlook auf dem PC** + **teilweise iPhone** („schaut über Apple zentral — nur wenn etwas ankommt oder vor Terminen").
- Frequenz (C3): zu festen Zeiten, **1–15× pro Tag**, schwankend.
- **Durchgerutscht in 6 Monaten (C4) — die Baseline:**
  1. Kaufinteresse eines Kunden an einem Objekt **nicht bemerkt** (entgangenes Geschäft!)
  2. Kundennachfrage unbeantwortet
  3. **Rechnungen** in falschen Outlook-Ordner einsortiert → auf dem iPhone nicht angezeigt → übersehen

## C. Gesichert: Was „wichtig" heißt (erste Hälfte)

Wichtig ist bei Kira **kunden-/umsatzgetrieben** (nicht primär fristen-getrieben wie zunächst angenommen):

1. **Bestandskunde mit Rückfrage/Problem im Bauablauf** — Eskalationsgefahr, unzufriedener Kunde (D1)
2. **Kaufinteressent in Verhandlung** („Was kostet?", „Wir möchten Vertrag machen") — braucht **schnelle Antwort**, sonst entgeht das Geschäft (D1)
3. **Behörden: immer wichtig** (D3)
4. **Kunden mit Fragen / Problem / Vertragsabschluss: immer wichtig** (D3)

→ Konsequenz für Phase 3: Priorisierung muss **Absenderklasse Kunde/Interessent erkennen** (Kontaktkontext!), nicht nur Fristen/Signalwörter.

## D. OFFEN — blockiert den Abschluss von Phase 0

| # | Frage | Status |
|---|---|---|
| **E1** | Datenabfluss: lokal / EU-Cloud+AVV / US+AVV | **KRITISCH — blockiert Architektur (Phase 2)** |
| **D2** | 5 Beispiele unwichtiger Mails | **KRITISCH — ohne Negativbeispiele kein Regelwerk** |
| **E2** | Rechtsformen der 4 Firmen | wichtig (AVV-Konstrukt) |
| D4/D5 | Signalwörter, typische Fristen | Vorschlag wird vorgelegt |
| E3/E4 | Datenschutzberater, Tabu-Inhalte | offen |
| F1–F4 | Briefing-Kanal/-Zeit, Todo-Ziel, Kalender | Vorschlag wird vorgelegt |
| G1–G3 | Ton je Firma, Signaturen, Niemals-Entwurf-Typen | Vorschlag wird vorgelegt |
| H1–H5 | 100 Test-Mails, Pilot-Postfach, Budget, Feedback-Zeit, Umsetzer | offen |
| A5 | Domain-Registrar | unkritisch, keine Eile |
