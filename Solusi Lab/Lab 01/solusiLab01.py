import math

# meminta input radius dari user
rad = float(input("Masukkan radius lingkaran: "))

# melakukan penghitungan luas dengan rumus bangun datar
luas_persegi = (rad*2)**2
luas_lingkaran = math.pi*rad**2
luas_segitiga = rad*rad

# melakukan penghitungan luas daerah berdasarkan cat
luas_merah = luas_persegi-luas_lingkaran
luas_kuning = luas_lingkaran - luas_segitiga
luas_ungu = luas_segitiga

# mencetak output luas daerah berdasarkan cat
print(f"Luas daerah cat merah: {luas_merah:.2f}")
print(f"Luas daerah cat kuning: {luas_kuning:.2f}")
print(f"Luas daerah cat ungu: {luas_ungu:.2f}")