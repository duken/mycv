import streamlit as st
from utils.data_cv import BIODATA, RINGKASAN

st.markdown("<h2 style='color:#006D77;'>👤 Profil Singkat</h2>", unsafe_allow_html=True)
st.markdown(f"""
<b>Nama:</b> <span style='color:#006D77'>{BIODATA['Nama']}</span><br>
<b>Alamat:</b> {BIODATA['Alamat']}<br>
<b>Email:</b> <a href="mailto:{BIODATA["Kontak"]}">{BIODATA["Kontak"]}</a><br>
<b>Telepon:</b> {BIODATA['Telepon']}<br>
<b>Website:</b> <a href="{BIODATA['Website']}" style="color:#006D77">{BIODATA['Website']}</a>
""", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)
st.success(RINGKASAN)
