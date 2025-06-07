import streamlit as st
from utils.data_cv import PUBLIKASI

st.markdown("<h2 style='color:#006D77;'>📑 Publikasi & Karya Tulis</h2>", unsafe_allow_html=True)
for pub in PUBLIKASI:
    st.markdown(f"<span style='color:#22223B'>• {pub}</span>", unsafe_allow_html=True)
