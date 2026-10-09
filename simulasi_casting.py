# ====================================================================
# SIMULASI 2: KONVERSI RAW DATA SENSOR (TYPE CASTING)
# ====================================================================

if __name__ == "__main__":
    print("--- MODUL PENERIMAAN DATA SERIAL ---")
    
    # Skenario: Data mentah dikirim alat pengukur Kuncup Roda (Side Slip) dalam format teks String
    raw_data_slip = "3.2"
    
    # Pembuktian Tipe Data Awal
    print("1. Menerima Data Mentah  :", raw_data_slip)
    print("   Tipe Data Saat Ini    :", type(raw_data_slip))
    
    # Melakukan eksekusi Type Casting (Konversi ke Float)
    print("\n[SISTEM SEDANG MENGONVERSI DATA...]")
    data_slip_aktual = float(raw_data_slip)
    
    # Pembuktian Tipe Data Setelah Konversi
    print("2. Data Setelah Konversi :", data_slip_aktual)
    print("   Tipe Data Terbaru     :", type(data_slip_aktual))
    
    # Pembuktian Matematis (Kalkulasi)
    print("\n3. Mengeksekusi Kalkulasi Batas Toleransi (+0.5):")
    hasil_kalkulasi = data_slip_aktual + 0.5
    print(f"   Hasil Akhir: {hasil_kalkulasi} meter/km")
    print("   [BERHASIL DIEKSEKUSI TANPA ERROR]")