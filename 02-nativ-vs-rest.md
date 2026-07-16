# 02-nativ-vs-rest.md — Phase 1: Ordnung vor Intelligenz (Stand 16.07.2026)

**Prinzip:** Bevor irgendein KI-Modell auftaucht, wird ausgeschöpft, was Microsoft 365 mit Bordmitteln kann.
Nur was danach übrig bleibt, darf ein Agent bekommen.

---

## Teil A — Was Microsoft nativ löst

### A1. Postfachbündelung: „4 Postfächer, eine Ansicht" ist ein 30-Minuten-Job — OHNE Adminarbeit

Deine Lage (4 eigene Postfächer in 4 getrennten Tenants) klingt kompliziert, ist aber für die *Leseansicht* trivial:

| Weg | Was es ist | Bewertung für dich |
|---|---|---|
| **Alle 4 Konten in der Outlook-App (iPhone)** | Die Outlook-App fürs Handy hat einen **„Alle Konten"-Posteingang**: EINE Liste, alle 4 Postfächer chronologisch vermischt | ✅ **Empfohlen — der einzige echte native Überblick.** Ersetzt Apple Mail; wichtig auch wegen Fehlerfall Nr. 3 (s.u.) |
| **Alle 4 Konten in einem Outlook (PC)** | Outlook am PC zeigt alle Konten *nebeneinander* (4 Posteingänge in der linken Spalte). **Ehrlich: eine verschmolzene Einzelliste wie auf dem Handy gibt es am PC nicht zuverlässig.** Bester Trick: alle 4 Posteingänge per Rechtsklick zu den **Favoriten** pinnen → gestapelt ganz oben, 4 Klicks statt 4 Logins | ⚠️ **Milderung, kein Überblick.** Der echte PC-Gesamtüberblick bleibt Rest-Problem → wird das Briefing des Agenten (R2) |
| Shared Mailbox („geteiltes Postfach") | Ein gemeinsames Postfach, in das alle Mails fließen | ❌ Geht nicht über Tenant-Grenzen hinweg; bei dir irrelevant, da nur du liest |
| Weiterleitung alles in 1 Postfach | Alle Mails automatisch in ein Hauptpostfach kopieren | ❌ Zerstört die saubere Firmen-Trennung beim Antworten; Datenschutz-Vermischung. Nicht tun |
| Tenants zusammenlegen | Alle 4 Firmen in einen Microsoft-Verbund migrieren | ❌ Großprojekt, rechtlich heikel (4 Verantwortliche), Nutzen gering. Nicht tun |

**Fazit Bündelung:** Kein Adminprojekt nötig, saubere Trennung bleibt. Aber differenziert: **Handy = echter Überblick nativ** („Alle Konten"-Liste), **PC = nur Milderung** (Favoriten-Stapel). Der priorisierte Gesamtüberblick am PC — alle 4 Konten in EINER nach Wichtigkeit sortierten Sicht — ist nativ nicht zu haben und wandert als Kernauftrag ins Briefing des Agenten (R2).

### A2. Dein Fehlerfall Nr. 3 (übersehene Rechnungen) ist ein reiner Regel-Fix — keine KI nötig

Diagnose: Eine **Outlook-Regel** (oder der Hornetsecurity-Filter) sortiert Rechnungen in einen Unterordner. Apple Mail auf dem iPhone zeigt dir nur den Posteingang prominent → Unterordner = unsichtbar = übersehen.

Der Fix (je betroffenes Konto, ~10 Minuten):
1. Outlook im Browser öffnen → Zahnrad → **Regeln** → jede Regel prüfen: Was wird wohin verschoben?
2. Grundsatz umstellen: **Verschieben ersetzen durch Kategorisieren.** Eine **Kategorie** ist ein farbiges Etikett — die Mail bleibt im Posteingang sichtbar, ist aber markiert (z.B. 🔵 „Rechnung"). Ordner verstecken, Kategorien markieren.
3. Outlook-App auf dem iPhone statt Apple Mail nutzen (A1) — dann siehst du dieselbe Welt wie am PC.

### A3. Fokussierter Posteingang: für dich ein RISIKO, kein Feature

Der „Fokussierte Posteingang" ist Microsofts eingebaute Mini-KI: Sie teilt den Posteingang in „Wichtig" und „Sonstige" — nach undurchschaubaren Kriterien, ohne dein Regelwerk, ohne Rechenschaft.

Das ist **genau dein Constraint-Verstoß**: eine falsch einsortierte Interessenten-Mail landet lautlos unter „Sonstige". **Empfehlung: ausschalten** (in Outlook: Ansicht → „Fokussierten Posteingang anzeigen" deaktivieren). Priorisierung machen wir später explizit und nachvollziehbar — nicht als Blackbox.

### A4. Was Bordmittel für deine Prioritäten leisten (und wo sie enden)

| Werkzeug | Was es kann | Grenze |
|---|---|---|
| **Regeln** („Wenn Absender X → Kategorie Y") | Bekannte Absender zuverlässig markieren: Bauamt, Bank, Steuerberater, Stammkunden | Kennt nur, was du einträgst. **Ein neuer Interessent ist per Definition unbekannt** → Regel greift nie |
| **Kategorien** (farbige Etiketten) | Einheitliches Farbsystem über alle 4 Konten: z.B. 🔴 Kunde/Eskalation, 🟢 Interessent, 🔵 Rechnung/Finanzen, 🟣 Behörde | Muss von Regeln oder Hand gesetzt werden — versteht keinen Inhalt |
| **Benachrichtigungs-Favoriten** (Handy) | Sofort-Push nur für ausgewählte Personen (deine Top-Kunden), Rest still | Wieder: nur bekannte Absender |
| **QuickSteps** („aufgezeichnete Regeln") | Ein Klick = Mail kategorisieren + verschieben + weiterleiten. Gut für deine Handgriffe | Löst nichts automatisch aus |
| **Kennzeichnen/Nachverfolgung + To Do** | Mail anflaggen → erscheint automatisch in **Microsoft To Do** auf PC und iPhone. Deine Todo-Frage (F3) ist damit nativ beantwortet: **To Do, keine neue Insel** | Flag setzt du selbst; kein Kontext, keine Frist aus dem Mailtext |
| **Absender-Identität** | Bei 4 getrennten Konten antwortet Outlook **automatisch von der Adresse, an die die Mail ging** — dein sauberes Ist-Verhalten bleibt technisch garantiert | — |
| **Suchordner / Alle-Konten-Ansicht** | Gespeicherte Suchen wie „alle ungelesenen mit Kategorie Rot über alle Konten" | Nur Anzeige, keine Bewertung |

### A5. Quick-Wins — sofort umsetzbar, bevor irgendein Agent existiert (~1–2 Stunden einmalig)

1. **Outlook-App aufs iPhone**, alle 4 Konten rein, „Alle Konten"-Posteingang nutzen; Apple Mail für Firmenmails in Rente schicken
2. **Regeln-Inventur** in allen 4 Konten: Verschiebe-Regeln → Kategorie-Regeln (Fix für Fehlerfall Nr. 3)
3. **Fokussierten Posteingang ausschalten** (alle Konten, PC + App)
4. **Ein Kategorien-Farbsystem** in allen 4 Konten identisch anlegen (🔴🟢🔵🟣 wie oben)
5. **Regeln für die immer-wichtigen bekannten Absender**: Bauamt, Banken, Steuerberater, Top-Kunden → Kategorie + ggf. Handy-Push
6. **Flag→To Do** einmal ausprobieren: Mail anflaggen, in To Do wiederfinden

**Erwarteter Effekt:** Fehlerfall Nr. 3 (Rechnungen) ist damit vollständig gelöst. Die Fälle Nr. 1 und 2 (übersehener Interessent, unbeantwortete Kundenfrage) werden *gemildert* (eine Übersicht statt vier, weniger Verstecke) — aber **nicht gelöst**, denn kein Bordmittel erkennt, *dass* eine Mail ein Kaufsignal oder eine Eskalation enthält.

---

## Teil B — Was als echtes Problem übrig bleibt (NUR das bekommt der Agent)

| # | Rest-Problem | Warum Bordmittel scheitern |
|---|---|---|
| **R1** | **Unbekannte/neue Absender einordnen:** Ist das ein Interessent mit Kaufsignal? Ein Bestandskunde mit Eskalation? | Regeln kennen nur eingetragene Absender; Kaufsignale („Was kostet…?", „Vertrag unterschreiben") und Eskalationston stehen im *Inhalt* — den liest kein Bordmittel |
| **R2** | **Der Gesamtüberblick = tägliches Briefing 7:30 Uhr** über alle 4 Konten: je Mail 1 Satz Kern, Frist, nächster Schritt; gegliedert nach Handlungsbedarf heute / Woche / FYI / Rauschen (+ Excel). **Das ist die Antwort auf „alle Postfächer einzeln, kein Überblick"** — nativ gibt es diese verschmolzene, nach Wichtigkeit sortierte Sicht am PC nicht | Existiert nativ schlicht nicht (PC: nur Favoriten-Stapel; Handy: Liste ohne Priorisierung) |
| **R3** | **Zusammenfassung statt Löschung** von Werbung/CC-Mails (dein Recall-Schutz) | Regeln können nur verschieben/löschen, nicht komprimieren |
| **R4** | **Fristen aus Mailtext ziehen** („bis zum 24.07.") und in Briefing/Alarm heben | Kein Bordmittel liest Fließtext |
| **R5** | **Todos mit Kontext erzeugen** („Rückruf Familie X wegen Nachtrag, bis Fr") in To Do | Flag→To Do überträgt nur die Mail, versteht sie nicht |
| **R6** | **Kontaktkontext pflegen:** Wer ist das, welche Firma, welches Projekt, letzter Stand | Kein natives Gedächtnis über Konten hinweg |
| **R7** | **Wiederkehr-Überwachung:** Rechnung/BWA zum Monats-/Quartalsende ausgeblieben oder unbearbeitet → Hinweis | Regeln reagieren auf Mails, die *ankommen* — nicht auf solche, die *fehlen* |
| **R8** | *(Ausbaustufe)* Antwortentwürfe im kundenabhängigen Ton | — |
| **R9** | *(Ausbaustufe, nur durchgeplant.de)* Anhänge/Fotos automatisch in Projektordner sortieren | Regeln können Anhänge nicht nach Projekt zuordnen |

**Kernbefund:** Dein eigentliches Problem ist nicht Unordnung, sondern **semantische Erkennung** (R1) plus **Verdichtung** (R2/R3). Beides sind genuine KI-Aufgaben — hier ist ein Agent gerechtfertigt, vorher nicht.

---

**→ Nächster Schritt: Phase 2 — Architektur-Optionen (A/B/C/D) inkl. des zugesagten Risikovergleichs lokal vs. EU-Cloud vs. US-Anbieter für deine E1-Entscheidung. Ergebnis: 03-optionen.md**
