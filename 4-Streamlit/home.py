import os

import base64
import requests

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Food-pairing",
    page_icon="🍷",
)

@st.cache_data
#@st.experimental_memo
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


def requette(donnees):
    response = requests.post(f"http://{os.environ['PREDICT_HOST']}/predict", json=donnees)
    return response.json()


img = get_img_as_base64("vin-page-1.jpeg")
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
background-position: bottom-center;
background-size: 100%;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stVerticalBlock"] {{
    height:Opx;
   
}}

</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown(f'''
<div style='margin-left: 40%; margin-top: 40%;'> 
            <div style='color: #db545a; font-size: 35px; font-weight: 700;letter-spacing: 1px; text-align: center; '>On boit quoi avec ça ?</div>
            <div style='text-align: center;font-style: italic; font-size: 24px;font-weight: 400;'>Vous choisissez le repas, <br>
Nous vous conseillons le vin !</div>
</div>

            ''', unsafe_allow_html=True,
            )

buff, col, buff2 = st.columns([1, 1, 3])


with buff2:
    if "my_input" not in st.session_state:
        st.session_state["my_input"] = "Mon plat"
        st.session_state["choix"] = "choix"

    my_input = st.text_input("")
    submit = st.button("Valider")
    st.session_state["choix"] = my_input
    json = {'plat': my_input}
    if submit:
        category = requette(json)

        st.session_state["my_input"] = category
