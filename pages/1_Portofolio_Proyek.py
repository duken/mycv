import streamlit as st

st.title("Portofolio Proyek")
st.write("Berikut adalah beberapa proyek yang pernah saya kerjakan:")

projects = [
    {
        "judul": "Aplikasi Monitoring IoT",
        "deskripsi": "Sistem monitoring suhu dan kelembapan real-time untuk tambak ikan.",
        "link": "https://github.com/duken/monitoring-iot"
    },
    {
        "judul": "Dashboard Data Guru",
        "deskripsi": "Dashboard web interaktif untuk visualisasi data guru di Kabupaten Gorontalo Utara.",
        "link": "https://dagu.smart-x.id"
    }
]

for proj in projects:
    st.markdown(f"""
    #### {proj['judul']}
    {proj['deskripsi']}
    [Lihat Proyek]({proj['link']})
    """)
