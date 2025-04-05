from login_page import login_page
from dashboard_page import dashboard_page

import streamlit as st

def navigate(page):
    st.session_state.page = page
    st.rerun()  # 🧠 Forces Streamlit to reload and route to the correct page

# Initialize session
if "page" not in st.session_state:
    st.session_state.page = "login"

if "user" not in st.session_state:
    st.session_state.user = None

# Route based on session state
if st.session_state.page == "login":
    login_page(navigate)
elif st.session_state.page == "dashboard":
    if st.session_state.user:
        dashboard_page(navigate)
    else:
        st.warning("You must be logged in to view this page.")
        navigate("login")