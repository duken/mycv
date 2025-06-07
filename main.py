import streamlit as st
from utils.data_cv import BIODATA, RINGKASAN

st.set_page_config(
    page_title=f"CV Digital {BIODATA['Nama']}",
    page_icon=":man_technologist:",
    layout="wide"
)

st.title(f"Curriculum Vitae — {BIODATA['Nama']}")
col1, col2 = st.columns([1, 2])

with col1:
    st.image("assets/foto.jpg", width=180, caption=BIODATA["Nama"])
with col2:
    st.markdown(f"""
    ### {BIODATA["Nama"]}
    - 📍 {BIODATA["Alamat"]}
    - 📧 {BIODATA["Kontak"]}
    - ☎️ {BIODATA["Telepon"]}
    - 🌐 [Website]({BIODATA["Website"]})
    """)
st.markdown("---")

st.subheader("Profil Singkat")
st.markdown(RINGKASAN)

st.markdown("---")
st.markdown("<center>CV Digital dibuat dengan Streamlit</center>", unsafe_allow_html=True)
