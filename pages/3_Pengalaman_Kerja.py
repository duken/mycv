import streamlit as st
from utils.data_cv import PENGALAMAN_KERJA

st.markdown("<h2 style='color:#006D77;'>💼 Pengalaman Kerja</h2>", unsafe_allow_html=True)
for kerja in PENGALAMAN_KERJA:
    st.markdown(
        f"<span style='color:#22223B; font-size:17px;'><b>{kerja['Tahun']}</b> | {kerja['Posisi']} di <b>{kerja['Perusahaan']}</b></span>",
        unsafe_allow_html=True
    )
    if kerja["Deskripsi"]:
        st.caption(f"📝 {kerja['Deskripsi']}")
