import streamlit as st
import requests
from key import key

api_key = st.secrets["API_KEY"]

# Get astro image of the day
response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={api_key}")
content = response.json()

#get EPIC data
response2 = requests.get(f"https://api.nasa.gov/EPIC/api/natural/images?api_key={api_key}")
content2 = response2.json()

parse_content2 = content2[:1]

df = {}

for contents in parse_content2:
    df.update(contents)

date = df["date"]
date, time = date.split(" ")
parsed_date = date.replace("-","/")

epic_img = df["image"]

title = content["title"]


st.set_page_config(layout="wide")


col1, col2, col3 = st.columns([.3,.4,.3])
with col2:
    st.title(f":orange[Astronomy Picture Of The Day]")
    st.header(f"Date: {content['date']}")
    st.header(f":blue[{title}]")

col4, col5, col6 = st.columns([.1, .8, .1])
with col5:
    st.image(content["hdurl"])
    st.info(content["explanation"])
    st.header(f":blue[{df['caption']} on {parsed_date}]")
    st.image(f"https://epic.gsfc.nasa.gov/archive/natural/{parsed_date}/jpg/{epic_img}.jpg")