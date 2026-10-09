# -----------------------------------------------------
# SIMULASI DASAR: MEMBUAT PROFIL KENDARAAN UJI
# -----------------------------------------------------

# 1. Mengisi Variabel dengan Tipe Data STRING
nomor_identitas = "DK 1555 TE"
nama_pemilik = "Bapak Wayan"

# 2. Mengisi Variabel dengan Tipe Data INTEGER
tahun_produksi = 2021
batas_usia_uji_tahun = 10

# 3. Mengisi Variabel dengan Tipe Data FLOAT
gaya_rem_kiri = 14.5 
gaya_rem_kanan = 14.2

# 4. Mengisi Variabel dengan Tipe Data BOOLEAN
status_pembayaran_sah = True

# -----------------------------------------------------
# MEMERINTAHKAN MESIN BERBICARA (MENCETAK OUTPUT)
# -----------------------------------------------------
print("========================================")
print("SISTEM PENGUJIAN KENDARAAN POLTRADA BALI")
print("========================================")

# Mesin mencetak isi dari variabel yang kita panggil
print("Menampilkan Profil Kendaraan:")
print("Plat Nomor :", nomor_identitas)
print("Nama       :", nama_pemilik)
print("Tahun Buat :", tahun_produksi)

# Kita juga bisa menjumlahkan variabel numerik langsung di dalam perintah cetak
total_gaya_rem = gaya_rem_kiri + gaya_rem_kanan
print("Total Pengereman (kN) :", total_gaya_rem)

print("Status Retribusi Lunas?", status_pembayaran_sah)