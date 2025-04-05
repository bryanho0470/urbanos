import streamlit as st
import pandas as pd

def dashboard_page(navigate):
    st.title("Dashboard")
    st.write("Welcome to the dashboard!")
    
    if st.session_state.user:
        st.success(f"Welcome, {st.session_state.user['email']}!")
        if st.button("Logout"):
            st.session_state.user = None
            navigate("login")
    else:
        st.warning("You must be logged in to view this page.")
        navigate("login")
    method = st.selectbox(
            "Select data source",
            ("Database", "Local UPLOAD", "API"),
            index=0,
            key="data_source",
            help="Choose the data source for energy consumption data.",
        )
    if method == "Database":
        st.info("Database connection is not implemented yet.")
        st.stop()
    elif method == "API":
        st.info("API connection is not implemented yet.")
        st.stop()
    else:
      

        # set tabs
        electric_tab, water_tab = st.tabs(["Electricity Consumption","Water Consumption"])
                

        with electric_tab:   
            st.title("Energy Consumption Data")
            uploaded_file_elec = None
            uploaded_file_elec = st.file_uploader("Upload Electric CSV", type=["csv"], key="electric_file")
            if uploaded_file_elec is not None:
                # Read the CSV file into a DataFrame
                df = pd.read_csv(uploaded_file_elec)

                #show the table
                st.subheader("Data Preview:")
                st.dataframe(df)

                #Show chart if certain cloumns exist
                if "timestamp" in df.columns and "consumption_kwh" in df.columns:
                    st.subheader("Energy Consumption Chart:")
                    st.line_chart(df.set_index("timestamp")["consumption_kwh"])
            else:
                st.info("Please upload a CSV file to see the data.")

        with water_tab:
            st.title("Water Consumption Data")
            uploaded_file_water = None
            uploaded_file_water = st.file_uploader("Upload Water Concumption CSV", type=["csv"], key="water_file")
            if uploaded_file_water is not None:
                # Read the CSV file into a DataFrame
                df = pd.read_csv(uploaded_file_water)

                #show the table
                st.subheader("Data Preview:")
                st.dataframe(df)

                #Show chart if certain cloumns exist
                if "timestamp" in df.columns and "consumption_liters" in df.columns:
                    st.subheader("Water Consumption Chart:")
                    st.line_chart(df.set_index("timestamp")["consumption_liters"])
            else:
                st.info("Please upload a CSV file to see the data.")

