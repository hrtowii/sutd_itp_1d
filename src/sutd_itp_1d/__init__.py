import streamlit as st
from sutd_itp_1d.pages import dashboard, recommendations
#
pages = [
    st.Page(dashboard.render, title="dashboard :3", url_path="/dashboard"),
    st.Page(recommendations.render, title="recommended rides :3", url_path="/recommend"),
]

page = st.navigation(pages)
page.run()
