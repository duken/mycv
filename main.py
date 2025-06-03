# main.py
import streamlit as st
from utils.data_cv import BIODATA, RINGKASAN, PENDIDIKAN, PENGALAMAN_KERJA, PENGALAMAN_ORGANISASI, PELATIHAN, SKILL, PUBLIKASI

st.set_page_config(
    page_title=f"CV Digital {BIODATA['Nama']}",
    page_icon=":man_technologist:",
    layout="wide"
)

# --- HEADER: Foto dan Biodata ---
st.title(f"Curriculum Vitae {BIODATA['Nama']} :Portofolio 4:")
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

# --- Ringkasan Profil ---
st.subheader("Profil Singkat")
st.markdown(RINGKASAN)

# --- Pendidikan ---
st.subheader("🎓 Riwayat Pendidikan")
for edu in PENDIDIKAN:
    st.markdown(f"**{edu['Tahun']}** | {edu['Institusi']} | {edu['Jurusan']}")

# --- Pengalaman Kerja ---
st.subheader("💼 Pengalaman Kerja")
for kerja in PENGALAMAN_KERJA:
    st.markdown(f"**{kerja['Tahun']}** | {kerja['Posisi']} di {kerja['Perusahaan']}")
    if kerja["Deskripsi"]:
        st.caption(f"  {kerja['Deskripsi']}")

# --- Skill ---
st.subheader("🚀 Skill & Keahlian")
colA, colB = st.columns(2)
for idx, skill in enumerate(SKILL):
    if idx % 2 == 0:
        colA.markdown(f"- {skill}")
    else:
        colB.markdown(f"- {skill}")

# --- Publikasi ---
st.subheader("📑 Publikasi")
for pub in PUBLIKASI:
    st.markdown(f"- {pub}")

# --- Footer ---
st.markdown("---")
st.markdown("<center>© 2025 CV Digital Streamlit</center>", unsafe_allow_html=True)
