import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="📂 File Converter & Cleaner" , layout="wide")
st.title("📂 File Converter & Cleaner")
st.write("Upload your CSV and Excel files to clean the data convert data formats effortlessly 🚀")

files = st.file_uploader("Upload CSV or Excel files", type=["csv" , "xlsx"], accept_multiple_files=True)

if files:
    for file in files:
        ext = file.name.split(".")[-1]
        df = pd.read_csv(file) if ext == "csv" else pd.read_excel(file)

        st.subheader(f"🔍 {file.name} - Preview")
        st.dataframe(df.head())

        if st.checkbox(f"Fill Missing Values - {file.name}"):
            df.fillna(df.select_dtypes(include=["number"]).mean(), inplace=True)
            st.success("Missing values filled successfully")
            st.dataframe(df.head())
        selected_columns = st.multiselect(f"Select Columns - {file.name}" , df.columns , default=df.columns)
        df = df[selected_columns]
        st.dataframe(df.head())
        if st.checkbox