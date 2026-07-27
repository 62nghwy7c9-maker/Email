# Pilot einrichten — deine 3 Handgriffe

Alles andere ist fertig gebaut. Diese drei Dinge kann nur jemand mit deinen Zugängen tun.
Gesamtdauer: etwa 30 Minuten, einmalig.

---

## ① Der KI „Leserechte" geben (App-Registrierung, ~15 Min)

*Was das ist: Du legst im Microsoft-Konto von durchgeplant.de eine „Schlüsselkarte" für das Programm an. Sie erlaubt nur Lesen + Kategorien — Senden ist technisch ausgeschlossen.*

1. Browser: **portal.azure.com** → mit dem durchgeplant-Admin-Konto anmelden
2. Suchfeld oben: **„App-Registrierungen"** → **„Neue Registrierung"**
3. Name: `E-Mail-Triage-Pilot` · Kontotyp: **„Nur Konten in diesem Organisationsverzeichnis"** · Registrieren
4. Auf der Übersichtsseite zwei Werte kopieren (für Schritt ③):
   - **Anwendungs-ID (Client)**
   - **Verzeichnis-ID (Mandant)**
5. Links **„Authentifizierung"** → „Einstellung hinzufügen": **„Mobile Geräte- und Desktopanwendungen"** aktivieren → unten bei „Erweiterte Einstellungen" **„Öffentliche Clientflows zulassen" = Ja** → Speichern
6. Links **„API-Berechtigungen"** → „Berechtigung hinzufügen" → **Microsoft Graph** → **Delegierte Berechtigungen** → `Mail.ReadWrite` ankreuzen → Hinzufügen
   *(Bewusst NICHT: Mail.Send — das ist unsere Sicherheitsgarantie.)*

## ② AVV beim KI-Anbieter abschließen (~10 Min)

- Konto beim gewählten EU-Anbieter anlegen (Empfehlung aus 03-optionen: EU-Datenresidenz).
- Im Kundenbereich den **Auftragsverarbeitungsvertrag (AVV/DPA)** akzeptieren — Standard-Klickstrecke.
- **API-Schlüssel** erzeugen und kopieren (für Schritt ③).

## ③ Konfigurieren und starten (~5 Min)

1. Auf deinem PC: den Ordner `pilot/` aus dem Projekt herunterladen
2. `config-beispiel.json` kopieren zu **`config.json`** und die 4 Werte eintragen (IDs aus ①, Schlüssel aus ②)
3. Einmalig im Terminal/Eingabeaufforderung:
   ```
   pip install msal requests openpyxl
   ```
4. Start:
   ```
   python triage.py
   ```
   Beim ersten Lauf zeigt das Programm einen **Code + Link** — Link öffnen, Code eingeben, mit hm@durchgeplant.de anmelden. Danach nie wieder nötig.

**Ergebnis jedes Laufs:** Kategorien an den neuen Mails + **Briefing als Entwurf** im Entwürfe-Ordner (Mail + Excel-Anhang). Es wird nichts gesendet.

## Täglich 7:30? — Aufgabenplanung (optional, ~5 Min)

Windows: Startmenü → **„Aufgabenplanung"** → „Einfache Aufgabe erstellen" → täglich 07:25 → Programm: `python`, Argument: voller Pfad zu `triage.py`. Fertig.

---

## Sicherheits-Zusammenfassung (für dich und Papa)

- Berechtigung nur **Mail.ReadWrite** — kein Senden möglich, egal was passiert
- Briefing = **Entwurf**, kein Versand; nichts wird gelöscht oder verschoben
- Mailinhalt gilt für die KI als Daten, nie als Befehl (im Test mit echter Phishing-Mail bestätigt)
- KI-Aufruf: nur Mailtext, keine Anhänge; EU-Anbieter mit AVV
- Jederzeit abschaltbar: geplante Aufgabe löschen — fertig. Rückstände: nur farbige Kategorien
