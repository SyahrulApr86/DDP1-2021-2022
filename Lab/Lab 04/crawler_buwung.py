# program meminta user memasukkan nama file input dan output
nama_input = input("Masukkan nama file input: ")
nama_otput = input("Masukkan nama file output: ")

try: # handling ketika file tidak ada
    file_input = open(nama_input, "r") # membaca file input
except FileNotFoundError:
    print("File input tidak ada :(")
    print("Program selesai. Tekan enter untuk keluar...")
    exit()

# kontainer untuk menampung bermacam variabel
# yang akan diisi secara dinamis
list_baris_baru = []
jumlah_mention = 0
jumlah_hashtag = 0
jumlah_url = 0

list_baris = file_input.read().split("\n") # memisahkan tiap baris menjadi list

# conditional statement jika file ada tapi kosong
if list_baris == ['']:
    print("File input ada tapi kosong :(")
    print("Program selesai. Tekan enter untuk keluar...")
    exit()
else:
    file_output = open(nama_otput, "w") # menulis file output

    for baris_ke in range(0, len(list_baris)): # iterasi tiap baris
        list_kata = list_baris[baris_ke].split(' ')
        baris_baru = []

        try: # handling ketika baris kosong
            for kata in list_kata: # iterasi tiap kata dalam tiap baris
                if kata[0] == "@":
                    baris_baru += ["(M)"]
                    jumlah_mention += 1
                elif kata[0] == "#":
                    baris_baru += ["(H)"]
                    jumlah_hashtag += 1
                elif kata[0:4] == "www.":
                    baris_baru += ["(U)"]
                    jumlah_url += 1
                else:
                    baris_baru += [kata]

            baris_baru =" ".join(baris_baru) # membuat baris baru
            list_baris_baru += [baris_baru] # memasukkan baris baru ke list

        except IndexError:
            continue

    mention_baru = '\n'.join(list_baris_baru)  # menggabungkan baris-baris yang ada dalam list

    # menulis output pada file output
    print(f"""{mention_baru} 

###############
Mention : {jumlah_mention:>5}
Hashtag : {jumlah_hashtag:>5}
Url     : {jumlah_url:>5}""", file = file_output)

    # menutup file output
    file_output.close()

# menutup file input
file_input.close() 

print(f"""Output berhasil ditulis pada {nama_otput}
Program selesai. Tekan enter untuk keluar...""")
