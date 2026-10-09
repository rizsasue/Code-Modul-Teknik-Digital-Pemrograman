# =====================================================================
# SIMULASI BLOK KODE: STRUKTUR PERULANGAN PADA AKUISISI DATA SENSOR
# STUDI KASUS: SAMPLING UJI EMISI GAS BUANG MULTI-SIKLUS
# =====================================================================

import time
import random  # Digunakan semata untuk menyimulasikan data sensor acak

if __name__ == "__main__":
    print("==================================================")
    print(" INISIALISASI MODUL GAS ANALYZER (SIMULASI LOOP)")
    print("==================================================")

    # --- 1. SIMULASI STANDBY MODE (MENGGUNAKAN WHILE LOOP) ---
    print("\n[FASE 1] Sistem memantau ketersediaan probe pada knalpot...")
    waktu_tunggu = 1
    
    # Perulangan while akan terus berjalan selama waktu_tunggu kurang dari 4
    while waktu_tunggu < 4:
        print(f"-> Detik ke-{waktu_tunggu}: Sensor belum mendeteksi aliran gas.")
        time.sleep(1) # Menunda eksekusi mesin selama 1 detik
        waktu_tunggu += 1 # Compound Assignment (wajib agar tidak Infinite Loop)
        
    print(">>> ALIRAN GAS TERDETEKSI. MEMULAI SAMPLING DATA <<<")

    # --- 2. SIMULASI SAMPLING DATA TERUKUR (MENGGUNAKAN FOR LOOP) ---
    print("\n[FASE 2] Proses Pengambilan 5 Sampel Data HC (PPM)")
    
    total_hc_terakumulasi = 0.0
    sampel_berhasil = 0
    
    # Perulangan for untuk membatasi pengambilan data tepat 5 kali
    for iterasi in range(1, 6):
        time.sleep(0.5) # Jeda pembacaan alat ukur
        
        # Simulasi fluktuasi data mesin (bisa normal, bisa error minus)
        # Menghasilkan angka acak antara -20 (error) hingga 250 (normal)
        data_hc_sensor = random.uniform(-20.0, 250.0) 
        
        # --- IMPLEMENTASI INTERUPSI KONTROL (CONTINUE & BREAK) ---
        if data_hc_sensor < 0.0:
            print(f"  [X] Siklus {iterasi}: Data cacat (Negatif). Mengabaikan sampel.")
            continue # Mengabaikan baris di bawah, langsung lanjut ke siklus berikutnya
            
        if data_hc_sensor > 500.0:
            print(f"  [!] Siklus {iterasi}: KONSENTRASI BERBAHAYA! Hentikan alat!")
            break # Menghancurkan loop secara total (Emergency Stop)
            
        # Jika data valid, eksekusi penyimpanan ke variabel akumulasi
        print(f"  [v] Siklus {iterasi}: Membaca HC sebesar {round(data_hc_sensor, 2)} PPM")
        total_hc_terakumulasi += data_hc_sensor
        sampel_berhasil += 1

    # --- 3. KALKULASI PASCAL-LOOP (MENGHITUNG RATA-RATA) ---
    print("\n[FASE 3] Evaluasi Data Akhir")
    if sampel_berhasil > 0:
        rata_rata_hc = total_hc_terakumulasi / sampel_berhasil
        print(f"Total Sampel Valid : {sampel_berhasil} sampel")
        print(f"Nilai Rata-rata HC : {round(rata_rata_hc, 2)} PPM")
    else:
        print("Pengujian gagal. Tidak ada data valid yang terekam.")
        
    print("==================================================")