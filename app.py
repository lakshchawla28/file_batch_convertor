import streamlit as st
import os
import pandas as pd
from io import BytesIO

from target import available_targets
from convertor import (
    convertor_csv_to_json, convertor_csv_to_xlsx,
    convertor_json_to_csv, convertor_json_to_xlsx,
    convertor_xlsx_to_csv, convertor_xlsx_to_json
)

st.title("File Batch Converter")
st.subheader("Hello! Welcome to the File Batch Converter App")

st.write("""
This simple tool helps you **convert your files** from one format to another effortlessly.  
Just upload your `.csv`, `.json`, or `.xlsx` files and choose your desired output format.

No AI involved, just pure data-type magic! 
""")

uploaded = st.file_uploader("Upload your file", type=["csv", "xlsx", "json"], accept_multiple_files=False)

if uploaded:
    ext = os.path.splitext(uploaded.name)[1].lower()
    targets = available_targets(ext)

    if not targets:
        st.error("Unsupported file format")
        st.stop()

    if ext == ".csv":
        df = pd.read_csv(uploaded)
    elif ext == ".json":
        df = pd.read_json(uploaded)
    elif ext == ".xlsx":
        df = pd.read_excel(uploaded)

    st.subheader("Quick preview:")
    st.dataframe(df.head())

    target_ext = st.radio("Convert to:", [e for e, _ in targets], format_func=dict(targets).__getitem__)

    if st.button("Convert"):
        if ext == ".csv" and target_ext == ".json":
            new_path = convertor_csv_to_json(uploaded)
            st.download_button("Download JSON File", open(new_path, "rb").read(),
                               file_name=os.path.basename(new_path),
                               mime="application/json")

        elif ext == ".csv" and target_ext == ".xlsx":
            new_path = convertor_csv_to_xlsx(uploaded)
            st.download_button("Download Excel File", open(new_path, "rb").read(),
                               file_name=os.path.basename(new_path),
                               mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

        elif ext == ".json" and target_ext == ".csv":
            new_path = convertor_json_to_csv(uploaded)
            st.download_button("Download CSV File", open(new_path, "rb").read(),
                               file_name=os.path.basename(new_path),
                               mime="text/csv")

        elif ext == ".json" and target_ext == ".xlsx":
            new_path = convertor_json_to_xlsx(uploaded)
            st.download_button("Download Excel File", open(new_path, "rb").read(),
                               file_name=os.path.basename(new_path),
                               mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

        elif ext == ".xlsx" and target_ext == ".json":
            new_path = convertor_xlsx_to_json(uploaded)
            st.download_button("Download JSON File", open(new_path, "rb").read(),
                               file_name=os.path.basename(new_path),
                               mime="application/json")

        elif ext == ".xlsx" and target_ext == ".csv":
            new_path = convertor_xlsx_to_csv(uploaded)
            st.download_button("Download CSV File", open(new_path, "rb").read(),
                               file_name=os.path.basename(new_path),
                               mime="text/csv")

        st.success("Conversion finished")
        st.title("Thank you")


          