# =====================================================================
# SIMULASI BLOK KODE DASAR: PROFIL IDENTIFIKASI KENDARAAN UJI
# =====================================================================

# --- DEKLARASI VARIABEL BERDASARKAN HIERARKI TIPE DATA ---

# 1. Deklarasi Data Identitas (Tipe: String)
no_uji_berkala = "KIR-B-2026-991"
nomor_polisi_kendaraan = "DK 1822 ZB"
nama_operator_uji = "Adrian Pradana"

# 2. Deklarasi Data Mutlak (Tipe: Integer)
tahun_produksi_unit = 2023
jumlah_sumbu_roda = 2
batas_baku_mutu_hc_ppm = 200

# 3. Deklarasi Data Sensor Presisi (Tipe: Float)
gaya_rem_utama_kiri_kn = 15.2
gaya_rem_utama_kanan_kn = 14.8
emisi_gas_buang_co_persen = 2.15

# 4. Deklarasi Status Interlock Keselamatan (Tipe: Boolean)
kendaraan_tepat_diatas_sensor = True
sistem_pembayaran_sah = True

# --- BLOK EKSEKUSI UTAMA (MENCETAK OUTPUT KE TERMINAL) ---
# Tanda pemisah untuk memperjelas visualisasi terminal
print("==================================================")
print("SISTEM TELEMATI PENGUJIAN KENDARAAN BERMOTOR (KIR)")
print("==================================================")

# Memanggil Variabel String
print("-> Profil Identitas Kendaraan:")
print("Nomor Register :", no_uji_berkala)
print("Plat Nomor     :", nomor_polisi_kendaraan)
print("Petugas Uji    :", nama_operator_uji)

print("\n-> Profil Spesifikasi Teknis:")
print("Tahun Rakit    :", tahun_produksi_unit)
print("Jumlah Sumbu   :", jumlah_sumbu_roda)

# Melakukan Kalkulasi Matematis Langsung menggunakan Variabel Float
print("\n-> Hasil Akuisisi Sensor Fisis:")
total_pengereman = gaya_rem_utama_kiri_kn + gaya_rem_utama_kanan_kn
print("Gaya Rem Kiri  :", gaya_rem_utama_kiri_kn, "kN")
print("Gaya Rem Kanan :", gaya_rem_utama_kanan_kn, "kN")
print("TOTAL GAYA REM :", total_pengereman, "kN")

print("\n-> Status Validasi Administrasi:")
print("Administrasi   :", sistem_pembayaran_sah)
print("==================================================")
print("STATUS: MENUNGGU INSTRUKSI LOGIKA BERIKUTNYA...")