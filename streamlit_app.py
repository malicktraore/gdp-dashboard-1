import streamlit as st
import pandas as pd
import math
from pathlib import Path

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
    if st.button("Retour à l'accueil"):
        st.session_state["page"] = "accueil"
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
elif st.session_state["page"] == "page2":
    page_2()
elif st.session_state["page"] == "page3":
    page_3()