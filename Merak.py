from hewan import hewan

class Merak(hewan):
    def __init__(self, nama, usia, habitat, warna_bulu):
        super().__init__(nama, usia, habitat)
        self.warna_bulu = warna_bulu

    def info(self):
        return f"{self.nama} adalah merak dengan warna bulu {self.warna_bulu}, usia nya {self.usia} tahun, dan hidup di {self.habitat}."

# Objek Merak
merak1 = Merak("Raja", 5, "Hutan Tropis", "Hijau")
merak2 = Merak("Indah", 4, "Taman Safari", "Biru")
merak3 = Merak("Cantik", 6, "Hutan Jawa", "Emas")
merak4 = Merak("Mulia", 3, "Cagar Alam", "Putih")

#cetak 
print("\n=== Informasi Merak ===")
print(merak1.info())
print(merak2.info())
print(merak3.info())
print(merak4.info())