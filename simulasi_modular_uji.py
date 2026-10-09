# =====================================================================
# SIMULASI BLOK KODE: IMPLEMENTASI FUNGSI DAN MODULARITAS (DRY)
# STUDI KASUS: SISTEM MANAJEMEN PENGUJIAN KENDARAAN (KIR)
# =====================================================================

# ---------------------------------------------------------------------
# BLOK 1: PUSTAKA DAN KONSTANTA GLOBAL (Baku Mutu)
# ---------------------------------------------------------------------
BATAS_EFISIENSI_REM = 50.0
BATAS_CO_PERSEN = 4.5

# ---------------------------------------------------------------------
# BLOK 2: DEFINISI FUNGSI MODULAR (SUB-SISTEM INDEPENDEN)
# ---------------------------------------------------------------------

# Fungsi 1: Modul Kalkulasi Rem
# Menerima 2 parameter masukan, mengembalikan 1 nilai boolean keluar
def modul_evaluasi_rem(gaya_kiri_kg, gaya_kanan_kg, berat_sumbu_kg):
    # Logika terisolasi (Lokal)
    total_gaya = gaya_kiri_kg + gaya_kanan_kg
    efisiensi = (total_gaya / berat_sumbu_kg) * 100
    
    # Pengkondisian kelulusan
    if efisiensi >= BATAS_EFISIENSI_REM:
        return True
    else:
        return False

# Fungsi 2: Modul Kalkulasi Emisi Gas Buang
# Menerima 1 parameter, mengembalikan string status
def modul_evaluasi_emisi(kadar_co_terukur):
    if kadar_co_terukur <= BATAS_CO_PERSEN:
        return "LULUS"
    else:
        return "GAGAL"

# ---------------------------------------------------------------------
# BLOK 3: EKSEKUSI UTAMA (MAIN LOOP / SISTEM SENTRAL)
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("==================================================")
    print(" SISTEM PENGUJIAN MODULAR POLTRADA BALI")
    print("==================================================")
    
    # Simulasi data yang ditangkap dari antarmuka sensor / operator
    data_berat = 2000
    data_rem_kiri = 550
    data_rem_kanan = 520
    data_gas_co = 3.2
    
    print("[SISTEM] Menghubungi Modul Uji Rem...")
    # Memanggil fungsi 1, menyuntikkan Argumen, dan menampung hasil 'return'
    status_rem = modul_evaluasi_rem(data_rem_kiri, data_rem_kanan, data_berat)
    
    print("[SISTEM] Menghubungi Modul Uji Emisi...")
    # Memanggil fungsi 2, menyuntikkan Argumen, dan menampung hasil 'return'
    status_emisi = modul_evaluasi_emisi(data_gas_co)
    
    # Mengeksekusi Laporan Akhir berdasarkan penggabungan kedua modul
    print("\n================HASIL AKHIR======================")
    print(f"Status Komponen Rem   : {status_rem}")
    print(f"Status Komponen Emisi : {status_emisi}")
    
    # Syarat mutlak laik jalan
    if (status_rem == True) and (status_emisi == "LULUS"):
        print(">>> KESIMPULAN: KENDARAAN LAIK JALAN <<<")
    else:
        print(">>> KESIMPULAN: KENDARAAN TIDAK LAIK JALAN <<<")
    print("==================================================")