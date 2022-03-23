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


dewpoint = st.slider('Dewpoint',df['dew'].min(),df['dew'].max(),1.0)
humidity = st.slider('Humidity',df['humidity'].min(),df['humidity'].max(),1.0)
precipitation = st.slider('Precipitation',df['precip'].min(),df['precip'].max(),1.0)
snow = st.slider('Snow',df['snow'].min(),df['snow'].max(),1.0)
snow_depth = st.slider('Snow Depth',df['snowdepth'].min(),df['snowdepth'].max(),1.0)
wind_gust = st.slider('Wind Gust',df['windgust'].min(),df['windgust'].max(),1.0)
wind_speed = st.slider('Wind Speed',df['windspeed'].min(),df['windspeed'].max(),1.0)
wind_dir = st.slider('Wind Direction',df['winddir'].min(),df['winddir'].max(),1.0)
sealevel = st.slider('Sea Level Pressure',df['sealevelpressure'].min(),df['sealevelpressure'].max(),1.0)
cloudcover = st.slider('Cloud Cover',df['cloudcover'].min(),df['cloudcover'].max(),1.0)
visibility = st.slider('Visibility',df['visibility'].min(),df['visibility'].max(),1.0)
solar_radiation = st.slider('Solar Radiation',df['solarradiation'].min(),df['solarradiation'].max(),1.0)
solar_energy = st.slider('Solar Energy',df['solarenergy'].min(),df['solarenergy'].max(),1.0)
UV = st.slider('UV Index',df['uvindex'].min(),df['uvindex'].max(),1)
moonphase = st.slider('MoonPhase',df['moonphase'].min(),df['moonphase'].max(),.1)
conditions = st.text_input('Conditions (seperate each condition with a comma',value='')
feels_like = st.checkbox('Is it warmer than expected')
if feels_like:
    feels_like_value = 1
else:
    feels_like_value = 0
big_range = st.checkbox('Did the temp vary greatly today?')
if big_range:
    big_range_value = 1
else:
    big_range_value = 0

raining = st.checkbox('Did it rain most of today?')
if raining:
    raining_value = 1
else:
    raining_value = 0
sunset = 1151
sunrise = 417
