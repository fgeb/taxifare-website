import streamlit as st
import geopy as gp
from geopy.geocoders import Nominatim

import requests
import pandas as pd
import numpy as np

'''
# Maps
'''

# url = 'https://taxifare.lewagon.ai/predict'
# res = requests.get(url)
# print(res.text)

location_query = st.text_input("Search for address", "")
geolocator = Nominatim(user_agent="streamlit-mapbox")

df = pd.DataFrame(
    [[52.51978, 13.40443]],
    columns=["lat", "lon"],
)
map = st.map(df)

if location_query:
    location = geolocator.geocode(location_query)

    if location:
        df = pd.DataFrame(
            [[location.latitude, location.longitude]],
            columns=["lat", "lon"],
        )
        map.map(df)
