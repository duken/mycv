import streamlit as st

st.markdown("<h2 style='color:#006D77;'>🛠️ Portofolio Proyek</h2>", unsafe_allow_html=True)
st.write("Berikut beberapa proyek yang pernah saya kerjakan:")

# Contoh data portofolio, silakan ganti/isi sesuai proyek Anda sendiri
portfolio = [
    {
        "judul": "Si-PiTUNG",
        "deskripsi": "Aplikasi peLaporan dan Realiasi Pembayaran Tunjangan Guru",
        "link": "https://si-pitung.id"
    },
    {
        "judul": "Dashboard GTK",
        "deskripsi": "Dashboard Guru dan Tenaga Kependidikan Kab. Gorontalo Utara.",
        "link": "https://dagu.smart-x.id"
    },

]

# Tampilkan portofolio dalam format card (kolom dua)
for i, proj in enumerate(portfolio):
    if i % 2 == 0:
        cols = st.columns(2)
    idx = i % 2
    with cols[idx]:
        st.markdown(f"""
        <div style="background-color:#A7C957; padding:18px 15px 10px 15px; border-radius:18px; margin-bottom:18px;">
            <h4 style="color:#22223B; margin-bottom:5px;">{proj['judul']}</h4>
            <p style="color:#22223B;">{proj['deskripsi']}</p>
            <a href="{proj['link']}" style="color:#006D77;" target="_blank">🔗 Lihat proyek</a>
        </div>
        """, unsafe_allow_html=True)
