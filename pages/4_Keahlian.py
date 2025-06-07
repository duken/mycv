import streamlit as st
from utils.data_cv import SKILL

st.markdown("<h2 style='color:#006D77;'>🚀 Keahlian & Skill</h2>", unsafe_allow_html=True)
colA, colB = st.columns(2)
for idx, skill in enumerate(SKILL):
    if idx % 2 == 0:
        colA.markdown(f"<span style='color:#A7C957'>✅ {skill}</span>", unsafe_allow_html=True)
    else:
        colB.markdown(f"<span style='color:#A7C957'>✅ {skill}</span>", unsafe_allow_html=True)
