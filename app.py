# Mengimpor pustaka Flask dan SQLite
from flask import Flask, render_template
import sqlite3

# Menginisialisasi mesin aplikasi web Flask
aplikasi_web = Flask(__name__)

# Mendefinisikan Rute (URL Endpoint) utama
@aplikasi_web.route('/')
def halaman_utama_dashboard():
    # 1. Membuka koneksi ke pangkalan data relasional
    koneksi_db = sqlite3.connect("server_pengujian.db")
    kursor = koneksi_db.cursor()
    
    # 2. Menarik (Query) seluruh rekaman data pengujian dari tabel
    kursor.execute("SELECT * FROM rekam_jejak_uji")
    semua_data_kendaraan = kursor.fetchall() # Berupa List of Tuples
    
    # 3. Menutup koneksi (Prosedur Keamanan Memori)
    koneksi_db.close()
    
    # 4. Merender HTML dan menyuntikkan variabel 'semua_data_kendaraan' ke Front-end
    return render_template('index.html', data_uji=semua_data_kendaraan)

# Perintah untuk menjalankan server lokal di Port 5000
if __name__ == '__main__':
    # Mengizinkan akses dari semua perangkat di jaringan LAN (host='0.0.0.0')
    aplikasi_web.run(host='0.0.0.0', port=5000, debug=True)