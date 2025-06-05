import json
import pandas as pd
import plotly.express as px

# %% Objekt-Welt

# Klasse EKG-Data für Peakfinder, die uns ermöglicht peaks zu finden

class EKGdata:

## Konstruktor der Klasse soll die Daten einlesen

    def __init__(self, ekg_dict):
        #pass
        self.id = ekg_dict["id"]
        self.date = ekg_dict["date"]
        self.data = ekg_dict["result_link"]
        self.df = pd.read_csv(self.data, sep='\t', header=None, names=['Messwerte in mV','Zeit in ms',])
   
    @staticmethod
    def load_by_id(ekg_id):
        """Lädt ein EKG anhand der EKG-ID aus der Datenbank und gibt ein EKGdata-Objekt zurück."""
        with open("data/person_db.json", "r") as file:
            person_data = json.load(file)
        found_ids = []
        for person in person_data:
            for ekg in person.get("ekg_tests", []):
               found_ids.append(ekg["id"])
               if str(ekg["id"]) == str(ekg_id):
                   return EKGdata(ekg)
        print("Gefundene EKG-IDs:", found_ids)
        print("Gesuchte EKG-ID:", ekg_id)
        return None
   
    def plot_time_series(self):
        """Erstellt einen Plotly-Line-Plot der EKG-Daten und speichert ihn als Attribut."""
        self.fig = px.line(self.df, x="Zeit in ms", y="Messwerte in mV", title=f"EKG ID: {self.id}")
        return self.fig


if __name__ == "__main__":
    print("This is a module with some functions to read the EKG data")
    file = open("data/person_db.json")
    person_data = json.load(file)
    ekg_dict = person_data[0]["ekg_tests"][0]
    print(ekg_dict)
    ekg = EKGdata(ekg_dict)
    print(ekg.df.head())
