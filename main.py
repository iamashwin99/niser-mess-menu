import streamlit as st
import os
import pandas as pd
from datetime import datetime
import json
import random
import requests as re
# import plotly.express as px 
# import plotly.graph_objects as go
st.set_page_config("NISER Mess Menu","🍲","wide","collapsed")
from st_material_table import st_material_table
headerColor = 'grey'
rowEvenColor = 'lightgrey'
rowOddColor = 'white'

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSpgPFjsVbVak8MuXxOYEV8ezmsXC38Ki13xHcGwVt3YbFRoRSKwiRemMk9lCGOKRsDCrlYtD2ePg7V/pub?output=csv"
df = pd.read_csv(url)

st.write("# NISER Mess Menu:")

_ = st_material_table(df)

