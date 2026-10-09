# ====================================================================
# SIMULASI 1: INISIALISASI DATA KENDARAAN DAN PENGECEKAN TIPE DATA
# ====================================================================

# 1. Variabel Tipe Data String (Teks Karakter)
nomor_kendaraan = "DK 8812 AA"
kategori_uji = "Mobil Barang"

# 2. Variabel Tipe Data Integer (Bilangan Bulat)
berat_sumbu_depan_kg = 2500
berat_sumbu_belakang_kg = 3200

# 3. Variabel Tipe Data Float (Bilangan Desimal dari Sensor)
gaya_rem_kiri_kn = 12.50
gaya_rem_kanan_kn = 11.85

# 4. Variabel Tipe Data Boolean (Logika Aktuasi 1/0)
sensor_optik_aktif = True

# --- BLOK EKSEKUSI CETAK (OUTPUT TERMINAL) ---
if __name__ == "__main__":
    print("=" * 50)
    print("SISTEM PENGUJIAN KENDARAAN - POLTRADA BALI")
    print("=" * 50)
    
    print("\n[IDENTITAS KENDARAAN]")
    print(f"No. Polisi    : {nomor_kendaraan} -> Dideteksi sebagai: {type(nomor_kendaraan)}")
    print(f"Kategori      : {kategori_uji}")
    
    print("\n[PARAMETER FISIS KENDARAAN]")
    print(f"Beban Depan   : {berat_sumbu_depan_kg} Kg -> Dideteksi sebagai: {type(berat_sumbu_depan_kg)}")
    print(f"Gaya Rem Kiri : {gaya_rem_kiri_kn} kN -> Dideteksi sebagai: {type(gaya_rem_kiri_kn)}")
    
    print("\n[STATUS KESELAMATAN]")
    print(f"Sensor Optik  : {sensor_optik_aktif} -> Dideteksi sebagai: {type(sensor_optik_aktif)}")
    print("=" * 50)