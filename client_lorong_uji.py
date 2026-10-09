# =====================================================================
# PROYEK AKHIR - TAHAP 1: SCRIPT SERVER PUSAT (BACK-END & UI)
# NAMA FILE: server_pusat.py
# =====================================================================

from flask import Flask, request, render_template_string
import sqlite3
import json

app = Flask(__name__)
NAMA_DATABASE = "database_kir_pusat.db"

# 1. INISIALISASI STRUKTUR BASIS DATA (DDL)
def inisialisasi_database():
    koneksi = sqlite3.connect(NAMA_DATABASE)
    kursor = koneksi.cursor()
    kursor.execute("""
        CREATE TABLE IF NOT EXISTS tabel_uji_rem (
            id_kendaraan TEXT PRIMARY KEY,
            berat_sumbu REAL,
            gaya_rem_total REAL,
            efisiensi REAL,
            status TEXT,
            waktu_uji TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    koneksi.commit()
    koneksi.close()

# 2. ENDPOINT API UNTUK MENERIMA DATA DARI MESIN UJI (METODE POST)
@app.route('/api/terima_data', methods=['POST'])
def api_terima_data():
    try:
        # Mengekstrak muatan JSON dari transmisi HTTP Klien
        data_klien = request.get_json()
        
        # Validasi keamanan data (Memastikan data tidak kosong)
        if not data_klien:
            return {"status": "error", "pesan": "Payload JSON kosong"}, 400
            
        # Membuka koneksi database untuk proses injeksi (DML)
        koneksi = sqlite3.connect(NAMA_DATABASE)
        kursor = koneksi.cursor()
        
        perintah_sql = """
            INSERT INTO tabel_uji_rem (id_kendaraan, berat_sumbu, gaya_rem_total, efisiensi, status)
            VALUES (?, ?, ?, ?, ?)
        """
        parameter = (
            data_klien['id_kendaraan'],
            data_klien['berat_sumbu'],
            data_klien['gaya_rem_total'],
            data_klien['efisiensi'],
            data_klien['status']
        )
        
        kursor.execute(perintah_sql, parameter)
        koneksi.commit()
        koneksi.close()
        
        print(f"[SERVER LOG] Berhasil menyimpan data kendaraan: {data_klien['id_kendaraan']}")
        return {"status": "sukses", "pesan": "Data berhasil direkam oleh Server Pusat."}, 200

    except sqlite3.IntegrityError:
        print("[SERVER ERROR] Terjadi duplikasi ID Kendaraan.")
        return {"status": "error", "pesan": "Integritas Data Gagal (Duplikat ID)."}, 409
    except Exception as e:
        print(f"[SERVER ERROR] Galat Sistem: {e}")
        return {"status": "error", "pesan": str(e)}, 500

# 3. ENDPOINT WEB DASHBOARD UNTUK ADMINISTRATOR (METODE GET)
@app.route('/')
def halaman_dashboard():
    koneksi = sqlite3.connect(NAMA_DATABASE)
    kursor = koneksi.cursor()
    # Mengambil data diurutkan dari yang paling baru
    kursor.execute("SELECT id_kendaraan, berat_sumbu, gaya_rem_total, efisiensi, status, waktu_uji FROM tabel_uji_rem ORDER BY waktu_uji DESC")
    semua_data = kursor.fetchall()
    koneksi.close()
    
    # Template HTML Internal (Tanpa perlu folder templates terpisah untuk kemudahan praktikum)
    desain_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Dashboard Server UJI KIR</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; padding: 20px; background-color: #f0f2f5;}
            table { width: 100%; border-collapse: collapse; background-color: white; box-shadow: 0 1px 3px rgba(0,0,0,0.2); }
            th, td { border: 1px solid #dddddd; text-align: center; padding: 12px; }
            th { background-color: #2c3e50; color: white; }
            .lulus { color: green; font-weight: bold; }
            .gagal { color: red; font-weight: bold; }
        </style>
    </head>
    <body>
        <h2 style="text-align: center; color: #2c3e50;">SERVER PUSAT: REKAPITULASI UJI REM (BRAKE TESTER)</h2>
        <table>
            <tr>
                <th>Waktu Pengujian</th><th>ID Registrasi</th><th>Berat Sumbu (Kg)</th>
                <th>Total Gaya Rem (Kg)</th><th>Efisiensi (%)</th><th>Status Akhir</th>
            </tr>
            {% for baris in data_kendaraan %}
            <tr>
                <td>{{ baris[5] }}</td><td>{{ baris[0] }}</td><td>{{ baris[1] }}</td>
                <td>{{ baris[2] }}</td><td>{{ baris[3] }}</td>
                {% if baris[4] == 'LULUS' %}
                    <td class="lulus">{{ baris[4] }}</td>
                {% else %}
                    <td class="gagal">{{ baris[4] }}</td>
                {% endif %}
            </tr>
            {% else %}
            <tr><td colspan="6">Pangkalan data kosong. Menunggu data dari Lorong Uji...</td></tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """
    return render_template_string(desain_html, data_kendaraan=semua_data)

if __name__ == "__main__":
    inisialisasi_database()
    print("==========================================================")
    print(" SERVER PUSAT DIAKTIFKAN PADA http://127.0.0.1:5000")
    print("==========================================================")
    app.run(host='0.0.0.0', port=5000)