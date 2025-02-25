import streamlit as st
import pandas as pd

# Pilih dataset
option = st.sidebar.selectbox("Pilih Dataset:", ["df_hour", "df_day"])

# Load Data
if option == "df_hour":
    df = pd.read_csv("dashboard/df_hour.csv")
elif option == "df_day":
    df = pd.read_csv("dashboard/df_day.csv")

# Tampilkan Data
st.write(f"Menampilkan dataset: {option}")
st.dataframe(df.head())
