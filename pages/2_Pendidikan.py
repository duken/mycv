import streamlit as st
from utils.data_cv import PENDIDIKAN

st.title("Riwayat Pendidikan")
for edu in PENDIDIKAN:
    st.markdown(f"**{edu['Tahun']}** | {edu['Institusi']} {edu['Jurusan']}")
