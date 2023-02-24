import base64
import requests

import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

DATA = "https://data-vins.s3.amazonaws.com/vins.csv"


#@st.experimental_memo
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


@st.cache_data
def load_data():
    df = pd.read_csv(DATA, sep=";")
    return df


data_load_state = st.text('Loading data...')
df = load_data()
data_load_state.text("")

st.markdown(
    f"""<h2 style="text-align: center; color: black;">Votre plat est {st.session_state["choix"] } , 
    nous l'avons classifié dans {st.session_state["my_input"]}</h2>""", unsafe_allow_html=True)


def get_data(category):
    newdf = df.loc[df['target'] == category]
    return newdf[['vin', 'type', 'region']]


def App1page():
    st.write("hello world")


img = get_img_as_base64("vin-page-2.jpeg")
logo = get_img_as_base64("logo.png")

page_bg_img = f"""
<style>
 [data-testid="stSidebarNav"] {{
                background-image: url("data:image/png;base64,{logo}");
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 10px 10px;
                background-size: 200px 200px;
            }}

[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img}");
background-position: left;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid=stDataFrameResizable]{{
    margin-top: 20%;
    margin-left: 88%;
    
}}

</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.write(

    f'''
<div style='margin-left: 40%; margin-top: 10%;'> 
<div style='color: #db545a; font-size: 25px; font-weight: 700;letter-spacing: 1px; text-align: right; '>NOTRE SÉLECTION POUR VOUS</div>
            
</div>

            ''', unsafe_allow_html=True,
)

result = get_data(st.session_state["my_input"])

st.dataframe(result)
