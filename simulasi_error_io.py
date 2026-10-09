# =====================================================================
# SIMULASI BLOK KODE: ERROR HANDLING & FILE I/O (PERSISTENSI DATA)
# STUDI KASUS: SISTEM AKUISISI DAN PENCATATAN BERAT SUMBU (AXLE LOAD)
# =====================================================================

import time # Modul untuk mengambil waktu jeda (timestamp simulasi)

if __name__ == "__main__":
    print("==================================================")
    print(" MODUL AKUISISI DATA SENSOR BERAT AKTIF (SAFE MODE)")
    print("==================================================")

    # Inisialisasi variabel string untuk mencatat riwayat
    catatan_log_baru = ""

    # --- 1. MEMBUKA BLOK JARING PENGAMAN (TRY) ---
    try:
        # Mensimulasikan input data mentah. (Fungsi input() menahan layar 
        # hingga operator mengetik sesuatu dan menekan Enter).
        raw_input_berat = input(">> Masukkan Berat Sumbu (Kg): ")
        
        # Titik Krisis Pertama: Type Casting (Berpotensi ValueError)
        berat_aktual_kg = float(raw_input_berat)
        
        # Titik Krisis Kedua: Operasi Fisika (Berpotensi ZeroDivisionError)
        # Menghitung estimasi distribusi gaya (misal dibagi rata ke roda)
        gaya_distribusi = 5000 / berat_aktual_kg
        
        print(f"\n[SUKSES] Komputasi Berhasil. Distribusi Gaya: {round(gaya_distribusi, 2)}")
        catatan_log_baru = f"BERHASIL | Input Berat: {berat_aktual_kg} Kg | Distribusi: {gaya_distribusi}"

    # --- 2. PENANGKAP GALAT / EXCEPTION HANDLER ---
    except ValueError:
        # Menangkap error jika teks yang dimasukkan bukan angka numerik
        print("\n[PERINGATAN SINTAKSIS] Data sensor korup. Masukan tidak dapat dikonversi ke angka desimal.")
        catatan_log_baru = f"ERROR_VALUE | Input Ditolak (Bukan Numerik): {raw_input_berat}"
        
    except ZeroDivisionError:
        # Menangkap error jika berat yang dimasukkan tepat angka Nol
        print("\n[PERINGATAN FISIKA] Sensor berat membaca angka NOL. Komputasi distribusi tidak mungkin dilakukan (Devide by Zero).")
        catatan_log_baru = f"ERROR_ZERO | Input Ditolak: Berat tidak logis (0 Kg)"
        
    # Blok Exception utama (Menangkap error lain yang tidak teridentifikasi)
    except Exception as e:
        print(f"\n[SISTEM CRASH TERHINDARI] Error tidak dikenal terdeteksi: {e}")
        catatan_log_baru = f"ERROR_UNKNOWN | Kejadian: {e}"

    # --- 3. BLOK FILE I/O (PERSISTENSI DATA / LOGGING) ---
    # Terlepas dari program berhasil atau memicu error, kita WAJIB mencatat hasilnya ke Hard Disk
    print("\n[SISTEM] Menyimpan riwayat aktivitas ke database lokal (log_sistem.txt)...")
    
    # Membuka file dengan mode 'a' (Append/Sisipkan di Bawah) menggunakan Context Manager
    with open("log_sistem.txt", "a") as file_log:
        # Mengekstrak waktu saat ini untuk laporan audit
        waktu_sekarang = time.ctime()
        
        # Merakit teks yang akan disuntikkan ke dalam file txt
        teks_rekaman = f"[{waktu_sekarang}] -> {catatan_log_baru}\n"
        
        # Menulis paksa memori ke Hard Disk
        file_log.write(teks_rekaman)
    
    print("[SISTEM] Proses Penulisan File I/O Selesai. Eksekusi Program Berakhir Aman.")
    print("==================================================")