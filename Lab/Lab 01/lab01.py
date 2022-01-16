import math #import math agar bisa mendefinisikan pi dengan presisi
rad = float(input("Masukkan radius lingkaran: ")) #input user

luas_ungu = rad**2 #luas segitiga
luas_kuning = math.pi * rad**2 - luas_ungu #luas lingkaran tanpa segitiga
luas_merah = (2*rad)**2 - luas_kuning - luas_ungu #luas persegi tanpa lingkaran dan tanpa segitiga

print(f"Luas daerah cat merah: {luas_merah:.2f}") #menggunakan format string agar dapat menampilkan 2 angka dibelakang koma
print(f"Luas daerah cat kuning: {luas_kuning:.2f}")
print(f"Luas daerah cat ungu: {luas_ungu:.2f}")
 
