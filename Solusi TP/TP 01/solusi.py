import random

# Daftar mode
mode_text = '''
1. Penjumlahan
2. Pengurangan
3. Campur
4. Akhiri program
'''

# Daftar jenis quiz
jenis = '''
1. Kuis Lepas
2. Kuis 5
3. Ganti mode
4. Akhiri Program
'''

print("Halo, selamat datang di Mathbot")
jalan = True

while jalan:
    print("Pilih Mode: " + mode_text)
    mode = input("Masukkan perintah: ")
    print()

    if mode.isdigit():
        mode = int(mode)
        # Memulai kuis dengan mode penjumlahan
        if mode == 1:
            print("Baik, pilih mode penjumlahan ya, sekarang pilih jenis kuis apa?")    
            while True:   
                print("Pilih kuis: ", jenis)
                jenis_kuis = input("Masukkan jenis kuis: ")
                print()

                if jenis_kuis.isdigit():
                    jenis_kuis = int(jenis_kuis)

                    # Memulai kuis lepas
                    if jenis_kuis == 1:
                        while True:
                            a = random.randint(0,10)
                            b = random.randint(0,10)
                            ans = a + b
                            print("Berapa " + str(a) + " + " + str(b) + "?")
                            user_ans = input("Jawab: ")

                            if user_ans == "akhiri kuis":
                                break
                            else : 
                                if user_ans.isdigit():
                                    if int(user_ans) == ans:
                                        print("Hore benar!")
                                    else :
                                        print("Masih kurang tepat, ya. Jawabannya adalah " + str(ans))
                                else:
                                    print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
                            print()

                    # Memulai kuis 5
                    elif jenis_kuis == 2:
                        score = 0
                        for i in range(1,6):
                            a = random.randint(0,10)
                            b = random.randint(0,10)
                            ans = a+b
                            print("Pertanyaan " + str(i) + ": Berapa " + str(a) + " + " + str(b) + " ?")
                            user_ans = input("Jawab: ")

                            if user_ans.isdigit():
                                if int(user_ans) == ans:
                                    score += 20
                                    print("Hore benar!")
                                else :
                                    print("Masih kurang tepat, ya. Jawabannya adalah " + str(ans))
                            else:
                                print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")

                            print()

                        print("Score kamu: " + str(score))

                    # Mengganti mode kuis          
                    elif jenis_kuis == 3:
                        break
                    
                    # Mengakhiri program
                    elif jenis_kuis == 4:
                        jalan = False
                        break
                    
                    # Nilai jenis_kuis lebih dari 4
                    else:
                        print("Program tidak mengenali perintah yang dimasukkan. Silakan memilih dari perintah yang tersedia.")
                
                # Jenis_kuis bukanlah angka
                else:
                    print("Program tidak mengenali perintah yang dimasukkan. Silakan memilih dari perintah yang tersedia.")
                print()


        # Memulai kuis dengan mode pengurangan
        elif mode == 2:
            print("Baik, pilih mode pengurangan ya, sekarang pilih jenis kuis apa?")
            while True:
                print("Pilih kuis: "  + jenis)
                jenis_kuis = input("Masukkan jenis kuis: ")
                print()

                if jenis_kuis.isdigit():
                    jenis_kuis = int(jenis_kuis)
                    # Memulai kuis lepas
                    if jenis_kuis == 1:
                        while True:
                            a = random.randint(0,10)
                            b = random.randint(0,10)
                            
                            # Bila a lebih kecil dari b, maka nilai perlu di tukar
                            if a < b:
                                a, b = b, a
                            print("Berapa " + str(a) + " - " + str(b) + "?")
                            user_ans = input("Jawab: ")
                            ans = a-b

                            # Apabila user ingin mengakhiri kuis
                            if user_ans == "akhiri kuis":
                                break

                            else: 
                                if user_ans.isdigit():
                                    # Jawaban benar
                                    if int(user_ans) == ans:
                                        print("Hore benar!")
                                    # Jawaban salah
                                    else :
                                        print("Masih kurang tepat, ya. Jawabannya adalah " + str(ans))
                                else:
                                    print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
                            
                            print()

                    # Memulai kuis 5
                    elif jenis_kuis == 2:
                        score = 0
                        for i in range(1, 6):
                            a = random.randint(0,10)
                            b = random.randint(0,10)

                            # Bila a lebih kecil dari b, maka nilai perlu di tukar
                            if a < b:
                                a, b = b, a
                            print("Pertanyaan " + str(i) + ": Berapa " + str(a) + " - " + str(b) + " ?")
                            user_ans = input("Jawab: ")
                            ans = a-b

                            if user_ans.isdigit():
                                # Jawaban benar
                                if int(user_ans) == ans:
                                    score += 20
                                    print("Hore benar!")
                                # Jawaban salah
                                else :
                                    print("Masih kurang tepat, ya. Jawabannya adalah " + str(ans))
                            else:
                                print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")

                            print()

                        print("Skor kamu adalah ", score)
                        
                    # Mengganti mode kuis
                    elif jenis_kuis == 3:
                        break

                    # Mengakhiri Program
                    elif jenis_kuis == 4:
                        jalan = False
                        break
                    
                    # Nilai jenis_kuis lebih dari 4
                    else:
                        print("Program tidak mengenali perintah yang dimasukkan. Silakan memilih dari perintah yang tersedia.")

                # Jenis_kuis bukanlah angka
                else:
                    print("Program tidak mengenali perintah yang dimasukkan. Silakan memilih dari perintah yang tersedia.")
                print()


        # Campur
        elif mode == 3:
            print("Baik, pilih mode campur ya, sekarang pilih jenis kuis apa?")
            while True:
                print("Pilih kuis: "  + jenis)
                jenis_kuis = input("Masukkan jenis kuis: ")
                print()

                if jenis_kuis.isdigit():
                    jenis_kuis = int(jenis_kuis)
                # Memulai kuis lepas
                    if jenis_kuis == 1:
                        while True:
                            a = random.randint(0,10)
                            b = random.randint(0,10)
                            operator = random.randint(0,10)

                            if operator < 5:
                                print("Berapa " + str(a) + " + " + str(b) + "?")
                                user_ans = input("Jawab: ")
                                ans = a+b

                                # Apabila user ingin mengakhiri kuis
                                if user_ans == "akhiri kuis":
                                    break

                                else:
                                    if user_ans.isdigit():
                                    # Jawaban benar
                                        if int(user_ans) == ans:
                                            print("Hore benar!")
                                        # Jawaban salah
                                        else :
                                            print("Masih kurang tepat, ya. Jawabannya adalah " + str(ans))
                                    else:
                                        print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")

                            else:
                            # Bila a lebih kecil dari b, maka nilai perlu di tukar
                                if a < b:
                                    a, b = b, a

                                print("Berapa " + str(a) + " - " + str(b) + "?")
                                user_ans = input("Jawab: ")
                                ans = a-b

                                # Bila a lebih kecil dari b, maka nilai perlu di tukar
                                if user_ans == "akhiri kuis":
                                    break

                                else:
                                    if user_ans.isdigit():
                                        # Jawaban benar
                                        if int(user_ans) == ans:
                                            print("Hore benar!")
                                        # Jawaban salah
                                        else :
                                            print("Masih kurang tepat, ya. Jawabannya adalah " + str(ans))
                                    else:
                                        print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")
                            print()

                    # Memulai kuis 5
                    elif jenis_kuis == 2:
                        score = 0
                        for i in range(1,6):
                            a = random.randint(0,10)
                            b = random.randint(0,10)
                            operator = random.randint(0,10)

                            # Operasi Penjumlahan
                            if operator < 5:
                                print("Pertanyaan " + str(i) + ": Berapa " + str(a) + " + " + str(b) + " ?")
                                user_ans = input("Jawab: ")
                                ans = a+b

                                if user_ans.isdigit():
                                    # Jawaban benar
                                    if int(user_ans) == ans:
                                        score += 20
                                        print("Hore benar!")
                                    # Jawaban salah
                                    else :
                                        print("Masih kurang tepat, ya. Jawabannya adalah " + str(ans))
                                else:
                                    print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")

                            # Operasi Pengurangan
                            else:
                                # Bila a lebih kecil dari b, maka nilai perlu di tukar
                                if a < b:
                                    a, b = b, a
                                print("Pertanyaan " + str(i) + ": Berapa " + str(a) + " - " + str(b) + " ?")
                                user_ans = input("Jawab: ")
                                ans = a-b

                                if user_ans.isdigit():
                                    # Jawaban benar
                                    if int(user_ans) == ans:
                                        score += 20
                                        print("Hore benar!")
                                    # Jawaban salah
                                    else :
                                        print("Masih kurang tepat, ya. Jawabannya adalah " + str(ans))
                                else:
                                    print("Jawaban tidak valid, hanya menerima jawaban bilangan bulat.")

                            print()

                        print("Skor kamu adalah " + str(score))
                        print()

                    # Mengganti mode kuis
                    elif jenis_kuis == 3:
                        break

                    # Mengakhiri program
                    elif jenis_kuis == 4:
                        jalan = False
                        break
                    
                    # Nilai jenis_kuis lebih dari 4
                    else:
                        print("Program tidak mengenali perintah yang dimasukkan. Silakan memilih dari perintah yang tersedia.")
                
                # Jenis_kuis bukanlah angka
                else:
                    print("Program tidak mengenali perintah yang dimasukkan. Silakan memilih dari perintah yang tersedia.")
                print()

        # Mengakhiri program
        elif mode == 4:
            jalan = False
            break
        
        # Nilai mode lebih dari 4
        else:
            print("Program tidak mengenali perintah yang dimasukkan. Silakan memilih dari perintah yang tersedia.")
    
    # Mode bukanlah angka
    else:
        print("Program tidak mengenali perintah yang dimasukkan. Silakan memilih dari perintah yang tersedia.")
    print()
    
print("Terima kasih telah bermain kuis ini. Sampai jumpa lagi!")