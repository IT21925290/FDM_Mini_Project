
import streamlit as st
import pandas as pd
import numpy as np

import plotly
import plotly.express as px
from streamlit_echarts import st_echarts


st.set_page_config(page_title="Stroke Prediction", page_icon="🩺", layout="centered", initial_sidebar_state="expanded")

dataframe = pd.read_csv(r'C:\Users\nrhhe\OneDrive\Documents\SLIIT\FDM\FDM-web-app\FDM_Mini_Project\Dataset\strokeDataset.csv')


st.subheader('Count of stroke patients categorized by Age')
# Create a new dataframe with age and stroke columns
age_stroke_df = dataframe[['age', 'stroke']]

# Group the dataframe by age and stroke, and count the number of occurrences
age_stroke_count = age_stroke_df.groupby(['age', 'stroke']).size().reset_index(name='count')

# Filter the dataframe to only include patients with stroke
stroke_count = age_stroke_count[age_stroke_count['stroke'] == 1]

# Create a bar chart using Plotly Express
fig = px.bar(stroke_count, x='age', y='count')
st.plotly_chart(fig, use_container_width=True)


# Display age and stroke in a histogram
#fig = px.histogram(dataframe[dataframe['stroke']==1], x="age", nbins=30)
#st.plotly_chart(fig)


st.subheader('Proportion Of Different Smoking Categories Among Stroke Population')
# Create a new dataframe with smoking status and stroke columns
smoking_stroke_df = dataframe[['smoking_status', 'stroke']]
# Group the dataframe by smoking status and stroke, and count the number of occurrences
# Filter the dataframe to exclude unknown smoking status
dataframe = dataframe[dataframe['smoking_status'] != 'Unknown']
smoking_stroke_df = dataframe[['smoking_status', 'stroke']]
smoking_stroke_count = smoking_stroke_df.groupby(['smoking_status', 'stroke']).size().reset_index(name='count')
# Filter the dataframe to only include patients with stroke
stroke_count = smoking_stroke_count[smoking_stroke_count['stroke'] == 1]
# Create a pie chart using Plotly Express
fig = px.pie(stroke_count, values='count', names='smoking_status')
st.plotly_chart(fig, use_container_width=True)


fig = px.histogram(dataframe[dataframe['stroke']==1], x="avg_glucose_level", nbins=30)
st.plotly_chart(fig)
