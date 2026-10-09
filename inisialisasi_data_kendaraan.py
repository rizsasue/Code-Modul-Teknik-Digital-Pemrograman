# =======================================================
# MODUL INISIALISASI DATA KENDARAAN (PROFIL UJI)
# =======================================================

# 1. Variabel Identifikasi (Tipe Data: String)
no_pendaftaran_uji = "KIR-26-08001"
nomor_kendaraan = "DK 8812 AA"
kategori_kendaraan = "Mobil Penumpang"

# 2. Variabel Parameter Fisis Statis (Tipe Data: Integer)
# Pastikan memperbarui nilai ini dengan metode Cari dan Ganti jika objek uji berubah
berat_sumbu_depan_kg = 1200
berat_sumbu_belakang_kg = 850

# 3. Variabel Parameter Pembacaan Sensor (Tipe Data: Float)
gaya_rem_utama_kiri_kn = 4.25
gaya_rem_utama_kanan_kn = 4.10
emisi_hidrokarbon_ppm = 150.5

# 4. Variabel Status Logika Sistem (Tipe Data: Boolean)
sensor_optik_aktif = True
kendaraan_siap_diuji = True

# -------------------------------------------------------
# Menampilkan Ringkasan Tipe Data ke Layar Monitor (Terminal)
# -------------------------------------------------------
print("==== STATUS KONEKSI SISTEM UJI ====")
print("Nomor Kendaraan:", nomor_kendaraan, "| Tipe Data:", type(nomor_kendaraan))
print("Total Beban Sumbu Depan:", berat_sumbu_depan_kg, "| Tipe Data:", type(berat_sumbu_depan_kg))
print("Kekuatan Rem Kiri:", gaya_rem_utama_kiri_kn, "| Tipe Data:", type(gaya_rem_utama_kiri_kn))
print("Status Optik Roller:", sensor_optik_aktif, "| Tipe Data:", type(sensor_optik_aktif))