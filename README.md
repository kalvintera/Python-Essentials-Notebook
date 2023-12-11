# Python Essentials Notebook
Das **"Python Essentials Notebook"** Projekt ist eine umfassende Lernressource für Studierende und Lehrende, die anhand eines realen Anwendungsfalls - der OMDb API - die Grundkonzepte der Python-Programmierung erforschen möchten. Es bietet praktische Beispiele und Übungen zu Datentypen, Datenquellen, Datenstrukturen, Built-in-Methoden, Funktionen und den Prinzipien der objektorientierten Programmierung.

## Projektstruktur

- **api/get_data.py:**
Eine Python-Klasse für die Interaktion mit der OMDb API.

- **processor/process_data.py:**
Eine Klasse für die Verarbeitung von Daten, inklusive spezifischer Merkmalsextraktion.
- **input/:**
Verzeichnis mit verschiedenen Eingabedateien, darunter IMDB-Filmlisten und Kundensegmentierungsdaten.
- **uebungen.ipynb:**
Ein Jupyter Notebook, das grundlegende Python-Konzepte demonstriert und Lösungen zu Übungsbeispielen enthält.
- **config.py:**
Eine Konfigurationsdatei, die Einstellungen wie API-Endpunkte und Schlüssel speichert.
- **main.py:**
Das Hauptskript, das die Funktionen der anderen Module nutzt.

## Setup
- Klonen Sie das Repository.
- Installieren Sie die erforderlichen Abhängigkeiten aus der Pipfile.
- Erstellen Sie eine .env-Datei im Projektverzeichnis und fügen Sie Ihren OMDb API-Schlüssel hinzu:

```
# API CREDENTIALS
API_KEY=IhrAPIKey
```

Den API-Schlüssel können Sie von <a href="https://www.omdbapi.com/apikey.aspx">OMDb API Key</a> beziehen.

**Abhängigkeiten**

Das Projekt verwendet folgende Pakete:

- *python-dotenv:* Zum Laden von Umgebungsvariablen.
- *requests:* Für HTTP-Anfragen.
- *jupyter:* Für das Jupyter Notebook.
- *pandas:* Zur Datenverarbeitung.
- *beautifulsoup4, lxml:* Für das Lesen der XML-Inhalte.
- *openpyxl:* Für das Lesen/Schreiben von Excel-Dateien.
- *black:* Für die Code-Formatierung.

## Nutzung
Führen Sie main.py aus, um die Skripte zu starten, oder öffnen Sie uebungen.ipynb in Jupyter, um interaktiv mit den Python-Beispielen zu arbeiten.

## Mitwirken

Feedback und Beiträge von Studierenden und Lehrenden sind immer willkommen, um dieses Projekt zu erweitern. 
Fühlen Sie sich frei, Ideen, Verbesserungen oder zusätzliche Inhalte vorzuschlagen, 
die zur Bereicherung des Lernmaterials beitragen könnten.