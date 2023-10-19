import streamlit as st
import numpy as np
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder

st.set_page_config(page_title="Stroke Prediction", page_icon="🩺", layout="wide", initial_sidebar_state="expanded")

# Load the SVM model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

def convert_data(data):
    # Define label encoders for categorical variables
    label_encoders = {
        'gender': LabelEncoder(),
        'ever_married': LabelEncoder(),
        'work_type': LabelEncoder(),
        'Residence_type': LabelEncoder(),
        'smoking_status': LabelEncoder()
    }
    
    for feature, encoder in label_encoders.items():
        data[feature] = encoder.fit_transform(data[feature])

    return data

def stroke_prediction(input_data):
    input_data = convert_data(input_data)

    # Ensure that the input data has the expected feature names
    expected_features = [
        'gender', 'age', 'hypertension', 'heart_disease', 'ever_married', 'work_type', 'Residence_type',
        'avg_glucose_level', 'bmi', 'smoking_status'
    ]
    
    # Add any missing features with default values
    for feature in expected_features:
        if feature not in input_data:
            input_data[feature] = 0

    # Align the columns with the expected feature order
    input_data = input_data[expected_features]

    # Make the prediction
    prediction = loaded_model.predict(input_data.values.reshape(1, -1))

    if prediction[0] == 0:
        st.warning('You are not at risk of stroke')
    else:
        st.warning('You are at risk of stroke')

# Form to get user input
with st.form(key='my_form'):
    age = st.number_input(label='Enter your age', min_value=0, max_value=120)
    gender = st.radio("Select your gender", options=["Male", "Female"])
    hypertension = st.radio("Do you have hypertension?", options=["Yes", "No"])
    heart_disease = st.radio("Do you have any heart diseases?", options=["Yes", "No"])
    ever_married = st.radio("Are you married?", options=["Yes", "No"])
    work_type = st.radio("What is your work type?", options=["children", "Private", "Self-employed", "Government Job", "Never worked"])
    Residence_type = st.radio("What is your residence type?", options=["Urban", "Rural"])
    avg_glucose_level = st.number_input(label='Enter your average glucose level', min_value=0.0, max_value=350.0)
    bmi = st.number_input(label='Enter your BMI', min_value=0.0, max_value=100.0)
    smoking_status = st.radio("Do you smoke?", options=["never smoked", "formerly smoked", "smokes"])
    
    if st.form_submit_button(label='Submit'):
        # Check if any of the input fields are empty
        if not age or not gender or not hypertension or not heart_disease or not ever_married or not work_type or not Residence_type or not avg_glucose_level or not bmi or not smoking_status:
            st.warning('Please fill in all fields.')
        else:
            # Create a DataFrame with the user input
            data = pd.DataFrame({
                'age': [age],
                'gender': [gender],
                'hypertension': 1 if hypertension == "Yes" else 0,
                'heart_disease': 1 if heart_disease == "Yes" else 0,
                'ever_married': 1 if ever_married == "Yes" else 0,
                'work_type': work_type,
                'Residence_type': Residence_type,
                'avg_glucose_level': [avg_glucose_level],
                'bmi': [bmi],
                'smoking_status': smoking_status
            })
            
            stroke_prediction(data)
