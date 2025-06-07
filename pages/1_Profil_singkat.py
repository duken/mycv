import streamlit as st
from utils.data_cv import BIODATA, RINGKASAN

st.title("Profil Singkat")
st.markdown(f"""
#### Nama: {BIODATA['Nama']}
- Alamat: {BIODATA['Alamat']}
- Email: {BIODATA['Kontak']}
- Telepon: {BIODATA['Telepon']}
- Website: [Klik di sini]({BIODATA['Website']})
""")
st.markdown("---")
st.markdown(RINGKASAN)
