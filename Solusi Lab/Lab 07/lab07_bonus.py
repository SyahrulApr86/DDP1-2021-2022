# function untuk menampilkan tujuan akhir semua KA
def info_tujuan():
    lst_tujuan = [dict_jadwal[i][1] for i in dict_jadwal]
        # menggunakan set untuk menampung tujuan_akhir kereta agar tidak ada duplikasi
    set_tujuan = set(lst_tujuan)
    for tujuan in set_tujuan:
        print(tujuan)

# function untuk mencari jadwal berdasarkan tujuan dan kelas
def tujuan_kelas(tujuan_akhir, kelas_kereta, termurah):
    if kelas_kereta == "Eksekutif":
        kelas = "1"
    elif kelas_kereta == "Bisnis":
        kelas = "2"
    else:
        kelas = "3"
    jadwal_baru = [x for x in list(dict_jadwal.values()) if x[0][0] == kelas and x[1] == tujuan_akhir]
    if len(jadwal_baru) == 0:
        print("Tidak ada jadwal KA yang sesuai")
    else:
        # mencari jadwal KA termurah sesuai berdasarkan tujuan dan kelas
        if termurah:
            min_harga = min(jadwal_baru, key=lambda x: x[3])
            min_jadwal = [x for x in jadwal_baru if x[3] == min_harga[3]]
            for i in min_jadwal:
                print_jadwal(i)
        else:
            for sub_jadwal in jadwal_baru:
                print_jadwal(sub_jadwal)

# function untuk mencari jadwal berdasarkan tujuan dan jam keberangkatan
def tujuan_jam(tujuan_akhir, jam_keberangkatan, termurah):
    jadwal_baru = [x for x in list(dict_jadwal.values()) if x[1] == tujuan_akhir and int(x[2]) <= int(jam_keberangkatan)]
    if len(jadwal_baru) == 0:
        print("Tidak ada jadwal KA yang sesuai")
    else:
        # mencari jadwal KA termurah sesuai berdasarkan tujuan dan kelas
        if termurah:
            min_harga = min(jadwal_baru, key = lambda x: x[3])
            min_jadwal = [x for x in jadwal_baru if x[3] == min_harga[3]]
            for i in min_jadwal:
                print_jadwal(i)
        else:
            for sub_jadwal in jadwal_baru:
                print_jadwal(sub_jadwal)

# function untuk mencetak jadwal yang diperoleh sesuai format output
def print_jadwal(kumpulan_jadwal):
    nomor_ka, waktu, harga = kumpulan_jadwal[0],  kumpulan_jadwal[2],  kumpulan_jadwal[3]
    print(f"KA {nomor_ka} berangkat pukul {waktu} dengan harga tiket {harga}")

# program utama
# dictionary untuk menyimpan seluruh jadwal KA
dict_jadwal = {}
print("Selamat datang! Silakan masukkan jadwal KA:")
# meminta input jadwal kereta dan berhenti saat dimasukkan input "selesai"

while True:
    jadwal = input()
    if jadwal == "selesai":
        break
    else:
        jadwal = jadwal.split()
        dict_jadwal[jadwal[0]] = [jadwal[0], jadwal[1], jadwal[2], jadwal[3]]

while True:
    print("""Perintah yang tersedia:
1. INFO_TUJUAN
2. TUJUAN_KELAS <tujuan_akhir> <kelas_kereta>
3. TUJUAN_KELAS_TERMURAH <tujuan_akhir> <kelas_kereta>
4. TUJUAN_JAM <tujuan_akhir> <jam_keberangkatan>
5. TUJUAN_JAM_TERMURAH <tujuan_akhir> <jam_keberangkatan>
6. EXIT""")
    # melakukan penanganan sesuai input perintah
    perintah = input("Masukkan perintah: ")
    perintah = perintah.split(" ")
    if perintah[0] == "INFO_TUJUAN" :
        print("KA di stasiun ini memiliki tujuan akhir:")
        info_tujuan()
    elif len(perintah) == 3:
        if perintah[0] == "TUJUAN_KELAS":
            tujuan_kelas(perintah[1], perintah[2], False)
        elif perintah[0] == "TUJUAN_JAM":
            tujuan_jam(perintah[1], perintah[2], False)
        elif perintah[0] == "TUJUAN_KELAS_TERMURAH":
            tujuan_kelas(perintah[1], perintah[2], True)
        elif perintah[0] == "TUJUAN_JAM_TERMURAH":
            tujuan_jam(perintah[1], perintah[2], True)
        else:
            print("Perintah yang dimasukkan tidak valid")
    elif perintah[0] == "EXIT" and len(perintah) == 1:
        print("Terima kasih sudah menggunakan program ini!")
        break
    else :
        print("Perintah yang dimasukkan tidak valid")
    print()
