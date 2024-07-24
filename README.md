# Textkorrektur mit OpenAI

Dieses Skript verwendet OpenAI GPT-4o mini zur Korrektur von deutschem Text, der in die Zwischenablage kopiert wurde. Es nutzt die `pynput`-Bibliothek zur Erkennung von Hotkeys, `pyperclip` zum Arbeiten mit der Zwischenablage und `playsound` zum Abspielen eines Signals, wenn die Textkorrektur abgeschlossen ist.

## Voraussetzungen


Stellen Sie sicher, dass die folgenden Python-Pakete installiert sind:

- `pynput`
- `pyperclip`
- `playsound`
- `openai`

Diese Pakete können Sie mit dem folgenden Befehl installieren:

```bash
pip install pynput pyperclip playsound openai
```

Zusätzlich benötigen Sie eine OpenAI API-Schlüssel, den Sie in den Code einfügen müssen.

## Installation
OpenAI API-Schlüssel einrichten. https://platform.openai.com/api-keys

Sie müssen Ihren OpenAI API-Schlüssel in die Variable api_key im Skript einfügen. Falls der Schlüssel nicht gesetzt ist, wird eine Fehlermeldung ausgegeben.


## Signaldatei vorbereiten

Stellen Sie sicher, dass eine Audiodatei namens signal.mp3 im gleichen Verzeichnis wie das Skript vorhanden ist. Diese Datei wird abgespielt, sobald die Textkorrektur abgeschlossen ist.


## Ausführung
Um das Skript auszuführen, starten Sie es einfach mit Python:

```bash
python textkorrektur.py
```

## Hotkey

Drücken Sie Ctrl + E, um den aktuell ausgewählten Text zu kopieren und die Korrektur zu starten. Der korrigierte Text wird dann automatisch wieder in die Zwischenablage kopiert.

## Textauswahl

Stellen Sie sicher, dass der zu korrigierende Text in der Zwoschenablage ist, bevor Sie den Hotkey verwenden.

## Fehlerbehebung
Falls Fehler auftreten, überprüfen Sie bitte die folgenden Punkte:

Ist der OpenAI API-Schlüssel korrekt gesetzt?
Ist die signal.mp3-Datei im richtigen Verzeichnis vorhanden?
Sind alle benötigten Python-Pakete installiert?
##Lizenz
Dieses Projekt steht unter der MIT-Lizenz. Siehe die LICENSE-Datei für weitere Informationen.
