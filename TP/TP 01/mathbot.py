# mengimport modul random agar dapat memasukkan angka random
import random 

print('Halo, selamat datang di Mathbot') 

# perulangan pemilihan mode
while True:
    print('''Pilih Mode:
1. Penjumlahan
2. Pengurangan
3. Campur
4. Akhiri program\n''')

    mode = (input("Masukkan perintah: "))

     # membuat conditionals statement untuk pemilihan mode
    if mode == "1": 
        flag_pilih_kuis = True # membuat flag agar perulangan mudah di break
        print('\nBaik, pilih mode penjumlahan ya, sekarang pilih jenis kuis apa?')
        
        while flag_pilih_kuis: # perulangan pemilihan kuis
            print('''Pilih kuis:
1. Kuis Lepas
2. Kuis 5
3. Ganti mode
4. Akhiri Program''')

            jenis_kuis = (input('\nMasukkan jenis kuis: ')) 
            # membuat conditionals statement untuk jenis kuis yang dipilih
            if jenis_kuis == "1":

                # membuat flag kuis 1 agar perulangan di kuis 1 dapat dibreak dengan mudah
                flag_kuis1 = True 
                while flag_kuis1:
                    numb1 = random.randint(1,10) # membuat variabel untuk diisi angka acak dari rentang 1 - 10 (inklusif)
                    numb2 = random.randint(1,10)
                    print(f'Berapa {numb1} + {numb2}?')
                    jawaban_user = (input('Jawab: '))

                    # conditionals statement, untuk pengecekan jawaban user
                    if jawaban_user.isdigit(): 
                        if jawaban_user == str(numb1 + numb2): 
                            print('Hore benar!\n')
                        else: 
                            print(f'Masih kurang tepat, ya. Jawabannya adalah {numb1 + numb2}\n')

                    
                    elif not jawaban_user.isdigit():  
                        if jawaban_user == "akhiri kuis": 
                            print()
                            flag_kuis1 = False 
                        elif jawaban_user != "akhiri kuis":
                            print('Jawaban tidak valid, hanya menerima jawaban bilangan bulat positif.\n')             

            elif jenis_kuis == "2": 
                skor = 0 # membuat kontainer untuk skor
                for i in range(0,5): # membuat perulangan sebanyak 5x
                    numb1 = random.randint(1,10) # membuat variabel untuk diisi angka acak dari rentang 1 - 10 (inklusif)
                    numb2 = random.randint(1,10)
                    print(f'Berapa {numb1} + {numb2}?')
                    jawaban_user = (input('Jawab: ')) 

                    # conditionals statement, untuk pengecekan jawaban user
                    if jawaban_user.isdigit(): 
                        if jawaban_user == str(numb1 + numb2): 
                            skor += 20 # menambah skor 20
                            print('Hore benar!\n')
                        else: 
                            print(f'Masih kurang tepat, ya. Jawabannya adalah {numb1 + numb2}\n')

                    elif not jawaban_user.isdigit(): 
                        print('Jawaban tidak valid, hanya menerima jawaban bilangan bulat positif.\n')
                    
                print(f'Score kamu: {skor}') # mencetak skor akhir
                print()

            elif jenis_kuis == "3": 
                print()
                flag_pilih_kuis = False
            
            elif jenis_kuis == "4": 
                print('\nTerima kasih telah bermain kuis ini. Sampai jumpa lagi!')
                exit() # function untuk mengakgiri program

            else: # handling jika input dari user adalah karakter selain 1, 2, 3, dan 4
                print("\nInput tidak valid, silakan pilih angka 1 sampai 4\n")
            

    elif mode == "2": 
        flag_pilih_kuis = True # membuat flag agar perulangan mudah di break
        print('\nBaik, pilih mode pengurangan ya, sekarang pilih jenis kuis apa?')
        
        while flag_pilih_kuis: # perulangan pemilihan kuis
            print('''Pilih kuis:
1. Kuis Lepas
2. Kuis 5
3. Ganti mode
4. Akhiri Program''')

            jenis_kuis = (input('\nMasukkan jenis kuis: '))
            if jenis_kuis == "1": # 

                flag_kuis1 = True
                while flag_kuis1:
                    numb1 = random.randint(1,10) # membuat variabel untuk diisi angka acak dari rentang 1 - 10 (inklusif)
                    numb2 = random.randint(1,10)
                    pengurangan = numb1 - numb2 # membuat variabel pengurangan

                    while pengurangan < 0: # handling ketika hasil pengurangan < 0
                        numb1 = random.randint(1,10)
                        numb2 = random.randint(1,10)
                        pengurangan = numb1 - numb2

                    print(f'Berapa {numb1} - {numb2}?')
                    jawaban_user = (input('Jawab: ')) 

                    # conditionals statement, untuk pengecekan jawaban user
                    if jawaban_user.isdigit():
                        if jawaban_user == str(numb1 - numb2): 
                            print('Hore benar!\n')
                        else: 
                            print(f'Masih kurang tepat, ya. Jawabannya adalah {numb1 - numb2}\n')

                    elif not jawaban_user.isdigit():
                        if jawaban_user == "akhiri kuis": 
                            print()
                            flag_kuis1 = False   
                        else: 
                            print('Jawaban tidak valid, hanya menerima jawaban bilangan bulat positif.\n')             

            elif jenis_kuis == "2":
                skor = 0 # membuat kontainer untuk skor
                for i in range(0,5): # membuat perulangan sebanyak 5x
                    numb1 = random.randint(1,10) # membuat variabel untuk diisi angka acak dari rentang 1 - 10 (inklusif)
                    numb2 = random.randint(1,10)
                    pengurangan = numb1 - numb2

                    while pengurangan < 0: # handling ketika hasil pengurangan < 0
                        numb1 = random.randint(1,10)
                        numb2 = random.randint(1,10)
                        pengurangan = numb1 - numb2
                    
                    print(f'Berapa {numb1} - {numb2}?')
                    jawaban_user = (input('Jawab: ')) 

                    # conditionals statement, untuk pengecekan jawaban user
                    if jawaban_user.isdigit(): 
                        if jawaban_user == str(numb1 - numb2): 
                            skor += 20 # menambah skor 20
                            print('Hore benar!\n')
                        else: 
                            print(f'Masih kurang tepat, ya. Jawabannya adalah {numb1 - numb2}\n')

                    elif not jawaban_user.isdigit(): 
                        print('Jawaban tidak valid, hanya menerima jawaban bilangan bulat positif.\n')
                    
                print(f'Score kamu: {skor}') # mencetak skor akhir
                print()

            elif jenis_kuis == "3": 
                print()
                flag_pilih_kuis = False
            
            elif jenis_kuis == "4":
                print('\nTerima kasih telah bermain kuis ini. Sampai jumpa lagi!')
                exit() # function untuk mengakgiri program

            else:  # handling jika input dari user adalah karakter selain 1, 2, 3, dan 4
                print("\nInput tidak valid, silakan pilih angka 1 sampai 4\n")


    elif mode == "3": 
        flag_pilih_kuis = True # membuat flag agar perulangan mudah di break
        print('\nBaik, pilih mode campur ya, sekarang pilih jenis kuis apa?')
        
        while flag_pilih_kuis: # perulangan pemilihan kuis
            print('''Pilih kuis:
1. Kuis Lepas
2. Kuis 5
3. Ganti mode
4. Akhiri Program''')

            jenis_kuis = (input('\nMasukkan jenis kuis: '))
            if jenis_kuis == "1":

                flag_kuis1 = True
                while flag_kuis1:
                    picker = random.randint(1,2) # membuat variabel untuk mengacak penjumlahan dan pengurangan

                    if picker == 1: # jika picker == 1 maka akan menjadi penjumlahan
                        numb1 = random.randint(1,10) 
                        numb2 = random.randint(1,10)
                        print(f'Berapa {numb1} + {numb2}?')
                        jawaban_user = (input('Jawab: '))

                        # pengecekan jawaban user
                        if jawaban_user.isdigit():
                            if jawaban_user == str(numb1 + numb2):
                                print('Hore benar!\n')
                                picker = random.randint(1,2) 
                            else:
                                print(f'Masih kurang tepat, ya. Jawabannya adalah {numb1 + numb2}\n')
                                picker = random.randint(1,2) 

                        elif not jawaban_user.isdigit():
                            if jawaban_user == "akhiri kuis":
                                print()
                                flag_kuis1 = False 
                            elif jawaban_user != "akhiri kuis":
                                print('Jawaban tidak valid, hanya menerima jawaban bilangan bulat positif.\n')
                                picker = random.randint(1,2)  

                    elif picker == 2: # jika picker == 2 maka akan menjadi pengurangan
                        numb1 = random.randint(1,10)
                        numb2 = random.randint(1,10)
                        pengurangan = numb1 - numb2

                        while pengurangan < 0: # handling jika hasilnya negatif
                            numb1 = random.randint(1,10)
                            numb2 = random.randint(1,10)
                            pengurangan = numb1 - numb2

                        print(f'Berapa {numb1} - {numb2}?')
                        jawaban_user = (input('Jawab: '))

                        # pengecekan jawaban user
                        if jawaban_user.isdigit():
                            if jawaban_user == str(numb1 - numb2):
                                print('Hore benar!\n')
                                picker = random.randint(1,2)
                            else:
                                print(f'Masih kurang tepat, ya. Jawabannya adalah {numb1 - numb2}\n')
                                picker = random.randint(1,2)

                        elif not jawaban_user.isdigit():
                            if jawaban_user == "akhiri kuis":
                                print()
                                flag_kuis1 = False   
                            else:
                                print('Jawaban tidak valid, hanya menerima jawaban bilangan bulat positif.\n')
                                picker = random.randint(1,2)                                 

            elif jenis_kuis == "2": 
                skor = 0
                for i in range(0,5): 
                    picker = random.randint(1,2) # membuat variabel untuk mengacak penjumlahan dan pengurangan
                    if picker == 1: # jika picker == 1 maka akan menjadi penjumlahan
                        numb1 = random.randint(1,10)
                        numb2 = random.randint(1,10)
                        print(f'Berapa {numb1} + {numb2}?')
                        jawaban_user = (input('Jawab: '))
                        
                        # pengecekan jawaban user
                        if jawaban_user.isdigit():
                            if jawaban_user == str(numb1 + numb2):
                                print('Hore benar!\n')
                                skor += 20
                                picker = random.randint(1,2) 
                            else:
                                print(f'Masih kurang tepat, ya. Jawabannya adalah {numb1 + numb2}\n')
                                picker = random.randint(1,2) 

                        elif not jawaban_user.isdigit():
                            print('Jawaban tidak valid, hanya menerima jawaban bilangan bulat positif.\n')
                            picker = random.randint(1,2)  

                    elif picker == 2: # jika picker == 2 maka akan menjadi pengurangan
                        numb1 = random.randint(1,10)
                        numb2 = random.randint(1,10)
                        pengurangan = numb1 - numb2

                        while pengurangan < 0: # handling jika pengurangan negatif
                            numb1 = random.randint(1,10)
                            numb2 = random.randint(1,10)
                            pengurangan = numb1 - numb2

                        print(f'Berapa {numb1} - {numb2}?')
                        jawaban_user = (input('Jawab: '))

                        # pengecekan jawaban user
                        if jawaban_user.isdigit():
                            if jawaban_user == str(numb1 - numb2):
                                print('Hore benar!\n')
                                skor += 20
                                picker = random.randint(1,2)
                            else:
                                print(f'Masih kurang tepat, ya. Jawabannya adalah {numb1 - numb2}\n')
                                picker = random.randint(1,2)
                        elif not jawaban_user.isdigit():
                                print('Jawaban tidak valid, hanya menerima jawaban bilangan bulat positif.\n')
                                picker = random.randint(1,2) 

                print(f'Score kamu: {skor}') # menampilkan output skor
                print()

            elif jenis_kuis == "3": 
                print()
                flag_pilih_kuis = False
            
            elif jenis_kuis == "4": 
                print('\nTerima kasih telah bermain kuis ini. Sampai jumpa lagi!')
                exit() # function untuk mengakgiri program

            else: # handling jika input dari user adalah karakter selain 1, 2, 3, dan 4
                print("\nInput tidak valid, silakan pilih angka 1 sampai 4\n")


    elif mode == "4": 
            print('\nTerima kasih telah bermain kuis ini. Sampai jumpa lagi!')
            exit() # function untuk mengakgiri program

    else: # handling ketika input user di pemilihan mode bukan 1, 2, 3, dan 4
        print("\nInput tidak valid, silakan pilih angka 1 sampai 4\n")

# kontributor: Ahmad Harori Zaki Ichsan (Asdos) atas asistensinya