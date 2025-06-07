import streamlit as st
from utils.data_cv import BIODATA, RINGKASAN

st.set_page_config(
    page_title=f"CV Digital {BIODATA['Nama']}",
    page_icon=":technologist:",
    layout="wide"
)

st.markdown(
    "<h1 style='color:#006D77;'>Curriculum Vitae &mdash; " + BIODATA['Nama'] + " 👨‍💻</h1>",
    unsafe_allow_html=True
)

col1, col2 = st.columns([1, 2])

with col1:
    st.image("assets/foto.jpg", width=180, caption=BIODATA["Nama"])
with col2:
    st.markdown(f"""
    <div style='font-size:20px;'>
    <b>📍 Alamat:</b> <span style='color:#006D77'>{BIODATA["Alamat"]}</span><br>
    <b>📧 Email:</b> <a href="mailto:{BIODATA["Kontak"]}">{BIODATA["Kontak"]}</a><br>
    <b>☎️ Telepon:</b> {BIODATA["Telepon"]}<br>
    <b>🌐 Website:</b> <a href="{BIODATA["Website"]}" style="color:#006D77">{BIODATA["Website"]}</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

st.subheader("📝 Profil Singkat")
st.info(RINGKASAN)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    "<center><span style='color:#006D77;'>CV Digital dibuat dengan Streamlit</span></center>",
    unsafe_allow_html=True
)
