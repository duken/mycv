import streamlit as st
from utils.data_cv import PUBLIKASI

st.title("Publikasi & Karya Tulis")
for pub in PUBLIKASI:
    st.markdown(f"- {pub}")
