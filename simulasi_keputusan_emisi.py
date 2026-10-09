# =====================================================================
# SIMULASI BLOK KODE: STRUKTUR PERCABANGAN BERSARANG (NESTED IF)
# STUDI KASUS: EVALUASI BAKU MUTU EMISI KENDARAAN BERMOTOR
# =====================================================================

if __name__ == "__main__":
    print("==================================================")
    print(" SISTEM EVALUASI EMISI MULTI-KRITERIA (SIMULASI)")
    print("==================================================")

    # --- 1. INISIALISASI PROFIL KENDARAAN (UBAH VARIABEL INI) ---
    jenis_bahan_bakar = "Bensin"   # Pilihan: "Bensin" atau "Solar"
    tahun_perakitan = 2010         # Tahun kendaraan
    
    # Data dari Sensor
    emisi_co_terukur = 1.2         # Karbon Monoksida (%) untuk Bensin
    opasitas_terukur = 35.0        # Ketebalan Asap (%) untuk Solar

    # Variabel Kontainer untuk Laporan Akhir
    status_lulus = False
    ambang_batas = 0.0

    print(f"Menganalisis Kendaraan : {jenis_bahan_bakar} | Tahun: {tahun_perakitan}")
    
    # --- 2. PERCABANGAN UTAMA (LAPIS PERTAMA) ---
    if jenis_bahan_bakar == "Bensin":
        print("[INFO] Mengaktifkan Modul Evaluasi Mesin Otto (Gasoline).")
        
        # --- PERCABANGAN BERSARANG (LAPIS KEDUA - KHUSUS BENSIN) ---
        if tahun_perakitan < 2007:
            # Baku mutu kendaraan lama lebih longgar
            ambang_batas = 4.5
            print(f"-> Regulasi < 2007. Ambang Maksimal CO: {ambang_batas} %")
        else:
            # Baku mutu kendaraan baru lebih ketat
            ambang_batas = 1.5
            print(f"-> Regulasi >= 2007. Ambang Maksimal CO: {ambang_batas} %")
            
        # Evaluasi Kelulusan menggunakan Operator Komparasi
        if emisi_co_terukur <= ambang_batas:
            status_lulus = True
            
    elif jenis_bahan_bakar == "Solar":
        print("[INFO] Mengaktifkan Modul Evaluasi Mesin Diesel (Opasitas).")
        
        # --- PERCABANGAN BERSARANG (LAPIS KEDUA - KHUSUS SOLAR) ---
        if tahun_perakitan < 2010:
            ambang_batas = 70.0
            print(f"-> Regulasi < 2010. Ambang Maksimal Asap: {ambang_batas} %")
        else:
            ambang_batas = 40.0
            print(f"-> Regulasi >= 2010. Ambang Maksimal Asap: {ambang_batas} %")
            
        # Evaluasi Kelulusan Opasitas
        if opasitas_terukur <= ambang_batas:
            status_lulus = True
            
    else:
        # Menangani anomali jika operator salah memasukkan tipe bahan bakar
        print("[ERROR FATAL] Tipe bahan bakar tidak valid pada database!")

    # --- 3. MENCETAK KESIMPULAN LOGIKA FINAL ---
    print("\n[KEPUTUSAN LOGIKA FINAL]")
    if status_lulus == True:
        print(">>> STATUS: SERTIFIKAT LAIK JALAN DITERBITKAN <<<")
    else:
        print(">>> STATUS: KENDARAAN DITOLAK (EMISI MELEBIHI BAKU MUTU) <<<")
    print("==================================================")