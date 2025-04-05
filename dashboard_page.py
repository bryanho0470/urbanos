from operator import le
from tarfile import LENGTH_NAME
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

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


   
                fig1 = px.line(df, x="Reading Date", y="Active Power (kWh)", title="Energy Consumption Over Time")
                st.plotly_chart(fig1, use_container_width=True)
                fig4 = px.line(df, x="Reading Date", y="Reactive Power (kVARh)", title="Reactive Power Over Time")
                st.plotly_chart(fig4, use_container_width=True)
                fig2 = px.bar(df,x="Reading Date", y="Active Power (kWh)", title="Energy Consumption Distribution")
                fig2.update_traces(marker_color="green") 
                st.plotly_chart(fig2, use_container_width=True)
                fig3 = px.bar(df, x="Reading Date", y="Amount", title="Total Payment")
                st.plotly_chart(fig3, use_container_width=True)

                combo_fig = make_subplots(
                    specs=[[{"secondary_y": True}]],
                    shared_xaxes=True,
                    subplot_titles=("Energy Consumption and Amount",),
                )

                combo_fig.add_trace(
                    go.Bar(
                        x=df["Reading Date"],
                        y=df["Active Power (kWh)"],
                        name="Energy Consumption",
                        marker_color="green",
                    ),
                    secondary_y=False,
                )

                combo_fig.add_trace(
                    go.Scatter(
                        x=df["Reading Date"],
                        y=df["Reactive Power (kVARh)"],
                        name="Reactive Power",
                        mode="lines+markers",
                        line=dict(color="orange", width=2),
                    ),
                    secondary_y=True,
                )

                combo_fig.update_layout(
                    title_text="Energy Consumption and Amount",
                    xaxis_title="Reading Date",
                    yaxis_title="Active Power (kWh)",
                    yaxis2_title="Reactive Power (kVARh)",
                    legend=dict(x=0.01, y=0.99),
                    height=600,
                )

                combo_fig.update_yaxes(title_text="Reactive Power (kVARh)", secondary_y=True, range=[0,20000])
                combo_fig.update_yaxes(title_text="Active Power (kWh)", secondary_y=False, range=[0, 60000])

                st.plotly_chart(combo_fig, use_container_width=True)
                # Show chart if certain columns exist

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

