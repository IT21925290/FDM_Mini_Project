import streamlit as st
import numpy as np
import pickle
import pandas as pd
import json
from streamlit_lottie import st_lottie


#loading the original dataset to get the columns(onehotencode columns)
dataset=pd.read_csv(r"C:\Users\nrhhe\OneDrive\Documents\SLIIT\FDM\FDM-web-app\FDM_Mini_Project\Dataset\strokeDataset.csv")
#dataset=pd.read_csv(r'C:\\Users\\Admin\\Desktop\\FDM\\FDM_Mini_Project\\Dataset\\strokeDataset.csv')


#loading the trained model
loaded_model = pickle.load(open('C:/Users/nrhhe/OneDrive/Documents/SLIIT/FDM/FDM-web-app/FDM_Mini_Project/Script&model/trained_model.sav', 'rb'))
#loaded_model = pickle.load(open('C:\\Users\\Admin\\Desktop\\FDM\\FDM_Mini_Project\\Script&model\\logistic_reg_model2.sav', 'rb'))



st.header('Predicting Risk of Stroke ',divider=True)
st.write("Provide us with your clinical details using the below form and we will predict your risk of you  getting a stroke.")
st.divider()

subcol1, subcol2 = st.columns([1,1])

col1, col2 = st.columns([3,2])
with col1:
        def stroke_prediction(input_data):
                conv_nparr = np.asarray(input_data)

                # reshape the array as we are predicting for one instance
                reshaped = conv_nparr.reshape(1,-1)

                prediction = loaded_model.predict(reshaped)
                print(prediction)

                if (prediction[0] == 0):
                    st.warning('You are not at risk of stroke')
                else:
                    st.warning('You are at risk of getting a stroke , please consult a doctor')


        def convert_data(data):
            # Convert Marrital Status, Residence and Gender into 0's and 1's
                data['gender']=data['gender'].apply(lambda x : 1 if x=='Male' else 0) 
                data["Residence_type"] = data["Residence_type"].apply(lambda x: 1 if x=="Urban" else 0)
                data["ever_married"] = data["ever_married"].apply(lambda x: 1 if x=="Yes" else 0)




        def OnehotEncoding(data):
            
            #if Stroke or id column exist in dataset drop them
            if 'id' in dataset.columns:
                dataset.drop('id', axis=1, inplace=True)

            if 'stroke' in dataset.columns:
                dataset.drop('stroke', axis=1, inplace=True)
            
            #concat to the bottom of the dataset
            to_one_hotencode=pd.concat([dataset,data],axis=0,ignore_index=True)
            

            #one hot encode the data
            data_dummies = to_one_hotencode[['smoking_status','work_type']]
            data_dummies = pd.get_dummies(data_dummies, drop_first=False)
            to_one_hotencode.drop(columns=['smoking_status','work_type'],inplace=True)
            to_one_hotencode=to_one_hotencode.merge(data_dummies,left_index=True, right_index=True,how='left')
            
            #drop unknown smoking status if it exists
            if 'smoking_status_Unknown' in to_one_hotencode.columns:
                to_one_hotencode.drop('smoking_status_Unknown', axis=1, inplace=True)
            
            #return the last row of the dataset
            #which is the user input
            oh_data=to_one_hotencode.tail(1)
            return oh_data

        #commented bec of errors    
        # def scale_data(data):
        #     std = StandardScaler()
        #     scaled_data = std.fit_transform(data)
        #     return scaled_data
            


        #form to get user input
        with st.form(key='my_form'):
            age = st.number_input(label='Enter your age',   min_value=0.1,max_value=120.0)

            gender = st.selectbox(
                label='Select your gender',
                index=None, 
                options=['Male', 'Female'])
            
            hypertension = st.selectbox(
                label='Do you have hypertension?',
                placeholder='Select Yes or No',
                index=None, 
                options=['Yes', 'No'])
            hypertension = 1 if hypertension == 'Yes' else 0

                              
            heart_disease = st.selectbox(
                label='Do you have any heart diseases?',
                placeholder='Select Yes or No',
                index=None, 
                options=['Yes', 'No'])
            heart_disease = 1 if heart_disease == 'Yes' else 0

            ever_married = st.selectbox(
                label='Are you married?',
                placeholder='Select Yes or No',
                index=None, 
                options=['Yes', 'No'])

            work_type = st.selectbox(
                label='What is your work type?',
                index=None, 
                options=['children','Private','Self-employed','Government Job','Never worked'])
            if work_type == 'Government Job':
                work_type = 'Govt_job'
            elif work_type == 'Never worked':
                work_type = 'Never_worked'

            Residence_type = st.selectbox(
                label='What is your residence type?',
                index=None, 
                options=['Urban','Rural'])
            
            avg_glucose_level = st.number_input(label='Enter your average glucose level',   min_value=0.0,max_value=350.0)
            if avg_glucose_level >=250 :
                    st.warning('You are aproching Dangerous glucose levels, reaching out to Medical care is recomended .')
            
            bmi = st.number_input(label='Enter your BMI',   min_value=0.0,max_value=100.0)

            smoking_status = st.selectbox(
                label='Do you smoke ?',
                placeholder='Select a option',
                index=None, 
                options=['never smoked','formerly smoked','smokes'])
            
            if st.form_submit_button(label='Submit'):
                if age == 0 or gender == ''or hypertension == '' or heart_disease == '' or work_type == '' or Residence_type == '' or avg_glucose_level == 0 or bmi == 0 or smoking_status == '':
                    st.warning('Please fill in all fields.')
                else:
                    
                    data = pd.DataFrame({
                        'gender': [gender],
                        'age': [age],
                        'hypertension': [hypertension],
                        'heart_disease': [heart_disease],
                        'ever_married': [ever_married],
                        'work_type': [work_type],
                        'Residence_type': [Residence_type],
                        'avg_glucose_level': [avg_glucose_level],
                        'bmi': [bmi],
                        'smoking_status': [smoking_status]
                    })
                    

                    # Convert Marrital Status, Residence and Gender into 0's and 1's
                    convert_data(data)
                    
                    #one hot encode the user input data
                    encoded_data=OnehotEncoding(data)
                    
                    #applying processed data to the model
                    #predict the risk of stroke
                    stroke_prediction(encoded_data)

with col2:
        def load_lottiefile(filepath: str):
            with open(filepath, "r") as f:
                return json.load(f)

        
        lottie_coding = load_lottiefile("C:\\Users\\nrhhe\\OneDrive\\Documents\\SLIIT\\FDM\\FDM-web-app\\FDM_Mini_Project\\animations\\p2.json")
        #lottie_coding = load_lottiefile("C:\\Users\\Admin\\Desktop\\Fdm_app\\app\\images\\p2.json")
        st_lottie(
            lottie_coding,
            speed =1,
            reverse = False,
            loop = True
        )