from sutd_itp_1d.backend.attractions import Attraction
import streamlit as st

def AttractionCard(attraction: Attraction):
    with st.container(border=True):
        # st.image(attraction.image_url)
        st.subheader(attraction.name)
        st.write(attraction.description)
        st.write(f"{attraction.price:2f}")
        if st.button("Select", key=attraction.name):
            return attraction
    return None
