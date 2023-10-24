import streamlit as st
import pandas as pd
import numpy as np
import json

from streamlit_lottie import st_lottie


def load_lottiefile(filepath: str):
    with open(filepath) as f:
        lottie_json = json.load(f)
    return lottie_json

lottie_file= load_lottiefile(r'C:\Users\nrhhe\OneDrive\Documents\SLIIT\FDM\FDM-web-app\FDM_Mini_Project\animations\animation.json')
#lottie_file= load_lottiefile(r'C:\\Users\\Admin\\Desktop\\FDM\\FDM_Mini_Project\\animations\\animation.json')

st.set_page_config(page_title="Stroke Prediction", page_icon="🩺", layout="wide", initial_sidebar_state="expanded")




st.header('Welcome to Stroke Prediction WebApp',divider=True)
st.write("We're here to help you take control of your health. Welcome to Stroke Predictor, your trusted companion on the journey to a healthier and safer life")


col1, col2, col3 = st.columns([1,1,1])

with col1:
    st.write("Why We're Here")
    st.write("Strokes can be life-altering, and their prevention is of utmost importance. Our mission is to empower you with knowledge and insights to understand and reduce your risk of stroke. We believe that informed choices lead to better health, and we're here to guide you every step of the way.")

with col2:
    st.write("What We Offer")
    st.write("Stroke Predictor, you have the opportunity to assess your stroke risk based on your unique health profile. Our advanced algorithms analyze various factors to provide you with a personalized risk assessment. Whether you're young or older, an individual or a healthcare professional, our platform is tailored to meet your needs.")

with col3:
    st.write("What We Value")
    st.write("Your Health is your most valuable asset, and we're here to protect it. With Stroke Predictor, you have the power to make informed decisions, implement positive changes, and lead a healthier life. Thank you for choosing Stroke Predictor. We're with you every step of the way on your journey to a healthier, stroke-free future.")

st.write("\n\n\n\n\n\n\n\n\n")
st.subheader("Let's get started!")

st_lottie(
    lottie_file,
    speed=1, 
    reverse=False,
    loop=True,
    quality='medium',
    
    height=500,
    key=None

)



