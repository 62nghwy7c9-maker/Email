# Fragebogen: E-Mail-Triage für 4 Postfächer (v2)

**Teil 1** = bereits ermittelte Daten (bitte gegenprüfen) · **Teil 2** = offene Fragen.
**So funktioniert's:** Kreuze an, indem du `[ ]` durch `[x]` ersetzt, und fülle die Freitextfelder aus.
Wenn du etwas nicht weißt: Kreuze „Weiß ich nicht" an — bei jeder Frage steht, wie du es herausfinden kannst (oder ich helfe dir dabei).
**Wenn Teil 2 ausgefüllt ist, kann ich direkt mit der Planung beginnen (Phase 1–3), ohne weitere Rückfragen.**

---

# TEIL 1 — Bereits ermittelt (bitte gegenprüfen)

*Quelle: ausschließlich öffentliche Verzeichnisse (MX-, Autodiscover-, SPF-Einträge und Microsofts Verzeichnisdienst). Kein Login, keine Mail-Inhalte. Die reinen Daten stehen in `Code-Markierung` — in der PDF-Version gelb hervorgehoben.*

## ✔ A1 beantwortet: Der E-Mail-Anbieter

| Domain | Anbieter | Besonderheit |
|---|---|---|
| planvoller.de | `Microsoft 365` | `Hornetsecurity` vorgeschaltet |
| aim-wohnbau.de | `Microsoft 365` | `Hornetsecurity` vorgeschaltet |
| durchgeplant.de | `Microsoft 365` | direkt, ohne Vorfilter |
| burk-keller.de | `Microsoft 365` | direkt, ohne Vorfilter |

*(Warum wichtig: Microsoft 365 heißt, der sichere Programm-Zugang **Graph-API** ist bei allen 4 verfügbar. Graph-API = Microsofts offizieller Zugang für Programme, bei dem sich Rechte exakt festlegen lassen — z.B. „darf nur lesen, niemals senden". Deine Regel „KI sendet niemals Mails" wird damit technisch erzwungen, nicht nur versprochen. Konsequenz: beste Ausgangslage.)*

*(Was ist Hornetsecurity: ein deutscher Sicherheits-Dienst, der eingehende Post **vor** Microsoft prüft — ein Pförtner, der Spam/Viren abfängt. Konsequenz: gut für Sicherheit, für unser Projekt neutral. Indiz: So etwas richtet üblicherweise ein **IT-Dienstleister** ein → relevant für A3 und H5.)*

## ✔ A2 beantwortet: 4 getrennte Microsoft-Verbünde („Tenants")

| Domain | Verbund-Nummer (Tenant-ID) |
|---|---|
| planvoller.de | `f9032dff-94c4-43b2-8ab8-6d33a9c28555` |
| aim-wohnbau.de | `5be4e792-3805-4a49-a71e-9dd6384e2056` |
| durchgeplant.de | `ad2158ae-c05f-4db1-894a-49eae5718ce9` |
| burk-keller.de | `592d3aa8-2229-4e1f-abcc-a923147ed9e9` |

*(Was ist ein Tenant: Microsofts Cloud ist ein Bürohochhaus; jede Firma mietet eine abgeschlossene Etage — den „Tenant". Alle 4 Nummern sind **verschieden** → deine Firmen wohnen auf **4 verschiedenen Etagen**, ohne Verbindungstür.)*

*(Konsequenz 1: Der KI-Assistent braucht **4 separate „Schlüsselkarten"** — Nur-Lesen-Zugang je Firma einzeln einrichten. Machbar, aber 4× Aufwand. Konsequenz 2: Datenschutzrechtlich ist die Trennung sogar sauberer. Ob man zusammenlegt → Phase 1.)*

### Bitte gegenprüfen — passt das zu deinem Alltag?

Musst du dich für jede Firma separat anmelden bzw. in Outlook zwischen 4 Konten wechseln?
- [ ] Ja, stimmt *(→ 4 Tenants korrekt ermittelt)*
- [ ] Nein, ich sehe alles mit einem Login *(→ bitte melden!)*

---

# TEIL 2 — Offene Fragen

Die 4 Postfächer:

| # | Adresse | Firma/Zweck |
|---|---------|-------------|
| 1 | moewes@planvoller.de | Neubau/Sanierung |
| 2 | hm@aim-wohnbau.de | |
| 3 | hm@durchgeplant.de | Einzelperson |
| 4 | hm@burk-keller.de | |

*(Bitte die leeren Zellen kurz ergänzen: Was macht die Firma?)*

---

## Block A — Technik: Restfragen

*A1 + A2 sind bereits beantwortet (siehe Teil 1) — es bleiben A3 bis A5.*

### A3. Wer hat Admin-Zugriff auf die 4 Microsoft-365-Verbünde?

*Gemeint ist: Wer kann Einstellungen für die ganze Firma ändern — Postfächer anlegen, Rechte vergeben? Nötig, um dem KI-Assistenten die fein abgestuften „Nur-Lesen"-Rechte einzurichten — bei euch 4×, einmal je Verbund. Vermutung aus Teil 1: Der Hornetsecurity-Filter wurde wahrscheinlich von einem IT-Dienstleister eingerichtet — wer betreut eure IT?*

- [ ] Ich selbst (bei allen 4)
- [ ] Mein IT-Dienstleister (Name/Firma: ______________)
- [ ] Unterschiedlich je Firma: ______________
- [ ] Weiß ich nicht

### A4. Womit liest du heute deine Mails? (Mehrfachauswahl)

- [ ] Outlook-Programm auf dem PC (installiert)
- [ ] Outlook im Browser
- [ ] Outlook-App auf dem Handy
- [ ] Apple Mail / anderes Mailprogramm: ______________
- [ ] Webmail des Anbieters (z.B. IONOS-Webmail, GMX-Website)

### A5. Bei wem sind die 4 Domains (die Namen nach dem @) registriert?

*So findest du es heraus: Wer schickt dir die Jahresrechnung für „planvoller.de" usw.? Die Mails laufen bei Microsoft (Teil 1) — der Domain-NAME kann trotzdem woanders gemietet sein (IONOS, Strato …). Nur fürs Gesamtbild wichtig, keine Eile.*

- [ ] Direkt bei Microsoft
- [ ] Anderer: ______________
- [ ] Unterschiedlich pro Domain: ______________
- [ ] Weiß ich nicht

---

## Block B — Die 4 Adressen: Was sind sie technisch?

### B1. Sind die 4 Adressen eigene Postfächer, oder landen manche im selben Briefkasten?

*So findest du es heraus: Hat jede Adresse ein eigenes Passwort/Login? Dann eigene Postfächer. Kommen Mails an zwei Adressen im selben Posteingang an? Dann ist eine davon ein Alias (zweites Namensschild am selben Briefkasten).*

| Adresse | Eigenes Postfach (eigener Login) | Alias (läuft in anderes Postfach) | Geteiltes Postfach (mehrere Leute) | Weiß nicht |
|---|:---:|:---:|:---:|:---:|
| moewes@planvoller.de | [ ] | [ ] | [ ] | [ ] |
| hm@aim-wohnbau.de | [ ] | [ ] | [ ] | [ ] |
| hm@durchgeplant.de | [ ] | [ ] | [ ] | [ ] |
| hm@burk-keller.de | [ ] | [ ] | [ ] | [ ] |

### B2. Wer außer dir liest oder beantwortet Mails in diesen Postfächern?

- [ ] Niemand — nur ich, bei allen 4
- [ ] Andere Personen, und zwar:

| Adresse | Wer noch? (Name/Rolle) |
|---|---|
| | |
| | |

### B3. Von welcher Adresse aus antwortest du heute — sauber getrennt oder vermischt?

- [ ] Ich antworte immer von der Adresse, an die die Mail ging
- [ ] Ehrlich: Es passiert, dass ich von der „falschen" Firma antworte
- [ ] Ich antworte fast alles von einer Hauptadresse: ______________

---

## Block C — Volumen & Alltag

### C1. Wie viele Mails kommen pro Werktag über alle 4 Adressen zusammen an? (grobe Schätzung)

- [ ] Unter 20
- [ ] 20–50
- [ ] 50–100
- [ ] 100–200
- [ ] Über 200

### C2. Wie viele davon brauchen wirklich eine Handlung von dir (Antwort, Entscheidung, Termin, Frist)?

- [ ] Fast alle (über 70 %)
- [ ] Etwa die Hälfte
- [ ] Etwa ein Viertel
- [ ] Nur wenige (unter 10 %)

### C3. Wie oft schaust du heute in die Postfächer?

- [ ] Ständig, den ganzen Tag nebenbei
- [ ] Zu festen Zeiten (morgens/mittags/abends)
- [ ] Unregelmäßig — manchmal Tage nicht (bei einzelnen Postfächern)

### C4. Was ist dir in den letzten 6 Monaten konkret durchgerutscht? (1–3 echte Beispiele)

*Das ist Gold wert — daran messen wir später, ob das System besser ist als der Status quo.*

1. ______________________________________________________________
2. ______________________________________________________________
3. ______________________________________________________________

---

## Block D — Was heißt „wichtig"? (Das Herzstück)

*Aus diesen 10 Beispielen baue ich das Regelwerk für die Priorisierung. Bitte echte Fälle, gern anonymisiert („Bauherr X", „Bauamt Y"). Je konkreter, desto besser wird die Sortierung.*

### D1. Fünf echte Beispiele für WICHTIGE Mails

*Pro Beispiel: Wer war der Absender (Rolle reicht: Bauherr, Bauamt, Handwerker, Anwalt…)? Worum ging es? Warum war es wichtig (Frist? Geld? Rechtsfolge? Baustillstand?)*

| # | Absender(-rolle) | Worum ging es? | Warum wichtig? |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

### D2. Fünf echte Beispiele für UNWICHTIGE Mails

| # | Absender(-rolle) | Worum ging es? | Warum unwichtig? |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

### D3. Welche Absender-Rollen sind bei dir IMMER wichtig, egal was drinsteht? (Mehrfachauswahl + Ergänzung)

- [ ] Behörden (Bauamt, Finanzamt, Gericht, …)
- [ ] Bauherren / Auftraggeber in laufenden Projekten
- [ ] Banken / Finanzierung
- [ ] Anwälte / Notare
- [ ] Versicherungen (Schadensfälle)
- [ ] Bestimmte einzelne Personen: ______________
- [ ] Weitere: ______________

### D4. Welche Signalwörter/Themen bedeuten bei dir „sofort ansehen"?

*Beispiele zum Ankreuzen/Ergänzen:*

- [ ] Frist / Termin / „bis zum …"
- [ ] Mahnung / Zahlungserinnerung
- [ ] Mangel / Schaden / Havarie auf der Baustelle
- [ ] Nachtrag / Mehrkosten
- [ ] Kündigung / Rücktritt / Anwalt eingeschaltet
- [ ] Abnahme / Übergabe
- [ ] Weitere: ______________

### D5. Gibt es wiederkehrende Fristen-Typen in deinem Geschäft, die die KI kennen muss?

*z.B. Widerspruchsfristen bei Bescheiden (1 Monat), Skonto-Fristen, Gewährleistungsfristen, Angebotsbindefristen…*

______________________________________________________________
______________________________________________________________

---

## Block E — Datenschutz: Die Grundsatzentscheidung

### E1. Wie weit dürfen Mail-Inhalte dein Haus verlassen? (Bitte GENAU EINE Option)

*Zur Einordnung — das ist die Entscheidung mit den größten Folgen:*

| Option | Qualität der KI | Kosten | Aufwand |
|---|---|---|---|
| Nur lokal (eigener Rechner) | Deutlich schwächer — „fleißiger Praktikant" | Hardware einmalig ~1.500–4.000 € | Hoch |
| EU-Cloud mit Vertrag (AVV) | Gut | ~20–100 €/Monat | Mittel |
| US-Anbieter (z.B. Anthropic/Claude) mit AVV + EU-Datenschutzklauseln | Sehr gut | ~20–100 €/Monat | Mittel |

- [ ] **Nur lokal** — kein Byte Mailinhalt verlässt meine Hardware
- [ ] **EU-Cloud mit AVV** ist akzeptabel
- [ ] **Auch US-Anbieter mit AVV** (Standardvertragsklauseln) ist akzeptabel
- [ ] Unsicher — ich will erst eine Risiko-Gegenüberstellung sehen

### E2. Sind die 4 Firmen rechtlich getrennte Unternehmen?

*Warum das zählt: Wenn ja, braucht formal jede Firma ihre eigene Datenschutz-Regelung, und ein gemeinsames KI-System über alle 4 braucht eine kleine Zusatzvereinbarung zwischen den Firmen (Standardformular, kein Drama — aber Pflicht).*

| Adresse | Rechtsform (GmbH, Einzelunternehmen, GbR, …) | Du bist: Inhaber / Geschäftsführer / Angestellter |
|---|---|---|
| planvoller.de | | |
| aim-wohnbau.de | | |
| durchgeplant.de | | |
| burk-keller.de | | |

### E3. Hast du bereits einen Datenschutzbeauftragten oder Datenschutz-Berater?

- [ ] Ja: ______________
- [ ] Nein
- [ ] Nicht nötig (unter 20 Beschäftigte mit Datenverarbeitung, keine Pflicht)

### E4. Gibt es Mail-Inhalte, die die KI NIEMALS sehen darf?

*z.B. Personalunterlagen, Gehälter, laufende Rechtsstreitigkeiten, private Mails im Firmenpostfach*

- [ ] Nein, alles in den 4 Postfächern darf gelesen werden
- [ ] Ja, und zwar: ______________________________________________

---

## Block F — Ausgabe: Wie soll das Ergebnis zu dir kommen?

### F1. Wie möchtest du das tägliche Briefing (die Übersicht) bekommen?

- [ ] Als E-Mail an mich selbst (empfohlen für den Start — keine neue App)
- [ ] Als Datei/Seite, die ich morgens öffne
- [ ] Per Messenger (WhatsApp/Signal/Teams): ______________
- [ ] Egal, Hauptsache übersichtlich

### F2. Wann und wie oft?

- [ ] 1× morgens (Uhrzeit: ______)
- [ ] 2× täglich (morgens + mittags/nachmittags)
- [ ] Zusätzlich Sofort-Alarm bei erkannten Fristen/Notfällen: [ ] ja [ ] nein

### F3. Wo sollen erkannte Aufgaben (Todos) landen? — Keine neue Insel!

*Wo pflegst du HEUTE deine Aufgaben?*

- [ ] Microsoft To Do / Outlook-Aufgaben
- [ ] Papier / Notizbuch
- [ ] Excel / eigene Liste
- [ ] Anderes Tool: ______________
- [ ] Nirgends systematisch — im Kopf / im Posteingang

**Wunsch:** Todos sollen erscheinen in: ______________

### F4. Führst du deine Termine in einem digitalen Kalender?

*Wichtig für später: Antwort-Entwürfe mit Terminvorschlägen darf die KI nur mit Kalenderabgleich — sonst gar nicht.*

- [ ] Ja, Outlook-Kalender
- [ ] Ja, anderer: ______________
- [ ] Teils digital, teils Papier
- [ ] Nein

---

## Block G — Antworten & Entwürfe (spätere Ausbaustufe)

### G1. Unterscheiden sich Ton/Anrede zwischen den 4 Firmen?

- [ ] Nein, ich schreibe überall gleich
- [ ] Ja: (kurz je Firma, z.B. „förmlich", „locker", „Du/Sie")

| Firma | Ton (förmlich/neutral/locker) | Du oder Sie? |
|---|---|---|
| planvoller.de | | |
| aim-wohnbau.de | | |
| durchgeplant.de | | |
| burk-keller.de | | |

### G2. Hat jede Firma eine eigene E-Mail-Signatur?

- [ ] Ja, alle 4 vorhanden und gepflegt
- [ ] Teilweise
- [ ] Nein / veraltet

### G3. Welche Mail-Typen dürfen NIEMALS von der KI vorentworfen werden, sondern gehören immer komplett in deine Hand?

*Vorschlag (bitte ergänzen/streichen):*

- [ ] Alles mit Preisen / Angeboten / Nachträgen
- [ ] Alles mit rechtlicher Wirkung (Kündigung, Mängelrüge, Fristsetzung)
- [ ] Alles an Behörden
- [ ] Zusagen von Terminen
- [ ] Weitere: ______________

---

## Block H — Test, Budget, Start

### H1. Kommst du an ~100 alte, bereits bearbeitete Mails für einen Test heran?

*Damit prüfen wir VOR dem Echtbetrieb: Hätte die KI die wichtigen erkannt? Du labelst sie einmal von Hand (wichtig/unwichtig), das dauert ca. 1–2 Stunden.*

- [ ] Ja, kein Problem
- [ ] Ja, aber Zeit fürs Durchgehen ist knapp
- [ ] Schwierig, weil: ______________

### H2. Mit welchem Postfach sollen wir den Piloten starten?

*Empfehlung: das mit dem meisten Schmerz, aber überschaubarem Risiko.*

- [ ] moewes@planvoller.de
- [ ] hm@aim-wohnbau.de
- [ ] hm@durchgeplant.de
- [ ] hm@burk-keller.de
- [ ] Deine Empfehlung, weil dort am meisten durchrutscht: ______________

### H3. Laufende Kosten: Was ist der Rahmen für das Gesamtsystem (KI + ggf. Software)?

- [ ] Bis 20 €/Monat
- [ ] Bis 50 €/Monat
- [ ] Bis 150 €/Monat
- [ ] Egal, wenn es nachweislich Zeit spart und nichts mehr durchrutscht

### H4. Wie viel eigene Zeit kannst du in den ersten 4 Wochen für Feedback investieren?

*Das System wird nur gut, wenn du ihm anfangs sagst, was es falsch einsortiert hat.*

- [ ] ~10 Min/Tag
- [ ] ~30 Min/Woche
- [ ] Einmalig beim Start, danach soll es laufen

### H5. Wer setzt das technisch um?

- [ ] Ich selbst mit Anleitung (traue ich mir zu)
- [ ] Mein IT-Dienstleister
- [ ] Suche ich noch / brauche Empfehlung, worauf zu achten ist

---

## Fertig?

Kurzer Selbst-Check — diese fünf sind die kritischen:

- [ ] Teil 1 gegengeprüft (4 separate Logins — ja/nein?)
- [ ] B1 (Postfach/Alias) ausgefüllt — notfalls mit „weiß nicht"
- [ ] D1 + D2 (10 Beispiele) vollständig — **ohne die geht es nicht**
- [ ] E1 (Datenabfluss) entschieden
- [ ] E2 (Rechtsform) ausgefüllt

Dann zurück an mich. Ich erstelle daraus `01-kontext.md` und starte direkt mit Phase 1 (Was löst Microsoft/dein Anbieter nativ?) bis Phase 3 (Design) — ohne weitere Rückfragen, außer deine Antworten widersprechen sich.
