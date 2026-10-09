# ==============================================================================
# ANATOMI PROGRAM: MODUL EVALUASI EMISI KENDARAAN (GAS ANALYZER)
# ==============================================================================

# --- 1. BLOK DEKLARASI PUSTAKA (IMPORTS) ---
import time
# (Di dunia nyata, pustaka 'serial' digunakan untuk menarik data alat secara langsung)

# --- 2. BLOK KONSTANTA GLOBAL (PARAMETER BAKU MUTU) ---
# Nilai batas yang ditetapkan pemerintah. Mudah diubah dengan metode Cari & Ganti
BATAS_MAKSIMAL_CO = 4.5    # Tipe: Float (Persen)
BATAS_MAKSIMAL_HC = 200    # Tipe: Integer (PPM)

# --- 3. BLOK DEFINISI FUNGSI MODULAR (SUB-ROUTINE) ---
def evaluasi_emisi_bensin(nilai_co_terukur, nilai_hc_terukur):
    """
    Fungsi ini membandingkan data aktual dengan baku mutu.
    Menerapkan logika perbandingan Boolean.
    """
    status_kelulusan = False
    
    if (nilai_co_terukur <= BATAS_MAKSIMAL_CO) and (nilai_hc_terukur <= BATAS_MAKSIMAL_HC):
        status_kelulusan = True
    else:
        status_kelulusan = False
        
    return status_kelulusan

# --- 4. BLOK EKSEKUSI UTAMA (MAIN EXECUTION) ---
if __name__ == "__main__":
    print("--- INISIALISASI SISTEM PEMBACAAN GAS ANALYZER ---")
    
    # Inisialisasi Variabel Identitas (Tipe String)
    plat_nomor = "DK 1782 AA"
    
    # Simulasi penerimaan data mentah dari alat ukur (biasanya masuk sebagai String)
    raw_data_co_dari_alat = "2.10"
    raw_data_hc_dari_alat = "180"
    
    # Eksekusi Type Casting (Konversi Tipe Data)
    aktual_co = float(raw_data_co_dari_alat)
    aktual_hc = int(raw_data_hc_dari_alat)
    
    # Memanggil Fungsi Modular dan menampung kembalian (Return) tipe Boolean
    hasil_uji = evaluasi_emisi_bensin(aktual_co, aktual_hc)
    
    print("Nomor Kendaraan  :", plat_nomor)
    print("Kadar CO Terukur :", aktual_co, "%")
    print("Kadar HC Terukur :", aktual_hc, "PPM")
    print("Status Kendaraan Lulus Emisi? :", hasil_uji)