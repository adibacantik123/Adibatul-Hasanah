from hewan import hewan

class Tupai(hewan):
    def __init__(self, nama, usia, habitat, makanan_favorit):
        super().__init__(nama, usia, habitat)
        self.makanan_favorit = makanan_favorit

    def info(self):
        return f"{self.nama} adalah tupai yang suka makan {self.makanan_favorit}, usianya {self.usia} tahun, dan hidup di {self.habitat}."

# Objek Tupai
tupai1 = Tupai("Chippy", 1, "Hutan", "Kacang")
tupai2 = Tupai("Niko", 2, "Pohon Pinus", "Buah-buahan")
tupai3 = Tupai("Bimo", 1.5, "Taman Kota", "Bijian")
tupai4 = Tupai("Lulu", 3, "Kebun Buah", "Mangga")

#cetak
print("\n=== Informasi Tupai ===")
print(tupai1.info())
print(tupai2.info())
print(tupai3.info())
print(tupai4.info())