import streamlit as st
import pandas as pd
import math
from pathlib import Path
import matplotlib.pyplot as plt 


# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='TABLEAU DE BORD DE SUIVI DES DOSSIERS par Malick TRAORE',
    page_icon='teteigf12.png', # This is an emoji shortcode. Could be a URL too.
    layout='wide'
)


# -----------------------------------------------------------------------------
# Declare some useful functions.

@st.cache_data
def get_gdp_data():
    """Grab GDP data from a CSV file.

    This uses caching to avoid having to read the file every time. If we were
    reading from an HTTP endpoint instead of a file, it's a good idea to set
    a maximum age to the cache with the TTL argument: @st.cache_data(ttl='1d')
    """

    # Instead of a CSV on disk, you could read from an HTTP endpoint here too.
    DATA_FILENAME = Path(__file__).parent/'data/gdp_data.csv'
    raw_gdp_df = pd.read_csv(DATA_FILENAME)

    MIN_YEAR = 1960
    MAX_YEAR = 2022

    # The data above has columns like:
    # - Country Name
    # - Country Code
    # - [Stuff I don't care about]
    # - GDP for 1960
    # - GDP for 1961
    # - GDP for 1962
    # - ...
    # - GDP for 2022
    #
    # ...but I want this instead:
    # - Country Name
    # - Country Code
    # - Year
    # - GDP
    #
    # So let's pivot all those year-columns into two: Year and GDP
    gdp_df = raw_gdp_df.melt(
        ['Country Code'],
        [str(x) for x in range(MIN_YEAR, MAX_YEAR + 1)],
        'Year',
        'GDP',
    )

    # Convert years from string to integers
    gdp_df['Year'] = pd.to_numeric(gdp_df['Year'])

    return gdp_df

gdp_df = get_gdp_data()

# -----------------------------------------------------------------------------
# Draw the actual page

# Set the title that appears at the top of the page.
st.image("teteigf12.png")
'''
# TABLEAU DE BORD DE SUIVI DES DOSSIERS
Ce tableau de bord de l'[Inspection Générale des Finances](https://www.igf.finances.gouv.ci/) permet de visualiser
l'état d'avancement des dossiers en cours à l'Inspection Générale des Finances.


'''

# Add some spacing
''
''

# Définir les pages
def page_accueil():
    st.title("Page d'accueil")
    st.write("Bienvenue sur la page d'accueil.")
    if st.button("Missions d’audit interne"):
        st.session_state["page"] = "page1"
    if st.button("Missions d’inspection et d’évaluation"):
        st.session_state["page"] = "page2"
    if st.button("Missions d’étude et de conseil"):
        st.session_state["page"] = "page3"

def page_1():
    #st.title("Page 1")
    st.title("Bienvenue sur la page présentant l'état des lieux des Missions d’audit interne.")
  
    #if st.button("Missions d’inspection et d’évaluation"):
        #st.session_state["page"] = "page2"
    #if st.button("Missions d’étude et de conseil"):
        #st.session_state["page"] = "page3"


def page_2():
    #st.title("Page 2")
    st.title("Bienvenue sur la page présentant l'état des lieux des missions d’inspection et d’évaluation.")
    if st.button("Retour à l'accueil"):
        st.session_state["page"] = "accueil"


def page_3():
    #st.title("Page 3")
    st.title("Bienvenue sur la page présentant l'état des lieux des missions d’étude et conseil.")
    if st.button("Retour à l'accueil"):
        st.session_state["page"] = "accueil"


# Initialiser l'état de session
if "page" not in st.session_state:
    st.session_state["page"] = "accueil"

# Afficher la page correspondant à l'état
if st.session_state["page"] == "accueil":
    page_accueil()
elif st.session_state["page"] == "page1":
    page_1()

    # Définition des données du tableau
    donnees = {
        "Nombre de missions planifiées dans l'année": 100,
        "Missions planifiées arrivant à échéance le mois précédent": 30,
        "Missions réalisées jusqu’au mois précédent": 24,
        "Missions arrivées à échéance au cours du mois": 33,
        "Missions réalisées dans les délais jusqu’au mois précédent": 22,
    }
    # Organisation en colonnes pour afficher les cadrans
    col1, col2, col3 = st.columns(3)  # Création de 3 colonnes

    # Ajouter des cadrans dans les colonnes
    with col1:
        st.metric("Missions planifiées dans l'année", donnees["Nombre de missions planifiées dans l'année"])
        st.metric("Missions planifiées à échéance", donnees["Missions planifiées arrivant à échéance le mois précédent"])

    with col2:
        st.metric("Missions réalisées jusqu'au mois précédent", donnees["Missions réalisées jusqu’au mois précédent"])
        st.metric("Missions réalisées dans les délais", donnees["Missions réalisées dans les délais jusqu’au mois précédent"])

    with col3:
        st.metric("Missions à échéance ce mois", donnees["Missions arrivées à échéance au cours du mois"])


    # Titre de l'application
    #st.title("Analyse des taux de réalisation des missions d'audit interne")

    # Données des mois et des taux
    mois = [
            "Janvier",
            "Février", 
            "Mars", 
            "Avril", 
            "Mai", 
            "Juin", 
            "Juillet", 
            "Août", 
            "Septembre", 
            "Octobre", 
            "Novembre", 
            "Décembre"
            ]

    taux_realisations = [0.8, 0.66, 0.72, 0.82, 0.32, 0.24, 0.74, 0.73, 0.91, 0.74, 0.85, 0.58]
    taux_delais = [0.67, 0.34, 0.04, 0.76, 0.07, 0.13, 0.30, 0.59, 0.28, 0.08, 0.62, 0.29]

    # Tracé du graphique
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(mois, taux_realisations, label="Taux réalisés jusqu'au mois précédent", marker='o', color='blue')
    ax.plot(mois, taux_delais, label="Taux réalisés dans les délais", marker='o', color='red')

    # Ajout des titres et légendes
    ax.set_title("Comparaison des taux de réalisation des missions d'audit interne", fontsize=16)
    ax.set_xlabel("Mois", fontsize=12)
    ax.set_ylabel("Taux", fontsize=12)
    ax.legend()
    ax.grid(True)
    plt.xticks(rotation=45)

    # Affichage dans Streamlit
    st.pyplot(fig)
    if st.button("Retour à l'accueil"):
        st.session_state["page"] = "accueil"

elif st.session_state["page"] == "page2":
    page_2()
elif st.session_state["page"] == "page3":
    page_3()

if __name__ == "__main__":
    get_gdp_data()





