import streamlit as st

st.title("Kontak Saya")
st.write("Hubungi saya melalui form berikut atau media sosial.")

with st.form("form_kontak"):
    nama = st.text_input("Nama")
    email = st.text_input("Email")
    pesan = st.text_area("Pesan")
    submit = st.form_submit_button("Kirim")
    if submit:
        st.success("Terima kasih, pesan Anda telah dikirim!")

st.markdown("""
- Email: duken.holland@email.com
- LinkedIn: [Duken Holland](https://linkedin.com/in/dukenholland)
""")
