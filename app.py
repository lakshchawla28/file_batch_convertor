import streamlit as st
import os
import pandas as pd

st.title(" File Batch Converter")
st.subheader(" Hello! Welcome to the File Batch Converter App")

st.write("""
This simple tool helps you **convert your files** from one format to another effortlessly.  
Just upload your `.csv`, `.json`, or `.xlsx` files and choose your desired output format.

No AI involved, just pure data-type magic! 🧙‍♂️  
""")


uploaded=st.file_uploader("upload your file",type=["csv", "xlsx" ,"json"],accept_multiple_files=False)

if uploaded:
     file_ext = os.path.splitext(uploaded.name)[1].lower()
     base_name=os.path.splitext(uploaded.name)[0]

     if file_ext ==".csv":
          df=pd.read_csv(uploaded)
          
     elif file_ext ==".json":
          df=pd.read_json(uploaded)
     elif file_ext ==".xlsx":
          df=pd.read_excel(uploaded)
     else:
          st.error("unsupported file format")
          st.stop
else:
     st.write("upload a file")

st.success(f"file loaded {uploaded.name}")

st.subheader("Quick preview of file")
st.dataframe(df.head())


st.info("Start by uploading a file using the upload button (coming soon!) 🚀")
