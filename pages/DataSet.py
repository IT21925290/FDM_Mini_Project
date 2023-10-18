import streamlit as st
import pandas as pd


st.title('This is out DATA SET page')

dataframe =pd.read_csv(r'C:\Users\nrhhe\Downloads\SLIIT\FDM\Datasets\strokeDataset.csv')
dataframe

st.write("There Are 5110 Rows and 12 Columns in this Dataset", )