import streamlit as st
from utils.data_cv import SKILL

st.title("Keahlian dan Skill")
colA, colB = st.columns(2)
for idx, skill in enumerate(SKILL):
    if idx % 2 == 0:
        colA.markdown(f"- {skill}")
    else:
        colB.markdown(f"- {skill}")
