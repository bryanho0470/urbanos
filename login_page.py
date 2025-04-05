import pyrebase
import streamlit as st

def login_page(navigate):
    # firebase initialize
    firebase_config = st.secrets["firebase"]
    firebase = pyrebase.initialize_app(firebase_config)
    auth = firebase.auth()

    st.title("Firebase Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            st.session_state.user = user
            navigate("dashboard")

        except Exception as e:
            st.error("Invalid Credentials")
