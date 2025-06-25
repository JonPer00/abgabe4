# Programmierübung Aufgabe 2

## Analyse und Visualisierung von EKG-Daten aus CSV-Dateien

In diesem Projekt werden EKG-Daten aus CSV-Dateien geladen, analysiert und mit interaktiven Plots visualisiert. Die Anwendung ist mit [Streamlit](https://streamlit.io/) umgesetzt und ermöglicht eine einfache Auswahl und Auswertung von Versuchspersonen und deren EKG-Messungen.

---

## Umgang mit PDM

- Zum Aufsetzen eines Projektes einmalig  
  ```bash
  pdm init
  ```
- Zum Installieren eines Projektes nach dem Clonen  
  ```bash
  pdm install
  ```
- Zum Hinzufügen eines Paketes  
  ```bash
  pdm add <paketname>
  ```

> **Hinweis:**  
> Die Datei `.gitignore` legt fest, was von git ignoriert wird.  
> __Vor__ dem ersten Commit sollte der Ordner `.venv` unbedingt eingetragen werden!

---

## Nutzung des Projektes

1. Klone das Repository mit [`diesem Link`](https://github.com/JonPer00/proueb_2025) in Visual Studio Code.
2. Führe im Terminal  
   ```bash
   pdm install
   ```
   aus, um alle Abhängigkeiten zu installieren.
3. Installiere unter "Extensions" die Erweiterung **Streamlit Runner**.
4. Installiere Streamlit im Projekt mit  
   ```bash
   pdm add streamlit
   ```
5. Um die Daten aus einer __CSV__-Datei zu analysieren, führe die Datei `main_ausgabe.py` mit Streamlit aus:  
   Rechtsklick auf `main_ausgabe.py` → **Run with Streamlit**.

Die Anwendung startet im Browser unter `localhost`.  
Bei Änderungen am Code genügt es, die Datei zu speichern und die Browserseite neu zu laden, um die Anpassungen zu sehen.

---

## Verwendete Funktionen und Methoden

Im Projekt werden unter anderem folgende zentrale Methoden verwendet:

- **`load_by_id()`**  
  Lädt eine Person oder ein EKG anhand der ID aus der Datenbank.
- **`find_peaks()`**  
  Findet Peaks (Herzschläge) in den EKG-Daten (optional, je nach Version mit oder ohne scipy).
- **`estimate_hr()`**  
  Schätzt die Herzrate aus den EKG-Daten.
- **`plot_time_series()`**  
  Erstellt einen Plot der EKG-Zeitreihe (z.B. die ersten 20.000 Messpunkte).

---

Hier noch eine kleiner prelook auf die Grafik: 
 ![](https://github.com/JonPer00/abgabe4/data/picutes/screen.jpg)

Viel Spaß beim Ausprobieren und Analysieren der EKG-Daten!