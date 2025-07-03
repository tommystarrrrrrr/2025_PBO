# database.py
import sqlite3

class DatabaseManager:
    def __init__(self, db_name='vote.db'):
        self.db_name = db_name
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS voting (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pemilih TEXT NOT NULL,
                kandidat TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    def simpan_suara(self, pemilih, kandidat):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("INSERT INTO voting (pemilih, kandidat) VALUES (?, ?)", (pemilih, kandidat))
        conn.commit()
        conn.close()

    def ambil_hasil(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("SELECT kandidat, COUNT(*) FROM voting GROUP BY kandidat")
        hasil = c.fetchall()
        conn.close()
        return hasil

    def sudah_memilih(self, nama_pemilih):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("SELECT COUNT(*) FROM voting WHERE pemilih = ?", (nama_pemilih,))
        hasil = c.fetchone()[0]
        conn.close()
        return hasil > 0

    def hapus_semua_suara(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("DELETE FROM voting")
        conn.commit()
        conn.close()
