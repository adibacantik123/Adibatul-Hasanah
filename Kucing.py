from hewan import hewan 

# Class child untuk Hewan
class Kucing(hewan):
    def __init__(self, nama, usia, habitat, ras):
        super().__init__(nama, usia, habitat)
        self.ras = ras

    def info(self):
        return f"{self.nama} adalah kucing ras {self.ras}, usia nya {self.usia} tahun, dan hidup di {self.habitat}."
 
#objek kucing
kucing1 = Kucing("Luna", 2, "Rumah", "Persia")
kucing2 = Kucing("Leo", 3, "Apartemen", "Anggora")
kucing3 = Kucing("Mochi", 1, "Desa", "Bengal")
kucing4 = Kucing("Choco", 4, "Pondok", "Sphynx")

#cetak
print("=== Informasi Kucing ===")
print(kucing1.info())
print(kucing2.info())
print(kucing3.info())
print(kucing4.info())
