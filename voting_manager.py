# voting_manager.py
from model import Voting
from database import DatabaseManager

class VotingManager:
    def __init__(self):
        self.db = DatabaseManager()

    def submit_vote(self, nama_pemilih, kandidat):
        if self.db.sudah_memilih(nama_pemilih):
            return False, "Nama ini sudah pernah memilih!"
        vote = Voting(nama_pemilih, kandidat)
        self.db.simpan_suara(vote.pemilih, vote.kandidat)
        return True, f"Terima kasih {vote.pemilih}, suara Anda untuk {vote.kandidat} telah disimpan."

    def get_hasil(self):
        return self.db.ambil_hasil()

    def reset_voting(self):
        self.db.hapus_semua_suara()
