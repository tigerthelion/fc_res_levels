import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import requests
import json
latest_date = "2000-01-01"


def save_data(data):
    pass

def fetch_data():
    r = requests.get("https://apps.larimer.org/api/water-levels/?prop=htr")
    df = pd.read_json(json.dumps(r.json()['records']))
    df.to_json('data.json')
    # st.write(f"New data fetched up to {latest_date}")
    # save_data(data)

def load_data():
    try:
         return pd.read_json('data.json')

    except FileNotFoundError as e:
        st.write("No file found ... fetching data")
        

if st.button("Load New Data","load_data", "Calls API and loads fresh data into graph"):
    fetch_data()
    df = load_data()
else:
    df = load_data()

    
# st.write(df)
# st.write()


# convert level to number and filter junk data
df['level'] = pd.to_numeric(df['level'], errors='coerce')
print(df.dtypes)
print(df.describe())
df = df[df['level'] >=0]
st.write(df.describe())

fig = plt.figure()
plt.plot(df['date'], df['level'])
st.pyplot(fig)
# plt.plot(df['date'], df['level'])
# plt.show()
# st.pyplot()
