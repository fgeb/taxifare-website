import streamlit as st
import requests
import pandas as pd
import numpy as np

'''
# TaxiFareModel Predict 🚕 💶
'''

# url = 'https://taxifare.lewagon.ai/predict'
# res = requests.get(url)
# print(res.text)

df = pd.DataFrame(
    [[52.50465, 13.28397]],
    columns=["lat", "lon"],
)
st.map(df)

# st.map(
#     latitude=52.50465,
#     #latitude=13.28397
# )

#st.map(data=None, *, latitude=None, longitude=None, color=None, size=None, zoom=None, use_container_width=True, width=None, height=None)
