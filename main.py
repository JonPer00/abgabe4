import streamlit as st
import read_person_data
import ekgdata
import matplotlib.pyplot as plt
from PIL import Image

#%% Zu Beginn

# Lade alle Personen
person_names = read_person_data.get_person_list(read_person_data.load_person_data())

# Anlegen diverser Session States
## Gewählte Versuchsperson
if 'aktuelle_versuchsperson' not in st.session_state:
    st.session_state.aktuelle_versuchsperson = 'None'

## Anlegen des Session State. Bild, wenn es kein Bild gibt
if 'picture_path' not in st.session_state:
    st.session_state.picture_path = 'data/pictures/none.jpg'

## TODO: Session State für Pfad zu EKG Daten 

#%% Design des Dashboards

# Schreibe die Überschrift
st.write("# EKG APP")
st.write("## Versuchsperson auswählen")

# Auswahlbox, wenn Personen anzulegen sind
st.session_state.aktuelle_versuchsperson = st.selectbox(
    'Versuchsperson',
    options = person_names, key="sbVersuchsperson")

# Name der Versuchsperson
st.write("Name: ", st.session_state.aktuelle_versuchsperson) 

# TODO: Weitere Daten wie Geburtsdatum etc. schön anzeigen

# Alter der Versuchsperson anzeigen
if st.session_state.aktuelle_versuchsperson in person_names:
    person_dict = read_person_data.find_person_data_by_name(st.session_state.aktuelle_versuchsperson)
    from person import Person
    person_obj = Person(person_dict)
    st.write("Alter:", person_obj.calc_age())
 

# Nachdem eine Versuchsperson ausgewählt wurde, die auch in der Datenbank ist
# Finde den Pfad zur Bilddatei
if st.session_state.aktuelle_versuchsperson in person_names:
    st.session_state.picture_path = read_person_data.find_person_data_by_name(st.session_state.aktuelle_versuchsperson)["picture_path"]
    # st.write("Der Pfad ist: ", st.session_state.picture_path) 

#%% Bild anzeigen


image = Image.open(st.session_state.picture_path)
st.image(image, caption=st.session_state.aktuelle_versuchsperson)

if st.session_state.aktuelle_versuchsperson in person_names:
    person_dict = read_person_data.find_person_data_by_name(st.session_state.aktuelle_versuchsperson)
    st.session_state.picture_path = person_dict["picture_path"]

#maximale Herzfrequenz anzeigen

from person import Person


if st.session_state.aktuelle_versuchsperson in person_names:
    person_dict = Person.find_person_data_by_name(st.session_state.aktuelle_versuchsperson)
    person_obj = Person(person_dict)
    st.write("Maximale Herzfrequenz:", person_obj.calc_max_heart_rate())

from ekgdata import EKGdata

ekg_id = 5  # Beispiel-ID, z.B. aus einer Auswahlbox
ekg_obj = EKGdata.load_by_id(ekg_id)
if ekg_obj:
    st.write("EKG geladen mit ID:", ekg_obj.id)
    ekg_obj.plot_time_series()
    st.plotly_chart(ekg_obj.fig)
else:
    st.write("Kein EKG mit dieser ID gefunden.")
    
#% Öffne EKG-Daten
# TODO: Für eine Person gibt es ggf. mehrere EKG-Daten. Diese müssen über den Pfad ausgewählt werden können
# Vergleiche Bild und Per-son
current_egk_data = ekgdata.EKGdata(read_person_data.find_person_data_by_name(st.session_state.aktuelle_versuchsperson)["ekg_tests"][0])

#%% EKG-Daten als Matplotlib Plot anzeigen
# Nachdem die EKG, Daten geladen wurden
# Erstelle den Plot als Attribut des Objektes
current_egk_data.plot_time_series()
# Zeige den Plot an
st.plotly_chart(current_egk_data.fig)

# %% Herzrate bestimmen
# Schätze die Herzrate 
#current_egk_data.estimate_hr()
# Zeige die Herzrate an
#st.write("Herzrate ist: ", int(current_egk_data.heat_rate)) 
