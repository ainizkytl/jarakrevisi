import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Fungsi untuk menghitung jarak
def hitung_jarak(kecepatan, waktu):
    return kecepatan * waktu

# Bagian utama aplikasi Streamlit
st.set_page_config(page_title="Kalkulator Jarak Interaktif", layout="centered")

st.title("🚀 Kalkulator Jarak Interaktif 🚀")

st.write("""
Hai! Mari kita jelajahi konsep **jarak**, **kecepatan**, dan **waktu** secara interaktif.
Geser slider di bawah untuk mengubah kecepatan dan waktu, lalu lihat bagaimana jaraknya berubah!
""")

# --- Input Pengguna ---
st.header("⚙️ Masukkan Data")
st.markdown("---")

# Menggunakan integer untuk slider agar output tidak ada koma
kecepatan = st.slider(
    "Pilih Kecepatan (km/jam):",
    min_value=1,
    max_value=100,
    value=10,
    step=1,
    help="Seberapa cepat kamu bergerak dalam satu jam."
)

waktu = st.slider(
    "Pilih Waktu Tempuh (jam):",
    min_value=1,
    max_value=10,
    value=2,
    step=1,
    help="Berapa lama kamu bergerak."
)

st.markdown("---")

# --- Perhitungan Jarak ---
st.header("📊 Hasil Perhitungan Jarak")

jarak_hasil = hitung_jarak(kecepatan, waktu)
# Format output jarak agar tidak ada angka di belakang koma
st.success(f"**Total Jarak yang Ditempuh: {jarak_hasil:.0f} km**")

st.write(f"Ini berarti, jika kamu bergerak dengan kecepatan **{kecepatan} km/jam** selama **{waktu} jam**,")
st.write(f"maka total jarak yang kamu tempuh adalah **{jarak_hasil:.0f} kilometer**.")


# --- Visualisasi Jarak ---
st.header("📈 Visualisasi Konsep Jarak")
st.write("""
Bayangkan setiap batang di grafik ini adalah jarak yang kamu tempuh dalam satu jam.
Tingginya menunjukkan kecepatanmu per jam, dan jumlah batangnya menunjukkan lamanya waktu.
""")

if waktu <= 0 or kecepatan <= 0:
    st.warning("Kecepatan dan waktu harus lebih besar dari nol untuk visualisasi yang meaningful.")
else:
    # Karena waktu sudah int dari slider, tidak perlu konversi lagi
    waktu_utuh = waktu

    jarak_per_unit_waktu = [kecepatan] * waktu_utuh
    labels = [f"Jam ke-{i+1}" for i in range(waktu_utuh)]

    fig, ax = plt.subplots(figsize=(9, 5))

    # Membuat bar chart
    bars = ax.bar(labels, jarak_per_unit_waktu, color='skyblue')

    # Menambahkan label pada setiap batang, format agar tidak ada desimal
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f'{yval:.0f} km', ha='center', va='bottom', fontsize=9)

    ax.set_xlabel("Waktu (Jam)", fontsize=11)
    ax.set_ylabel("Jarak yang Ditempuh per Jam (km)", fontsize=11)
    ax.set_title(f"Jarak Per Jam dengan Kecepatan {kecepatan} km/jam", fontsize=13)
    ax.set_ylim(0, kecepatan * 1.3) # Atur batas Y agar ada ruang di atas batang
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    st.pyplot(fig) # Tampilkan plot di Streamlit

st.markdown("---")
st.write("""
Bagaimana menurutmu? Apakah kamu bisa melihat bagaimana **kecepatan dikalikan dengan waktu** menghasilkan **jarak**?
Coba berbagai kombinasi kecepatan dan waktu untuk lebih memahami konsep ini!
""")
