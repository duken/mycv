import streamlit as st
from utils.data_cv import PENDIDIKAN

st.markdown("<h2 style='color:#006D77;'>🎓 Riwayat Pendidikan</h2>", unsafe_allow_html=True)
for edu in PENDIDIKAN:
    st.markdown(f"<span style='color:#22223B; font-size:17px;'><b>{edu['Tahun']}</b> | {edu['Institusi']} <i>{edu['Jurusan']}</i></span>", unsafe_allow_html=True)
