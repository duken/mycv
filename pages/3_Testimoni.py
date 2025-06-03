import streamlit as st

st.title("Testimoni & Rekomendasi")
st.write("Beberapa testimoni dari rekan dan atasan:")

testimoni = [
    {
        "nama": "Budi Santoso",
        "posisi": "Manager PT. Inovasi Digital",
        "pesan": "Duken adalah programmer yang sangat berdedikasi dan cepat belajar."
    },
    {
        "nama": "Siti Rahma",
        "posisi": "Dosen Pembimbing",
        "pesan": "Kreatif dan selalu mencari solusi baru, sangat direkomendasikan."
    }
]

for t in testimoni:
    st.markdown(f"""
    > "{t['pesan']}"
    **- {t['nama']}, {t['posisi']}**
    """)
