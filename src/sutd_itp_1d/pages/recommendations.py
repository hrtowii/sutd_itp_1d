import streamlit as st
from sutd_itp_1d.backend.attractions import Attraction
from sutd_itp_1d.pages.components.attraction import AttractionCard
attractions = [
    Attraction("roller coaster", "cool roller coaster", 20.0, "lol"),
    Attraction("roller coaster", "cool roller coaster", 20.0, "lol"),
    Attraction("roller coaster", "cool roller coaster", 20.0, "lol"),
    Attraction("roller coaster", "cool roller coaster", 20.0, "lol"),
    Attraction("roller coaster", "cool roller coaster", 20.0, "lol"),
    Attraction("roller coaster", "cool roller coaster", 20.0, "lol"),
    Attraction("roller coaster", "cool roller coaster", 20.0, "lol"),
    Attraction("roller coaster", "cool roller coaster", 20.0, "lol"),
    Attraction("roller coaster", "cool roller coaster", 20.0, "lol"),
    Attraction("roller coaster", "cool roller coaster", 20.0, "lol"),
    Attraction("roller coaster", "cool roller coaster", 20.0, "lol"),
    Attraction("roller coaster", "cool roller coaster", 20.0, "lol")
]
def render():
    st.title("recommendations :)")
    for attraction in attractions:
        AttractionCard(attraction=attraction)
