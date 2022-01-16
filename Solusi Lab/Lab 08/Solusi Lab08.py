# rantai penyebaran
def rantai_penyebaran(nama_penular): # return string
    # base case: print nama orang sekarang
    hasil = f"- {nama_penular}\n"
    for nama in daftar_terinfeksi[nama_penular]:
        hasil += rantai_penyebaran(nama)

    return hasil
    


# cek penyebaran
def cek_penyebaran(tertular, penular): # cek apakar penular menulari tertular, return value boolean
    # base case: jika tertular == penular, maka return true
    if (tertular == penular):
        return True
    
    hasil = False
    for nama in daftar_terinfeksi[penular]:
        hasil = hasil or cek_penyebaran(tertular, nama)

    return hasil


# main
daftar_terinfeksi = {} # key: penular, value: list orang2 yang tertular secara langsung oleh penular

print("Masukkan rantai penyebaran:")
while True:
    nama = input().split()
    if len(nama) == 0: # Handle input string kosong
        continue
    elif nama[0] == "selesai":
        break
    elif nama[0] in daftar_terinfeksi:
        daftar_terinfeksi[nama[0]].extend(nama[1:]) # Gabung ke list yang sudah ada pada dictionary
    else:
        daftar_terinfeksi[nama[0]] = nama[1:] # Tambahkan ke dictionary

# for i in daftar_terinfeksi:
    # print(i, daftar_terinfeksi[i])


print("\nList perintah:\n1. RANTAI_PENYEBARAN\n2. CEK_PENULARAN\n3. EXIT\n")
while True:
    perintah = input("Masukkan perintah: ").split()

    if len(perintah) == 2 and perintah[0] == "RANTAI_PENYEBARAN":
        if (perintah[1] in daftar_terinfeksi.keys()):
            print(f"Rantai penyebaran {perintah[1]}:")
            print(rantai_penyebaran(perintah[1]))
            
        else:
            print(f"Maaf, nama {perintah[1]} tidak terdapat dalam rantai penyebaran.")
    elif len(perintah) == 3 and perintah[0] == "CEK_PENULARAN":
        if (perintah[2]) in daftar_terinfeksi.keys():
            if perintah[1] in daftar_terinfeksi.keys():
                if perintah[1] == perintah[2] or cek_penyebaran(perintah[1], perintah[2]):
                    print("YA")
                else:
                    print("TIDAK")
            else:
                print(f"Maaf, nama {perintah[1]} tidak terdapat dalam rantai penyebaran.")
        else:
            if perintah[1] in daftar_terinfeksi.keys():
                print(f"Maaf, nama {perintah[2]} tidak terdapat dalam rantai penyebaran.")
            else:
                print(f"Maaf, nama {perintah[1]} dan {perintah[2]} tidak terdapat dalam rantai penyebaran.")
    elif len(perintah) == 1 and perintah[0] == "EXIT":
        print("Goodbye~ Semoga virus KOPIT cepat berakhir.", end="")
        break
    else:
        print("Maaf perintah tidak dkenali. Masukkan perintah yang valid.")
    print()