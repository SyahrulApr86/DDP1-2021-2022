print("Selamat datang! Silakan masukkan jadwal KA:")

# Membuat list jadwal untuk menampung jadwal yang diinput
jadwal = []
while True: # looping untuk penginputan jadwal
    add_jadwal = input().strip()
    if add_jadwal == "selesai" or add_jadwal == "Selesai":
        break
    else:
        lst_add_jadwal = add_jadwal.split()

        # Handle jika input tidak sesuai format
        if len(lst_add_jadwal) != 4:
            print('Perintah yang dimasukkan tidak valid.')
            continue

        jadwal.append(lst_add_jadwal)
print()

# print menu
print("""Perintah yang tersedia:
1. INFO_TUJUAN
2. TUJUAN_KELAS <tujuan_akhir> <kelas_kereta>
3. TUJUAN_JAM <tujuan_akhir> <jam_keberangkatan>
4. EXIT
""")

# sentinel loop untuk pemilihan menu
while True:
    perintah = input("Masukkan perintah: ").strip() # input perintah
    lst_perintah = perintah.split()

    # jika diberikan perintah INFO_TUJUAN
    if lst_perintah == ["INFO_TUJUAN"]:
        set_tujuan = {i[1] for i in jadwal}

        print("KA di stasiun ini memiliki tujuan akhir:")
        for i in set_tujuan:
            print(i)
        print()
    
    # Handling jika perintah whitespace, agar tidak error ketika di elif berikutnya
    elif lst_perintah == []:
        print("Perintah yang dimasukkan tidak valid.\n")

    # jika diberikan perintah TUJUAN_KELAS <tujuan_akhir> <kelas_kereta>
    elif lst_perintah[0] == "TUJUAN_KELAS" and len(lst_perintah) == 3:
        # menambah dictionary ke dalam list
        if lst_perintah[2] == "Eksekutif":
            lst_perintah.append({"kelas": "1"})
        elif lst_perintah[2] == "Bisnis":
            lst_perintah.append({"kelas": "2"})
        elif lst_perintah[2] == "Ekonomi":
            lst_perintah.append({"kelas": "3"})
        else:
            print("Perintah yang dimasukkan tidak valid.")
            print()
            continue

        # looping untuk print jadwal
        out = ""
        for kereta in jadwal:
            if lst_perintah[1] == kereta[1] and kereta[0][0] == lst_perintah[3]["kelas"]:
                out += f"KA {kereta[0]} berangkat pukul {kereta[2]} dengan harga tiket {kereta[3]} \n"
        
        # jika tidak ada jadwal yang sesuai
        if out == "":
            print("Tidak ada jadwal KA yang sesuai.\n")
        else:
            print(out)

    # jika diberikan perintah TUJUAN_JAM <tujuan_akhir> <jam_keberangkatan>
    elif lst_perintah[0] == "TUJUAN_JAM" and len(lst_perintah) == 3:
        # looping untuk print jadwal
        out = ""
        for kereta in jadwal:
            if lst_perintah[1] == kereta[1] and int(kereta[2]) <= int(lst_perintah[2]):
                out += f"KA {kereta[0]} berangkat pukul {kereta[2]} dengan harga tiket {kereta[3]}\n"

        # jika tidak ada jadwal yang sesuai
        if out == "":
            print("Tidak ada jadwal KA yang sesuai.\n")
        else:
            print(out)
    
    # jika diberikan perintah EXIT
    elif lst_perintah == ["EXIT"]:
        print("Terima kasih sudah menggunakan program ini!")
        exit()

    # Handling ketika input tidak sesuai
    else:
        print("Perintah yang dimasukkan tidak valid.\n")
