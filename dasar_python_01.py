# ====================================================================
# SIMULASI 3: ARSITEKTUR KODE LENGKAP - UJI EMISI KENDARAAN
# ====================================================================

# --- 1. BLOK PUSTAKA (IMPORTS) ---
import time

# --- 2. BLOK KONSTANTA GLOBAL (PARAMETER BAKU MUTU) ---
# Parameter di bawah ini dapat diubah dengan mudah menggunakan fitur Cari & Ganti 
# jika regulasi daerah/nasional mengalami perubahan.
BATAS_CO_PERSEN = 4.5    # Ambang Karbon Monoksida (Float)
BATAS_HC_PPM = 200       # Ambang Hidrokarbon (Integer)

# --- 3. BLOK FUNGSI MODULAR (SUB-ROUTINE) ---
def proses_evaluasi_emisi(co_terukur, hc_terukur):
    # Logika boolean sederhana: Harus memenuhi KEDUA syarat batas
    if (co_terukur <= BATAS_CO_PERSEN) and (hc_terukur <= BATAS_HC_PPM):
        return True
    else:
        return False

# --- 4. BLOK EKSEKUSI UTAMA (ENTRY POINT) ---
if __name__ == "__main__":
    print("=" * 45)
    print("    INTEGRASI SISTEM UJI EMISI GAS BUANG")
    print("=" * 45)
    
    # 4.1 Inisialisasi Data
    plat_nomor = "DK 4055 XD"
    data_co_alat = 2.10    # (Float) Dalam batas normal
    data_hc_alat = 250     # (Integer) Nilai melebihi ambang (Gagal)
    
    print(f"Menganalisis Kendaraan: {plat_nomor}")
    print("Mengambil data sensor...")
    time.sleep(1.5) # Simulasi delay pembacaan sensor selama 1.5 detik
    
    # 4.2 Pemanggilan Fungsi Penilai (Modular Call)
    status_kelulusan = proses_evaluasi_emisi(data_co_alat, data_hc_alat)
    
    # 4.3 Cetak Hasil Visual di Terminal
    print("\n[HASIL PEMBACAAN ALAT UKUR]")
    print(f"-> Kadar CO: {data_co_alat} %  (Batas Maks: {BATAS_CO_PERSEN} %)")
    print(f"-> Kadar HC: {data_hc_alat} PPM (Batas Maks: {BATAS_HC_PPM} PPM)")
    
    print("\n[KEPUTUSAN AKHIR SISTEM]")
    if status_kelulusan == True:
        print(">> STATUS: KENDARAAN LULUS UJI EMISI <<")
    else:
        print(">> STATUS: KENDARAAN GAGAL UJI EMISI <<")
    print("=" * 45)