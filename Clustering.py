# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 17:41:01 2023

@author: HP
"""

import pickle
import streamlit as st
import numpy as np

with open('C:/Users/HP/Downloads/k_mean.pkl', 'rb') as file:
    kmeans_loaded = pickle.load(file)

def cluster_prediction(input_data):
    
    input_data_asarray=np.asarray(input_data)
    input_data_reshaped=input_data_asarray.reshape(1,-1)
    prediction=kmeans_loaded.predict(input_data_reshaped)
    print(prediction)
    
    if (prediction[0] == 0):
      return 'Developing Country'
    elif (prediction[0] == 1):
      return 'Developed Country'
    else:
      return 'Under Developed Country'
    
    
    
def main():
        
    st.title('KMeans Prediction Model')
    
    CO2_Emissions=st.text_input ('Enter CO2 Emissions')
    Energy_Usage=st.text_input ('Enter Energy Usage')
    GDP=st.text_input ('Enter GDP')
    Hours_to_do_Tax=st.text_input ('Enter Hours to do Tax')
    Internet_Usage=st.text_input ('Enter Internet Usage')
    Lending_Interest=st.text_input ('Enter Lending Interest')
    Population_Total=st.text_input ('Enter Population Total')
    Tourism_Inbound=st.text_input ('Enter Tourism Inbound')
        
    
    predict=''    
    
    if st.button('Submit'):
        predict = cluster_prediction([CO2_Emissions,Energy_Usage,GDP,Hours_to_do_Tax,
                                      Internet_Usage,Lending_Interest,Population_Total,
                                      Tourism_Inbound])
            
    st.success(predict)
    
if __name__=='__main__': 
    main()         