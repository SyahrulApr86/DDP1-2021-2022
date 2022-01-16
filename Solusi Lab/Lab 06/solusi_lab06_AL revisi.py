# total waktu (baca + ngoding + coba tc dll) = +- 45 menit
# revisi = 25 menit

MENIT_DALAM_JAM = 60
MENIT_DALAM_HARI = 60 * 24

HARI = [i * MENIT_DALAM_HARI for i in range(7)]
JAM = [i * MENIT_DALAM_JAM for i in range(24)]

MATKUL_TERSEDIA = [
    ["ddp 1 a", HARI[0] + JAM[8] + 0, HARI[0] +  JAM[9] + 40],
    ["ddp 1 a", HARI[2] + JAM[8] + 0, HARI[2] +  JAM[9] + 40],
    ["ddp 1 b", HARI[1] + JAM[8] + 0, HARI[0] +  JAM[9] + 40],
    ["manbis", HARI[0] + JAM[9] + 0, HARI[0] + JAM[10] + 40],
    ["matdis 1 a", HARI[2] + JAM[9] + 0, HARI[2] + JAM[10] + 40],
    ["matdis 1 b", HARI[0] + JAM[9] + 0, HARI[0] + JAM[10] + 40],
    ["matdis 1 c", HARI[0] + JAM[9] + 0, HARI[0] + JAM[10] + 40],
    ["kalkulus 1 c", HARI[2] + JAM[10] + 0, HARI[2] + JAM[12] + 00]
]



"""
Merepresentasikan jadwal “ddp 1 a” hari senin 08.00 sampai 09.40, serta hari rabu jam 08.00 sampai 09.40

Jadwal “ddp 1 b” hari rabu jam 08.00 sampai 09.40
Jadwal “manbis” hari senin jam 09.00 sampai 10.40
Jadwal “matdis 1 a” hari rabu jam 09.00 sampai 10.40
Jadwal “matdis 1 b” hari rabu jam 09.00 sampai 10.40
"""

matkul_diambil = []

def func(e) : 
    return e[1]

while True : 
    print("=========== SUSUN JADWAL ===========")
    print("1  Add matkul")
    print("2  Drop matkul")
    print("3  Cek ringkasan")
    print("4  Lihat daftar matkul ")
    print("5  Selesai ")
    print("====================================")

    menu = input("\nMasukkan pilihan: ")
    matkul_diambil.sort(key=func)

    if menu == "1" : 
        matkul_input = input("Masukkan nama matkul: ")
        matkul_pilihan = [matkul for matkul in MATKUL_TERSEDIA if matkul_input.lower().replace(" ", "") == matkul[0].lower().replace(" ", "")] 
        if matkul_pilihan == [] : 
            print("Matkul tidak ditemukan")
        else : 
            matkul_diambil.extend(matkul_pilihan)
        print()


    elif menu == "2" : 
        matkul_input = input("Masukkan nama matkul: ")
        matkul_pilihan = [matkul for matkul in matkul_diambil if matkul_input.lower().replace(" ", "") == matkul[0].lower().replace(" ", "")]
        if matkul_pilihan == [] : 
            print("Matkul tidak ditemukan")
        else : 
            for i in range (len(matkul_pilihan)) : 
                matkul_diambil.remove(matkul_pilihan[i])
        print()
        
    elif menu == "3" : 
        tidak_bermasalah = True
        for i in range(len(matkul_diambil)) : 
            for j in range(i+1, len(matkul_diambil)) : 
                if matkul_diambil[i][1] <= matkul_diambil[j][1] < matkul_diambil[i][2]: 
                    print (f"{matkul_diambil[i][0]} bentrok dengan {matkul_diambil[j][0]}")
                    tidak_bermasalah = False

        if tidak_bermasalah : 
            print("Tidak ada matkul yang bermasalah\n")
        else : 
            print()


    elif menu == "4" : 
        hari_start = 0
        
        if matkul_diambil == [] : 
            print("Tidak ada matkul yang diambil\n")
        else : 
            print("daftar matkul: ")
            for matkul in matkul_diambil : 
                hari_start = matkul[1] // 1440
                if hari_start == 0 : 
                    hari_start = "Senin, "
                elif hari_start == 1 : 
                    hari_start = "Selasa, "
                elif hari_start == 2 : 
                    hari_start = "Rabu, "
                elif hari_start == 3 : 
                    hari_start = "Kamis, "
                elif hari_start == 4 : 
                    hari_start = "Jumat, "

                jam_start = matkul[1] % 1440 // 60
                menit_start = matkul[1] % 1440 % 60

                hari_end = matkul[2] // 1440
                if hari_end == 0 : 
                    hari_end = "Senin, "
                elif hari_end == 1 : 
                    hari_end = "Selasa, "
                elif hari_end == 2 : 
                    hari_end = "Rabu, "
                elif hari_end == 3 : 
                    hari_end = "Kamis, "
                elif hari_end == 4 : 
                    hari_end = "Jumat, "

                jam_end = matkul[2] % 1440 // 60
                menit_end = matkul[2] % 1440 % 60

                print(f"{matkul[0].upper():15s}{hari_start:8s}{jam_start:02d}:{menit_start:02d} s/d {hari_end:8s}{jam_end:02d}:{menit_end:02d}")

            print()

    elif menu == "5" : 
        print("Terima kasih!")
        break

    else : 
        print("Maaf, pilihan tidak tersedia\n")


