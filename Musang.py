from hewan import hewan

class Musang(hewan):
    def __init__(self, nama, usia, habitat, jenis):
        super().__init__(nama, usia, habitat)
        self.jenis = jenis

    def info(self):
        return f"{self.nama} adalah musang jenis {self.jenis}, usia nya {self.usia} tahun, dan hidup di {self.habitat}."

# Objek Musang
musang1 = Musang("Fero", 2, "Pohon Kelapa", "Musang Pandan")
musang2 = Musang("Sugi", 3, "Kebun Kopi", "Musang Luwak")
musang3 = Musang("Miki", 1, "Taman Belakang", "Musang Rase")
musang4 = Musang("Dino", 4, "Pinggir Hutan", "Musang Binturong")

print("\n=== Informasi Musang ===")
print(musang1.info())
print(musang2.info())
print(musang3.info())
print(musang4.info())
