# =====================================================================
# SIMULASI BLOK KODE: ALGORITMA CONTINUOUS SCAN CYCLE PLC
# STUDI KASUS: SISTEM LATCHING DAN INTERLOCK FORWARD-REVERSE
# =====================================================================

import time

if __name__ == "__main__":
    print("==================================================")
    print(" INISIALISASI SIMULATOR CPU PLC (VERSI PYTHON)")
    print("==================================================")

    # Inisialisasi Memori Output Image Table (Mesin dalam keadaan Off)
    koil_motor_forward = False
    koil_motor_reverse = False
    
    # Penghitung jumlah siklus operasi (Scan Time Counter)
    siklus_pemindaian = 1
    
    # Memulai eksekusi Scan Cycle Abadi (Simulasi dibatasi 10 siklus)
    while siklus_pemindaian <= 10:
        print(f"\n--- [SCAN CYCLE #{siklus_pemindaian}] ---")
        
        # -------------------------------------------------------------
        # FASE 1: INPUT SCAN (Pengambilan Status Sensor/Terminal Fisik)
        # -------------------------------------------------------------
        tombol_start_forward = False  # NO Contact
        tombol_start_reverse = False  # NO Contact
        tombol_stop = False           # NC Contact (Logika terbalik dikelola di Fase 2)
        
        # Skenario 1: Operator mengaktifkan tombol Forward (Siklus 2)
        if siklus_scan == 2:
            tombol_start_forward = True
            print("[TERMINAL INPUT] Tombol START FORWARD ditekan.")
            
        # Skenario 2: Operator mencoba memutar Reverse saat Forward masih menyala (Siklus 5)
        if siklus_scan == 5:
            tombol_start_reverse = True
            print("[TERMINAL INPUT] Tombol START REVERSE ditekan paksa!")

        # -------------------------------------------------------------
        # FASE 2: PROGRAM EXECUTION (Kalkulasi Evaluasi Ladder Diagram)
        # -------------------------------------------------------------
        
        # Evaluasi Anak Tangga 1: Motor Forward
        # Logika: (Start FWD OR Pengunci FWD) AND NOT Stop AND NOT Koil REV
        jalur_pengunci_fwd = tombol_start_forward or koil_motor_forward
        syarat_aman_fwd = (not tombol_stop) and (not koil_motor_reverse)
        
        if jalur_pengunci_fwd and syarat_aman_fwd:
            kalkulasi_fwd = True
        else:
            kalkulasi_fwd = False
            
        # Evaluasi Anak Tangga 2: Motor Reverse
        # Logika: (Start REV OR Pengunci REV) AND NOT Stop AND NOT Koil FWD
        jalur_pengunci_rev = tombol_start_reverse or koil_motor_reverse
        syarat_aman_rev = (not tombol_stop) and (not koil_motor_forward)
        
        if jalur_pengunci_rev and syarat_aman_rev:
            kalkulasi_rev = True
        else:
            kalkulasi_rev = False
            
        # -------------------------------------------------------------
        # FASE 3: OUTPUT SCAN (Pembaruan Status Keluaran ke Mesin)
        # -------------------------------------------------------------
        # Transmisi hasil evaluasi internal ke memori koil aktual
        koil_motor_forward = kalkulasi_fwd
        koil_motor_reverse = kalkulasi_rev
        
        # Pencetakan status operasional mesin
        if koil_motor_forward:
            print(">>> [AKTIF] AKTUATOR BERPUTAR ARAH FORWARD (Interlock Terkunci)")
        elif koil_motor_reverse:
            print(">>> [AKTIF] AKTUATOR BERPUTAR ARAH REVERSE (Interlock Terkunci)")
        else:
            print(">>> [NONAKTIF] AKTUATOR DALAM KEADAAN DIAM")
            
        # Simulasi Jeda Waktu (Housekeeping dan Sinkronisasi)
        siklus_pemindaian += 1
        time.sleep(1.0)
        
    print("\n==================================================")
    print(" SIMULASI SIKLUS OPERASIONAL MESIN BERAKHIR")
    print("==================================================")