# model.py
class Kandidat:
    def __init__(self, nama):
        self._nama = nama

    @property
    def nama(self):
        return self._nama


class Voting:
    def __init__(self, pemilih, kandidat):
        self._pemilih = pemilih
        self._kandidat = kandidat

    @property
    def pemilih(self):
        return self._pemilih

    @property
    def kandidat(self):
        return self._kandidat
