# app.py
import streamlit as st
from model import Kandidat
from voting_manager import VotingManager

# Inisialisasi Voting Manager
voting_manager = VotingManager()

# Setup kandidat list
if "daftar_kandidat" not in st.session_state:
    st.session_state.daftar_kandidat = []

# Theme & Style
st.set_page_config(page_title="Vote Ketua Kelas", layout="centered")
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 8px 20px;
    }
    .stRadio>div {
        padding: 10px 0;
    }
    .stTextInput>div>input {
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🗳️ Vote Ketua Kelas")

# -------- Tambah Kandidat --------
with st.expander("➕ Tambah Kandidat"):
    kandidat_baru = st.text_input("Nama Kandidat Baru", key="input_kandidat")

    if st.button("Tambah Kandidat"):
        if kandidat_baru.strip() == "":
            st.warning("Nama kandidat tidak boleh kosong!")
        elif kandidat_baru in st.session_state.daftar_kandidat:
            st.warning("Kandidat sudah ada.")
        else:
            st.session_state.daftar_kandidat.append(kandidat_baru)
            st.success(f"Kandidat '{kandidat_baru}' berhasil ditambahkan.")

# -------- Edit Kandidat --------
if st.session_state.daftar_kandidat:
    st.subheader("✏️ Ubah Kandidat")
    col1, col2, col3 = st.columns([2, 2, 1])
    with col1:
        kandidat_dipilih = st.selectbox("Pilih Kandidat", st.session_state.daftar_kandidat, key="edit_pilih")
    with col2:
        kandidat_baru = st.text_input("Nama Baru", key="edit_nama_baru")
    with col3:
        if st.button("Ubah"):
            if kandidat_baru.strip() == "":
                st.warning("Nama baru tidak boleh kosong.")
            elif kandidat_baru in st.session_state.daftar_kandidat:
                st.warning("Nama tersebut sudah digunakan.")
            else:
                idx = st.session_state.daftar_kandidat.index(kandidat_dipilih)
                st.session_state.daftar_kandidat[idx] = kandidat_baru
                st.success(f"'{kandidat_dipilih}' diubah menjadi '{kandidat_baru}'")

st.markdown("---")

# -------- Form Voting --------
st.header("📋 Form Pemilihan")
nama_pemilih = st.text_input("Nama Anda")

if not st.session_state.daftar_kandidat:
    st.warning("Belum ada kandidat yang tersedia.")
else:
    pilihan = st.radio("Pilih Ketua Kelas:", st.session_state.daftar_kandidat)
    if st.button("Kirim Suara"):
        if nama_pemilih.strip() == "":
            st.warning("Masukkan nama Anda terlebih dahulu!")
        else:
            success, message = voting_manager.submit_vote(nama_pemilih, pilihan)
            if success:
                st.success(message)
            else:
                st.error(message)

# -------- Hasil Voting --------
with st.expander("📊 Lihat Hasil Voting"):
    hasil = voting_manager.get_hasil()
    if hasil:
        for nama, jumlah in hasil:
            st.write(f"📊 {nama}: {jumlah} suara")
        st.bar_chart(dict(hasil))
    else:
        st.info("Belum ada suara yang masuk.")

# -------- Reset Voting --------
with st.expander("⚠️ Admin: Reset Voting"):
    if st.button("Hapus Semua Suara"):
        voting_manager.reset_voting()
        st.success("Semua suara telah dihapus.")
