# =====================================================================
# SIMULASI BLOK KODE: EVALUASI EFISIENSI REM & PENYIMPANGAN SUMBU (KIR)
# =====================================================================

if __name__ == "__main__":
    print("==================================================")
    print("  SISTEM ANALISIS BRAKE TESTER AKTIF (SIMULASI)")
    print("==================================================")

    # --- 1. INISIALISASI BAKU MUTU (KONSTANTA REGULASI) ---
    # Ruang memori absolut yang tidak boleh dimodifikasi oleh sembarang fungsi
    BATAS_EFISIENSI_MINIMAL = 50.0  # Persentase minimal laik jalan
    BATAS_SELISIH_MAKSIMAL = 8.0    # Persentase deviasi maksimal (batas agar tidak narik ke satu sisi)
    
    # --- 2. ABSTRAKSI DATA MENTAH SENSOR DARI ALAT UKUR ---
    berat_kendaraan_kosong_kg = 2400
    gaya_rem_kiri_kn = 6.20
    gaya_rem_kanan_kn = 5.85
    
    # Inisialisasi Variabel Antrean menggunakan Operator Penugasan Tradisional
    nomor_antrean = 15
    
    # --- 3. OPERATOR ARITMATIKA (MANIPULASI ALU) ---
    # Tahap Konversi besaran ukur dari satuan kilonewton (kN) ke Kilogram-force (Kg) 
    gaya_kiri_kg = gaya_rem_kiri_kn * 101.97
    gaya_kanan_kg = gaya_rem_kanan_kn * 101.97
    
    # Modifikasi Memori menggunakan Operator Penugasan Majemuk (Compound Assignment)
    # Mesin mengambil angka lama, menambahkannya 1, dan menyimpannya kembali di lokasi yang sama
    nomor_antrean += 1 
    
    # Eksekusi Kalkulasi Efisiensi (Memaksakan kasta prioritas dengan Tanda Kurung)
    total_gaya_rem = gaya_kiri_kg + gaya_kanan_kg
    efisiensi_rem_persen = (total_gaya_rem / berat_kendaraan_kosong_kg) * 100
    
    # Kalkulasi Persentase Penyimpangan Sumbu (Deviasi Mutlak Kiri-Kanan)
    # Penerapan struktur kendali untuk mencari deviasi nilai terbesar dikurangi yang terkecil
    if gaya_kiri_kg > gaya_kanan_kg:
        selisih_rem_persen = ((gaya_kiri_kg - gaya_kanan_kg) / total_gaya_rem) * 100
    else:
        selisih_rem_persen = ((gaya_kanan_kg - gaya_kiri_kg) / total_gaya_rem) * 100

    # --- 4. OPERATOR KOMPARASI (EVALUASI AMBANG BATAS/THRESHOLD) ---
    # Mesin menimbang kalkulasi aritmatika dengan konstanta baku mutu, melemparkan Boolean True/False
    lulus_batas_efisiensi = efisiensi_rem_persen >= BATAS_EFISIENSI_MINIMAL
    lulus_batas_deviasi = selisih_rem_persen <= BATAS_SELISIH_MAKSIMAL

    # --- 5. OPERATOR LOGIKA (KESIMPULAN TUNGGAL BERBASIS ALJABAR BOOLEAN) ---
    # Parameter Integritas: Kendaraan HANYA berstatus lulus jika efisiensi memadai (True) 
    # AND distribusi gayanya berimbang dan aman (True)
    status_kelayakan_jalan = lulus_batas_efisiensi and lulus_batas_deviasi

    # --- 6. MENCETAK LAPORAN OUTPUT KE LAYAR TERMINAL ---
    print(f"[STATUS] Menganalisis Kendaraan Antrean No: {nomor_antrean}")
    
    print("\n[HASIL KALKULASI ARITMATIKA ALAT UJI]")
    # Fungsi round(variabel, 2) memotong desimal yang tidak relevan agar tampilan bersih
    print(f"Total Gaya Rem       : {round(total_gaya_rem, 2)} Kg")
    print(f"Efisiensi Pengereman : {round(efisiensi_rem_persen, 2)} %")
    print(f"Selisih Rem (Kiri-Ka): {round(selisih_rem_persen, 2)} %")

    print("\n[EVALUASI KOMPARASI ALGORITMA]")
    print(f"Syarat 1 (Efisiensi >= {BATAS_EFISIENSI_MINIMAL}%)  : {lulus_batas_efisiensi}")
    print(f"Syarat 2 (Deviasi <= {BATAS_SELISIH_MAKSIMAL}%)   : {lulus_batas_deviasi}")

    print("\n[KEPUTUSAN LOGIKA FINAL]")
    if status_kelayakan_jalan == True:
        print(">>> KENDARAAN [ LULUS ] UJI REM UTAMA <<<")
    else:
        print(">>> KENDARAAN [ GAGAL ] UJI REM UTAMA <<<")
    print("==================================================")