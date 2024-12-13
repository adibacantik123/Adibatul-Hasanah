from hewan import hewan

class Gecko(hewan):
    def __init__(self, nama, usia, habitat, panjang):
        super().__init__(nama, usia, habitat)
        self.panjang = panjang

    def info(self):
        return f"{self.nama} adalah gecko dengan panjang {self.panjang} cm, usia nya {self.usia} tahun, dan hidup di {self.habitat}."

# Objek Gecko
gecko1 = Gecko("Gecky", 1, "Akuarium", 15)
gecko2 = Gecko("Lizzy", 2, "Terarium", 20)
gecko3 = Gecko("Spiky", 1.5, "Pohon", 18)
gecko4 = Gecko("Tiny", 3, "Kandang", 22)

#cetak
print("\n=== Informasi Gecko ===")
print(gecko1.info())
print(gecko2.info())
print(gecko3.info())
print(gecko4.info())