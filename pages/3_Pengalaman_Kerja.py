import streamlit as st
from utils.data_cv import PENGALAMAN_KERJA

st.title("Pengalaman Kerja")
for kerja in PENGALAMAN_KERJA:
    st.markdown(f"**{kerja['Tahun']}** | {kerja['Posisi']} di {kerja['Perusahaan']}")
    if kerja["Deskripsi"]:
        st.caption(f"  {kerja['Deskripsi']}")
