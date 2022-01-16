MENIT_DALAM_JAM = 60
MENIT_DALAM_HARI = 60 * 24

HARI = [i * MENIT_DALAM_HARI for i in range(7)]
JAM = [i * MENIT_DALAM_JAM for i in range(24)]

# mendefinisikan matkul yang tersedia
MATKUL_TERSEDIA = [
    ["ddp 1 a",     HARI[0] + JAM[8] + 0,    HARI[0] +  JAM[9] + 40],
    ["ddp 1 a",     HARI[2] + JAM[8] + 0,    HARI[2] +  JAM[9] + 40],
    ["ddp 1 b",     HARI[1] + JAM[8] + 0,    HARI[1] +  JAM[9] + 40],
    ["manbis",      HARI[0] + JAM[9] + 0,    HARI[0] + JAM[10] + 40],
    ["matdis 1 a",  HARI[2] + JAM[9] + 0,    HARI[2] + JAM[10] + 40],
    ["matdis 1 b",  HARI[2] + JAM[9] + 0,    HARI[2] + JAM[10] + 40]
]

# fungsi untuk menentukan waktu yang bentrok
def is_intersecting(timing,next_timing):
    if timing[0] <=  next_timing[0] and timing[1] >= next_timing[0] and timing[1] <= next_timing[1]:
        return True
    else:
        return False

# fungsi untuk mengambil elemen dengan indeks ke-1
def take_day(elem):
    return elem[1]

# membuat menu
menu = """=========== SUSUN JADWAL ===========
1  Add matkul
2  Drop matkul
3  Cek ringkasan
4  Lihat daftar matkul 
5  Selesai 
====================================
"""

# container untuk matkkul yang dipilih
matkul_pilihan = []

# sentinel loop untuk pemilihan mode
while True:
    print(menu)
    mode = input("Masukkan pilihan: ").strip() # meminta user menginput mode

    # conditionals statement untuk pemilihan mode
    if mode == "1":
        matkul = input("Masukkan nama matkul: ").strip() # meminta user menginput matkul
        nama_matkul_tersedia = [i[0].casefold() for i in MATKUL_TERSEDIA] # list berisi daftar nama matkul yang tersedia

        # conditionals statement untuk memasukkan matkul yang dipilih ke variabel matkul_pilihan
        if matkul.casefold() in nama_matkul_tersedia:
            print()
            temp = [i for i in MATKUL_TERSEDIA if i[0].casefold() == matkul.casefold()]
            matkul_pilihan.extend(temp)

        else:
            print('Matkul tidak ditemukan', "\n")


    elif mode == "2":
        matkul = input("Masukkan nama matkul: ").strip()# meminta user menginput matkul
        nama_matkul_pilihan = [i[0].casefold() for i in matkul_pilihan] # list berisi daftar nama matkul yang diambil

        # conditionals statement untuk menghapus matkul yang dipilih dari variabel matkul_pilihan
        if matkul.casefold() in nama_matkul_pilihan:
            print()
            matkul_pilihan2 = matkul_pilihan[:]
            for i in matkul_pilihan:
                if i[0].casefold() == matkul.casefold():
                    matkul_pilihan2.remove(i)

            matkul_pilihan = matkul_pilihan2[:]

        else:
            print('Matkul tidak ditemukan', "\n")


    elif mode == "3":
        # membuat variabel count untuk menentukan ada tidaknya matkul yang bermasalah
        count = 0 

        # looping untuk menentukan matkul yang bermasalah 
        for matkul in range(len(matkul_pilihan)):
            
            for next_matkul in range(matkul+1,len(matkul_pilihan)):

                if is_intersecting(matkul_pilihan[matkul][1:], matkul_pilihan[next_matkul][1:]):
                    print("   ", matkul_pilihan[matkul][0], "bentrok dengan", matkul_pilihan[next_matkul][0])
                    count += 1
                elif is_intersecting(matkul_pilihan[next_matkul][1:], matkul_pilihan[matkul][1:]):
                    print("   ", matkul_pilihan[matkul][0], "bentrok dengan", matkul_pilihan[next_matkul][0])
                    count += 1

        # ketika tidak ada matkul yang bermasalah
        if count == 0:
            print("Tidak ada mata kuliah yang bermasalah")

        print()


    elif mode == "4":

        # conditionals statements berdasarkan ada tidaknya matkul yang dipilih
        if matkul_pilihan == []:
            print("Tidak ada matkul yang diambil")

        else:
            print("daftar matkul:")
            # mengurutkan matkul yang dipilih berdasarkan start_time-nya
            matkul_pilihan3 = sorted(matkul_pilihan[:], key=take_day)

            # looping untuk memberikan output sesuai format yang ditentukan
            for i in range(len(matkul_pilihan3)):
                # konversi waktu ke format yang mudah dibaca
                hari1 = matkul_pilihan3[i][1]//1440
                jam1 = matkul_pilihan3[i][1]%1440//60
                menit1 = matkul_pilihan3[i][1]%60

                hari2 = matkul_pilihan3[i][2]//1440
                jam2 = matkul_pilihan3[i][2]%1440//60
                menit2 = matkul_pilihan3[i][2]%60

                # conditionals statements untuk menentukan hari
                if hari1 == 0:
                    hari1 = "Senin"
                elif hari1 == 1:
                    hari1 = "Selasa"
                elif hari1 == 2:
                    hari1 = "Rabu"
                elif hari1 == 3:
                    hari1 = "Kamis"
                elif hari1 == 4:
                    hari1 = "Jumat"
                elif hari1 == 5:
                    hari1 = "Sabtu"
                elif hari1 == 6:
                    hari1 = "Minggu"

                if hari2 == 0:
                    hari2 = "Senin"
                elif hari2 == 1:
                    hari2 = "Selasa"
                elif hari2 == 2:
                    hari2 = "Rabu"
                elif hari2 == 3:
                    hari2 = "Kamis"
                elif hari2 == 4:
                    hari2 = "Jumat"
                elif hari2 == 5:
                    hari2 = "Sabtu"
                elif hari2 == 6:
                    hari2 = "Minggu"

                print(f"    {matkul_pilihan3[i][0].upper():<14}{hari1 + ',':<8}{jam1:02}.{menit1:02}   s/d {hari2 + ',':<8}{jam2:02}.{menit2:02}")
            print()

            
    elif mode == "5":
        print('Terima kasih!')
        exit()

    # handling ketika user salah input
    else:
        print("Maaf, pilihan tidak tersedia", "\n")
        
# reference:
# https://stackoverflow.com/questions/60432998/resolve-schedule-conflicts-using-python
# https://stackoverflow.com/questions/942543/operation-on-every-pair-of-element-in-a-list