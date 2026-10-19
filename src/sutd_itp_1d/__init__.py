import streamlit as st
#
pages = [
    st.Page("pages/dashboard.py", title="dashboard :3"),
    st.Page("pages/recommendations.py", title="recommended rides :3"),
]

page = st.navigation(pages)
page.run()
