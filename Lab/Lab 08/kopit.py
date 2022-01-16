# fungsi untuk menemukan yang tertular
def rantai(nama, dct):
    # handling jika nama tidak ada dalam dictionary
    if nama not in dct:
        return None

    # base case
    if dct[nama] == []:
        return [nama]
    
    # recursion case
    lst = list()
    for i in dct[nama]:
        lst.append(nama)
        lst.append(i)
        a = rantai(i, dct)
        for b in a:
            lst.append(b)
    return lst


# fungsi untuk mengecek rantai penyebaran
def cek_rantai(tertular, penular, dct):
    # handling jika seorang tidak ada dalam rantai penyebaran
    if penular not in dct and tertular not in dct:
        return (f"Maaf, nama {tertular} dan {penular} tidak ada dalam rantai penyebaran.")
    elif penular not in dct:
        return (f"Maaf, nama {penular} tidak ada dalam rantai penyebaran.")
    elif tertular not in dct:
        return (f"Maaf, nama {tertular} tidak ada dalam rantai penyebaran.")
    
    # membuat daftar orang yang tertular oleh "penular"
    lst_tertular = rantai(penular, dct)
    sets_tertular = set()
    for i in lst_tertular:
        sets_tertular.add(i)

    # mengecek argumen "tertular" apakah ada dalam daftar orang yang tertular oleh "penular"
    if tertular in sets_tertular:
        return "YA"
    else:
        return "TIDAK"

# meminta input rantai penyebaran
print("Masukkan rantai penyebaran:")

# memasukkan rantai penyebaran ke dalam sebuah variabel
rantai_penyebaran = []
while True:
    add_rantai = input().strip()
    if add_rantai == "selesai" or add_rantai == "Selesai":
        break
    else:
        lst_add_rantai = add_rantai.split()

    rantai_penyebaran.append(lst_add_rantai)
print()

# mengubah rantai penyebaran menjadi dict 
# dengan key penular dan values orang yang tertular
dict_rantai_penyebaran = dict()
for i in rantai_penyebaran:
    if len(i) > 1:
        if i[0] in dict_rantai_penyebaran:
            for u in range(1, len(i)):
                dict_rantai_penyebaran[i[0]].append(i[u])
        elif i[0] not in dict_rantai_penyebaran:
            dict_rantai_penyebaran[i[0]] = i[1:]

    elif len(i) == 1:
        dict_rantai_penyebaran[i[0]] = []

# print menu
print("""List perintah:
1. RANTAI_PENYEBARAN
2. CEK_PENULARAN
3. EXIT
""")

# sentinel loop untuk pemilihan menu
while True:
    perintah = input("Masukkan perintah: ").strip() # input perintah
    lst_perintah = perintah.split()

    # jika tidak memasukkan perintah
    if lst_perintah == []:
        print("Maaf perintah tidak dikenali. Masukkan perintah yang valid.\n")

    # jika memilih perintah 1
    elif lst_perintah[0] == "RANTAI_PENYEBARAN":

        # handling jika nama orang tidak ada dalam rantai penyebaran
        if rantai((lst_perintah[1]), dict_rantai_penyebaran) == None:
            print(f"Maaf, nama {lst_perintah[1]} tidak ada dalam rantai penyebaran.\n")
            continue

        # processing list keluaran dari rantai() menjadi sebuah set
        lst_tertular = rantai((lst_perintah[1]), dict_rantai_penyebaran)
        sets_tertular = set()
        for i in lst_tertular:
            sets_tertular.add(i)
        
        # print rantai penyabran
        print(f"Rantai penyebaran {lst_perintah[1]}:")
        for i in sets_tertular:
            print(f"- {i}")
        print()


    # jika memilih perintah 2
    elif lst_perintah[0] == "CEK_PENULARAN":
        print(cek_rantai(lst_perintah[1], lst_perintah[2], dict_rantai_penyebaran))
        print()


    # jika memilih perintah 3
    elif lst_perintah[0] == "EXIT":
        print("Goodbye~ Semoga virus KOPIT cepat berakhir.")
        exit()


    # handling jika input tidak valid
    else:
        print("Maaf perintah tidak dikenali. Masukkan perintah yang valid.\n")

# reference:
# https://stackoverflow.com/questions/57222284/converting-lists-in-list-to-a-list-only-containing-integers-using-recursion