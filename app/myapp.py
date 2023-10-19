import streamlit as st
import pickle
import numpy as np
import json
from streamlit_lottie import st_lottie



loaded_model = pickle.load(open('C:\\Users\\Admin\\Desktop\\Fdm_app\\app\\Regression model\\logistic_reg_model2.sav', 'rb'))

# Function to predict stroke based on input features
def predict_stroke(X_train):
    X_train = np.array(X_train).reshape(1, -1)
    prediction = loaded_model.predict(X_train)
    probability = loaded_model.predict_proba(X_train)[0][1]
    return prediction, probability

# Create a Streamlit web app
def main():
    st.set_page_config(
        page_title="Stroke Prediction App",
        page_icon=":heart:",
    )

    # Add custom CSS styles
    st.markdown(
        """
        <style>

            
        .stHeader {
            color: #333;
            font-size: 24px;
        }
        .stButton button {
            background-color: #008080;
            color: white;
            font-weight: bold;
            border-radius: 5px;
        }
        .stButton button:hover {
            background-color: #005757;
        }
        .stSuccess {
            background-color: #32CD32;
            color: white;
        }
        .stError {
            background-color: #FF0000;
            color: white;
        }
        .stImage {
            max-width: 100%;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


 # Create a sidebar for navigation
    st.sidebar.header("Navigation")
    page = st.sidebar.radio("Go to", ["Charts", "Stroke Prediction"])

    if page == "Charts":
        show_name_page()
    elif page == "Stroke Prediction":
        show_prediction_type_page()

# Define the "Name" page content
def show_name_page():
    st.title("Charts of prediction")

    # You can add content specific to the "Name" page here.

# Define the "Prediction Type" page content
def show_prediction_type_page():
    
    st.header("Stroke Prediction Web App")
    st.subheader("Enter the required information to predict the likelihood of stroke.")

    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", min_value=1, max_value=100, value=30)
        hypertension = st.selectbox("Hypertension", ("Yes", "No"))
        heart_disease = st.selectbox("Heart Disease", ("Yes", "No"))
        avg_glucose_level = st.number_input("Average Glucose Level", min_value=0.0, value=80.0)
        bmi = st.number_input("BMI", min_value=0.0, value=20.0)
        gender = st.selectbox("Gender", ("Male", "Female"))
        smoking_status = st.selectbox("Smoking Status", ("Unknown", "Formerly Smoked", "Never Smoked", "Smokes"))
        ever_married = st.selectbox("Ever Married", ("Yes", "No"))
        work_type = st.selectbox("Work Type", ("Private", "Self-employed", "Children", "Govt_job", "Never_worked"))
        residence_type = st.selectbox("Residence Type", ("Urban", "Rural"))

    with col2:
        def load_lottiefile(filepath: str):
            with open(filepath, "r") as f:
                return json.load(f)

        
        lottie_coding = load_lottiefile("C:\\Users\\Admin\\Desktop\\Fdm_app\\app\\images\\p2.json")
        st_lottie(
            lottie_coding,
            speed =1,
            reverse = False,
            loop = True
        )


    # Convert categorical inputs to numerical values
    hypertension = 1 if hypertension == "Yes" else 0
    heart_disease = 1 if heart_disease == "Yes" else 0
    gender = 1 if gender == "Male" else 0
    ever_married = 1 if ever_married == "Yes" else 0
    residence_type = 1 if residence_type == "Urban" else 0

    # Map smoking status to numerical values
    smoking_map = {
        "Unknown": 0,
        "Formerly Smoked": 1,
        "Never Smoked": 2,
        "Smokes": 3
    }
    smoking_status = smoking_map[smoking_status]

    # Map work type to numerical values
    work_type_map = {
        "Govt_job": 0,
        "Never_worked": 1,
        "Private": 2,
        "Self-employed": 3,
        "Children": 4,
    }
    work_type = work_type_map[work_type]

    # Create a button to predict stroke
    if st.button("Predict Stroke"):
        # Gather input features
        X_train = [age, hypertension, heart_disease, avg_glucose_level, bmi, gender, smoking_status, ever_married, work_type, residence_type]

        # Predict stroke and probability
        prediction, probability = predict_stroke(X_train)

        # Display the prediction
        if prediction[0] == 0:
            st.markdown("<div class='stSuccess'>Congratulations! You have a low risk of stroke.</div>", unsafe_allow_html=True)
            
            lottie_coding = load_lottiefile("C:\\Users\\Admin\\Desktop\\Fdm_app\\app\\images\\p2.json")
            st_lottie(
                lottie_coding,
                speed =1,
                reverse = False,
                loop = True
            )

        else:
            st.markdown("<div class='stError'>Warning! You are at a high risk of stroke.</div>", unsafe_allow_html=True)
            st.write("Probability of stroke:", probability)

    

# Run the web app
if __name__ == "__main__":
    main()
