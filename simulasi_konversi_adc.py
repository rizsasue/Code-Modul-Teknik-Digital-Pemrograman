# =====================================================================
# SIMULASI BLOK KODE: ALGORITMA KONVERSI ANALOG TO DIGITAL (ADC)
# STUDI KASUS: KALIBRASI SENSOR AXLE LOAD TESTER 
# =====================================================================

def proses_konversi_adc_ke_fisis(nilai_adc_mentah):
    # -----------------------------------------------------------------
    # BLOK 1: INISIALISASI SPESIFIKASI PERANGKAT KERAS (KONSTANTA)
    # -----------------------------------------------------------------
    RESOLUSI_ADC_BIT = 10
    NILAI_ADC_MAKSIMAL = (2 ** RESOLUSI_ADC_BIT) - 1  # 2^10 - 1 = 1023
    
    TEGANGAN_REFERENSI_V = 5.0    # Voltase operasi mikrokontroler
    KAPASITAS_SENSOR_KG = 10000.0 # Kapasitas maksimal Load Cell (10 Ton)
    
    # Menghitung koefisien linear (Rasio Kg per Volt)
    konstanta_kalibrasi = KAPASITAS_SENSOR_KG / TEGANGAN_REFERENSI_V

    print("[SISTEM] Memulai proses transformasi sinyal digital...")
    
    # -----------------------------------------------------------------
    # BLOK 2: KALKULASI TAHAP 1 (MENCARI NILAI TEGANGAN AKTUAL)
    # -----------------------------------------------------------------
    # Rumus: (Nilai ADC Terbaca / ADC Maksimal) * VRef
    tegangan_sensor_v = (nilai_adc_mentah / NILAI_ADC_MAKSIMAL) * TEGANGAN_REFERENSI_V
    
    # -----------------------------------------------------------------
    # BLOK 3: KALKULASI TAHAP 2 (MENCARI BESARAN FISIS ABSOLUT)
    # -----------------------------------------------------------------
    # Rumus: Tegangan Terukur * Konstanta Rasio
    berat_aktual_kendaraan = tegangan_sensor_v * konstanta_kalibrasi
    
    # -----------------------------------------------------------------
    # BLOK 4: PENGEMBALIAN NILAI (RETURN DATA)
    # -----------------------------------------------------------------
    # Mengembalikan nilai dalam struktur List majemuk untuk keperluan log
    return [tegangan_sensor_v, berat_aktual_kendaraan]


# =====================================================================
# EKSEKUSI UTAMA (MAIN ROUTINE)
# =====================================================================
if __name__ == "__main__":
    print("==================================================")
    print(" MODUL KALIBRASI INSTRUMENTASI AXLE LOAD (SIMULASI)")
    print("==================================================")
    
    # Simulasi penerimaan data serial dari Mikrokontroler (Angka Diskrit)
    # Nilai ini harus selalu berada pada rentang 0 hingga 1023
    raw_data_adc = 380
    
    # Validasi Error Handling terhadap batasan kapabilitas perangkat keras
    if raw_data_adc < 0 or raw_data_adc > 1023:
        print("[ERROR] Nilai ADC di luar jangkauan spesifikasi 10-bit!")
    else:
        # Pemanggilan fungsi dan injeksi parameter
        hasil_komputasi = proses_konversi_adc_ke_fisis(raw_data_adc)
        
        # Ekstraksi hasil kembalian (return list)
        nilai_voltase = hasil_komputasi[0]
        nilai_berat_kg = hasil_komputasi[1]
        
        # Pencetakan laporan hasil kalibrasi
        print("\n[LAPORAN DIAGNOSTIK HARDWARE]")
        print(f"Data Digital ADC Diterima : {raw_data_adc} (Resolusi 10-bit)")
        # round(..., 3) digunakan untuk menampilkan 3 digit presisi di belakang koma
        print(f"Konversi Tegangan Sinyal  : {round(nilai_voltase, 3)} Volt DC")
        print(f"Konversi Parameter Fisis  : {round(nilai_berat_kg, 2)} Kilogram")
    
    print("==================================================")