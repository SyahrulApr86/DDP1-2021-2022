print("Selamat datang di Kalkulator IPK!")
jumlah_mk = int(input("Masukkan jumlah mata kuliah: ")) #sistem meminta input kepada user  

while jumlah_mk < 0: # membuat handling ketika user memasukkan angka negatif
    print("Input yang Anda masukkan tidak valid, silakan masukkan ulang.")
    jumlah_mk = int(input("Masukkan jumlah mata kuliah:  "))

# membuat conditionals statement agar ketika user menginput 0 pada jumlah mata kuliah
# maka program akan terhenti

if jumlah_mk == 0:
    print("Tidak ada mata kuliah yang diambil.")
else:
    # membuat beberapa variabel yang nantinya akan dimasukkan nilai-nilai secara dinamis

    jumlah_sks = 0 
    jumlah_sks_lulus = 0
    jumlah_mutu = 0 
    jumlah_mutu_lulus = 0

    # membuat perulangan "for" agar sistem dapat meminta user memasukkan mata kuliah, 
    # jumlah sks, dan nilai mata kuliah sebanyak input user di awal

    for i in range(jumlah_mk):
        print()
        mk = input(f"Masukkan nama mata kuliah ke-{i + 1}: ") # meminta user menginput nama mata kuliah 

        sks_mk = int(input(f"Masukkan jumlah SKS {mk}: ")) # meminta user menginput jumlah sks mata kuliah "mk"

        while sks_mk < 0:  # membuat handling ketika user memasukkan angka negatif
            print("Input yang Anda masukkan tidak valid, silakan masukkan ulang.")
            sks_mk = int(input(f"Masukkan jumlah SKS {mk}: "))

        nilai_mk = float(input("Masukkan nilai yang kamu dapatkan: ")) # meminta user menginput nilai mata kuliah "mk"

        while nilai_mk < 0: # membuat handling ketika user memasukkan angka negatif
            print("Nilai yang kamu masukkan tidak valid, silakan masukkan ulang.")
            nilai_mk = float(input("Masukkan nilai yang kamu dapatkan: ")) 

    # membuat conditionals statement untuk mengklasifikasikan nilai mata kuliah 
    # sesuai dengan bobot dan status kelulusan 

        if 85 <= nilai_mk:
            bobot = 4.00
            status = "lulus"
        elif 80 <= nilai_mk < 85:
            bobot = 3.70
            status = "lulus"
        elif 75 <= nilai_mk < 80:
            bobot = 3.30
            status = "lulus"
        elif 70 <= nilai_mk < 75:
            bobot = 3.00
            status = "lulus"
        elif 65 <= nilai_mk < 70:
            bobot = 2.70
            status = "lulus"
        elif 60 <= nilai_mk < 65:
            bobot = 2.30
            status = "lulus"
        elif 55 <= nilai_mk < 60:
            bobot = 2.00
            status = "lulus"
        elif 40 <= nilai_mk < 55:
            bobot = 1.00
            status = "tidak lulus"
        elif 0 <= nilai_mk < 40:
            bobot = 0.00
            status = "tidak lulus"

    # mengisi variabel yang telah ditetapkan di awal 

        jumlah_sks += sks_mk
        mutu_mk = sks_mk * bobot
        jumlah_mutu += mutu_mk

        if status == "lulus":
            jumlah_sks_lulus += sks_mk
            jumlah_mutu_lulus += mutu_mk

    # handling ZeroDivisionError ketika user tidak lulus dalam semua sks

    if jumlah_sks_lulus == 0:
        ipk = 0
    else:
        ipk = jumlah_mutu_lulus / jumlah_sks_lulus

    # memberi output pada user sesuai yang telah di tetapkan 

    print(f"\nJumlah SKS lulus : {jumlah_sks_lulus} / {jumlah_sks}")
    print(f"Jumlah mutu lulus: {jumlah_mutu_lulus:.2f} / {jumlah_mutu:.2f}")
    print(f"Total IPK kamu adalah {ipk:.2f}")
    print(f"Total IPT kamu adalah {jumlah_mutu / jumlah_sks:.2f}")