# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 20:00:09 2023

@author: MK$WAGGER
"""

import pickle
import numpy as np
import streamlit as st

loaded_model= pickle.load(open("G:\ONEDRIVE\Documents\GitHub\medical_insurance_costprediction\Trained_model.sav",'rb'))
def insurance(input_data):
    input_data_as_np_array = np.array(input_data)
    input_data_reshape = input_data_as_np_array.reshape(-1,1)
    
    prediction = loaded_model.predict(input_data_reshape)
    print(prediction)
    
 
def main():
    st.title("Medical Health Insurance Predictor App")
    Age = st.text_input('Age')
    Sex = st.text_input('Sex (1->Male, 0->Female)')
    bmi = st.text_input('BMI')
    children = st.text_input("No of children:")
    smoker = st.text_input("Smoker or not (0->non smoker, 1 -> non smoker")
    cost = ""
    
    if st.button("Test Results : "):
        cost = health_insurance_cost([Age,Sex,bmi,children,smoker])
    
    st.success(cost)

if __name__ == "__main__":
    main()
