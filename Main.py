import streamlit as st
import pandas as pd
import numpy as np
import json

from streamlit_lottie import st_lottie


def load_lottiefile(filepath: str):
    with open(filepath) as f:
        lottie_json = json.load(f)
    return lottie_json

lottie_file= load_lottiefile(r'C:\Users\nrhhe\OneDrive\Documents\SLIIT\FDM\web-app\animation.json')

st.set_page_config(page_title="Stroke Prediction", page_icon="🩺", layout="wide", initial_sidebar_state="expanded")

st.title('Welcome to Stroke Prediction WebApp')

#st.image(r'C:\Users\nrhhe\OneDrive\Documents\SLIIT\FDM\web-app\scope.png', width=700)



st_lottie(
    lottie_file,
    speed=1, 
    reverse=False,
    loop=True,
    quality='low',
    
    height=500,
    key=None

)