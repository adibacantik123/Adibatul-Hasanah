# Class hewan
class hewan:
    def __init__(self, nama, usia, habitat):
        self.nama = nama
        self.usia = usia
        self.habitat = habitat

    def info(self):
        return f"{self.nama} berusia {self.usia} tahun dan hidup di {self.habitat}."