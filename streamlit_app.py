# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 19:14:04 2022

@author: LMoran
"""


import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle

with open('final_model.pickle','rb') as modelFile:
    model = pickle.load(modelFile)
    

st.write(
'''

## Will It Rain Tomorrow?

In this app, you will be able to determine if it will rain tomorrow based off of the conditions of today.

''')

df = pd.read_csv('training_data.csv',index_col=[0])

st.write(
'''
## Datapoint Inputs

In this section, please enter the characteristics of the weather today
''')


dewpoint = st.number_input('Dew',value=1)
humidity = st.slider('Humidity',df['humidity'].min(),df['humidity'].max(),1.0)
