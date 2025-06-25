import json
import pandas as pd
import plotly.graph_objects as go

class EKGdata:
    def __init__(self, ekg_dict):
        self.id = ekg_dict["id"]
        self.date = ekg_dict["date"]
        self.data = ekg_dict["result_link"]
        self.df = pd.read_csv(self.data, sep='\t', header=None, names=['Messwerte in mV','Zeit in ms',])

    @staticmethod
    def load_by_id(ekg_id):
        """Lädt ein EKG anhand der EKG-ID aus der Datenbank und gibt ein EKGdata-Objekt zurück."""
        with open("data/person_db.json", "r") as file:
            person_data = json.load(file)
        for person in person_data:
            for ekg in person.get("ekg_tests", []):
                if str(ekg["id"]) == str(ekg_id):
                    return EKGdata(ekg)
        return None

    def plot_time_series(self):
        """Zeigt die ersten 20.000 Werte der EKG-Zeitreihe."""
        df_cut = self.df.head(2000)
        x = df_cut["Zeit in ms"]
        y = df_cut["Messwerte in mV"]

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='EKG'))

        fig.update_layout(
            title=f"EKG ID: {self.id}",
            xaxis_title="Zeit in ms",
            yaxis_title="Messwerte in mV",
            template="plotly_white"
        )
        self.fig = fig
        return fig

if __name__ == "__main__":
    print("This is a module with some functions to read the EKG data")
    # Beispiel zum Testen:
    with open("data/person_db.json") as file:
        person_data = json.load(file)
    ekg_dict = person_data[0]["ekg_tests"][0]
    ekg = EKGdata(ekg_dict)
    ekg.plot_time_series().show()