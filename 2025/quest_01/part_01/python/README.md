# Lösung

## Datenvorbereitung

### what_is_your_name.py (Zeilen 1 - 10)

Das Einlesen und Aufbereiten der Eingebedaten ist an eine Utility-Funktion ausgelagert (utils.py).

Zu diesem Zweck wird Python der Pfad auf diese Datei bekannt gegeben, damit aus diesem Pfad Pythondateien importiert werden können.

Danach wird der absolute Pfad auf die Eingabedaten ermittelt und an die Hilfsfunktion übergeben. Das Ergebnis der Hilfsfunktion wird schließlich zur Namenssuche verwendet.

### ../../utils.py (Zeilen 1 - 16)

Die Eingabedatei besteht aus mehreren Zeilen, von denen zwei Zeilen die Nutzdaten der Aufgabe enthalten:

- Die erste Zeile mit Nutzdaten enthält eine komma-separierte Liste der zu durchsuchenden Namen.
- Die zweite Zeile mit Nutzdaten enthält eine komma-separierte Liste der Kommandos zur Namenssuche.

Die Datei wird zeilenweise gelesen. Jede Zeile mit Nutzdaten wird in eine Liste umgewandelt. Jede Liste wird in einer Map unter einem Integer-Schlüssel gespeichert.

- Key == 0: Liste der zu durchsuchenden Namen.
- Key == 1: Liste der Kommandos zur Namenssuche.

Die Map dient lediglich dem vereinfachten Handling bei der Datenvorbereitung sowie zur Rückgabe an das Hauptprogramm.

## Namenssuche (Zeilen 12 - 25)

Die Anzahl der Namen ergibt sich aus der Länge der Namensliste unter Key == 1. Ein aktueller Zeiger zeigt auf den logisch ersten Namen in der Liste.

Für jedes Kommando in der Kommandoliste werden Suchrichtung und Suchlänge ermittelt. Je nach Suchrichtung wird der aktuelle Zeiger auf einen Namen in der Namensliste um die Suchlänge erhöht (maximal bis zur Länge der Namensliste) bzw. reduziert (minimal bis zur Position 1 in der Namensliste).

Die technische Position in der Namensliste ergibt sich am Ende durch den um 1 reduzierten Zeiger.
