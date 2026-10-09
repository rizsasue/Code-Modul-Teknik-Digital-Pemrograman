# =====================================================================
# SIMULASI BLOK KODE: ARSITEKTUR SCAN CYCLE DAN LADDER LOGIC PLC
# STUDI KASUS: KONTROL MOTOR BRAKE TESTER DENGAN SISTEM LATCHING
# =====================================================================

import time

if __name__ == "__main__":
    print("==================================================")
    print(" INISIALISASI SIMULATOR PLC: PANEL BRAKE TESTER")
    print("==================================================")

    # Inisialisasi Memori Output Coil (Mesin mati pada kondisi awal/default)
    status_koil_motor = False
    
    # Variabel penghitung siklus murni untuk keperluan visualisasi di terminal
    siklus_scan = 1
    
    # Memulai Siklus Pemindaian (Scan Cycle) Abadi
    while siklus_scan <= 10:
        print(f"\n--- [SCAN CYCLE #{siklus_scan}] Memulai Pemindaian ---")
        
        # -------------------------------------------------------------
        # FASE 1: INPUT SCAN (Pembacaan Sensor/Panel Fisik secara pasif)
        # -------------------------------------------------------------
        simulasi_tombol_start = False  # Kontak NO (Ditekan = True)
        simulasi_tombol_stop = False   # Kontak NC (Ditekan = True, memutus sirkuit)
        
        # Skenario 1: Jari Operator MENEKAN tombol Start sesaat (Hanya pada siklus 3)
        if siklus_scan == 3:
            simulasi_tombol_start = True
            print("[PANEL FISIK] Operator MENEKAN tombol START (Momentary).")
            
        # Skenario 2: Operator MENEKAN tombol Darurat/Stop (Pada siklus 8)
        if siklus_scan == 8:
            simulasi_tombol_stop = True
            print("[PANEL FISIK] Operator MENEKAN tombol STOP (Memutus Daya)!")

        # -------------------------------------------------------------
        # FASE 2: PROGRAM EXECUTION (Kalkulasi Logika Aljabar Boolean)
        # -------------------------------------------------------------
        # Translasi Ladder: (Start OR Memori_Koil_Motor) AND NOT Stop
        
        # Blok Logika Paralel (Gerbang OR) untuk mekanisme Latching (Jalur Bawah)
        jalur_latching_aktif = simulasi_tombol_start or status_koil_motor
        
        # Blok Logika Seri (Gerbang AND) untuk validasi keamanan absolut
        jalur_safety_aktif = not simulasi_tombol_stop
        
        # Kalkulasi Koil Akhir (Output Internal)
        if jalur_latching_aktif and jalur_safety_aktif:
            status_koil_motor_kalkulasi = True
        else:
            status_koil_motor_kalkulasi = False
            
        # -------------------------------------------------------------
        # FASE 3: OUTPUT SCAN (Pembaruan Terminal Fisik Aktuator)
        # -------------------------------------------------------------
        # Mengunci hasil kalkulasi sementara ke dalam memori aktuator sejati
        status_koil_motor = status_koil_motor_kalkulasi
        
        # Cetak status mekanis perangkat keras
        if status_koil_motor == True:
            print(">>> STATUS AKTUATOR : MOTOR BERPUTAR (KONTRAKTOR AKTIF) <<<")
        else:
            print(">>> STATUS AKTUATOR : MOTOR MATI <<<")
            
        # Housekeeping: Jeda waktu siklus (1 detik untuk simulasi mata manusia)
        siklus_scan += 1
        time.sleep(1.0)
        
    print("\n==================================================")
    print(" SIMULASI SIKLUS KENDALI BERAKHIR (MAKSIMAL 10 SIKLUS)")
    print("==================================================")