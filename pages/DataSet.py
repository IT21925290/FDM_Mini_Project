import streamlit as st
import pandas as pd
import os 


st.title('This is out DATA SET page')



dataframe =pd.read_csv(r'C:\Users\nrhhe\OneDrive\Documents\SLIIT\FDM\FDM-web-app\FDM_Mini_Project\Dataset\strokeDataset.csv')
dataframe



current_directory = os.getcwd()
print(current_directory)


st.write("There Are 5110 Rows and 12 Columns in this Dataset", )