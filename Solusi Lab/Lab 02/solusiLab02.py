print("Selamat datangg")

# inisialisasi variabel-variabel yang diperlukan
jumlah_matkul = 0
sks_total = 0
sks_lulus = 0
mutu_total = 0
mutu_lulus = 0

# validasi input jumlah matkul dari user
while True:
    jumlah_matkul = int(input("Masukkan jumlah mata kuliah: "))
    if jumlah_matkul == 0: # hentikan program jika input user sama dengan 0
        print("Tidak ada mata kuliah yang diambil.")
        exit()
    elif jumlah_matkul > 0: # keluar dari loop jika input user valid, yaitu lebih dari 0
        break

# meminta prompt pada user sesuai dengan jumlah matkul
for i in range(jumlah_matkul):
    nama_matkul = input("Masukkan nama mata kuliah ke-" + str(i+1) + " :")
    sks_matkul = int(input(f"Masukkan jumlah SKS {nama_matkul}: "))
    nilai = float(input(f"Masukkan nilai yang kamu dapatkan: "))
    # validasi nilai mata kuliah, yaitu tidak boleh kurang dari 0
    while nilai < 0:
        print("Nilai tidak boleh negatif")
        nilai = float(input(f"Masukkan nilai yang kamu dapatkan: "))
    status = "lulus" # nilai default dari status

    # penentuan bobot sesuai nilai mata kuliah
    if (nilai >= 85):
        bobot = 4.00
    elif (80 <= nilai < 85):
        bobot = 3.70
    elif(75 <= nilai < 80):
        bobot = 3.30
    elif (70 <= nilai < 75):
        bobot = 3.00
    elif(65 <= nilai < 70):
        bobot = 2.70
    elif (60 <= nilai < 65):
        bobot = 2.30
    elif(55 <= nilai < 60):
        bobot = 2.00
    elif (40 <= nilai < 55):
        bobot = 1.00
        status = "tidak lulus" # status diubah jika nilai jatuh pada rentang ini
    elif(0 <= nilai < 40):
        bobot = 0.00
        status = "tidak lulus" # status diubah jika nilai jatuh pada rentang ini
    
    # penghitungan sks total dan mutu total
    sks_total = sks_total + sks_matkul
    mutu_total += sks_matkul*bobot

    # penghitungan sks lulus dan mutu lulus
    if (status == "lulus"):
        sks_lulus += sks_matkul
        mutu_lulus += sks_matkul*bobot

# penghitungan ipt    
ipt = mutu_total/sks_total

# penghitungan ipk
if sks_lulus == 0: # menghandle jika tidak ada sks yang lulus
    ipk = 0
else:
    ipk = mutu_lulus/sks_lulus 

# mencetak output sesuai ketentuan program
print()
print(f"Jumlah SKS lulus : {sks_lulus} / {sks_total}")
print(f"Jumlah mutu lulus: {mutu_lulus:.2f} / {mutu_total:.2f}")
print(f"Total IPK kamu adalah {ipk:.2f}")
print(f"Total IPT kamu adalah {ipt:.2f}")