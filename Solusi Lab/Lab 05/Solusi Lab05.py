# Initial value
happiness = 50
sadness = 50
anger = 50

# Menambah nilai happiness dan mengurangi nilai sadness
def smile():
    global happiness, sadness
    happiness = min(100, happiness + 9)
    sadness = max(0, sadness - 6)

# Menambah nilai sadness dan mengurangi nilai anger
def sad():
    global sadness, anger
    sadness = min(100, sadness + 10)
    anger = max(0, anger - 8)

# Menambah nilai anger dan mengurangi nilai happiness
def angry():
    global anger, happiness
    anger = min(100, anger + 13)
    happiness = max(0, happiness - 5)
    

try:
    file_input = input("Masukkan nama file input: ")
    with open(file_input, "r", encoding="utf-8") as file:
        chats = file.read()
        
        # Jika file kosong, keluar
        if len(chats) == 0:
            print("File ada tapi kosong :(")
            exit()
        
        chats = chats.split("\n")

        # Mengganti keyword dengan emoticon
        for i in range(len(chats)):
            words = chats[i].split()
            for j in range(len(words)):
                if words[j] == "(smile)":
                    if words[0] == "Pak":
                        smile()
                    words[j] = "\U0001f603"
                elif words[j] == "(sad)":
                    if words[0] == "Pak":
                        sad()
                    words[j] = "\U0001f622"
                elif words[j] == "(angry)":
                    if words[0] == "Pak":
                        angry()
                    words[j] = "\U0001f621"
            chats[i] = words
        
        # Mencetak hasil chat dengan emoticon
        print()
        for chat in chats:
            print(" ".join(chat))

        print("\nMengukur suasana hati...\n")
        print("#### Hasil Pengukuran ####")
        print(f"Happiness = {happiness} | Sadness = {sadness} | Anger = {anger}\n")
        print("#### Kesimpulan ####")

        # Kesimpulan berdasarkan nilai happiness, sadness, dan anger
        if happiness == sadness == anger:
            print("Kesimpulan tidak ditemukan.")
        elif happiness > anger and happiness > sadness:
            print("Pak Chanek sedang bahagia.")
        elif sadness > anger and sadness > happiness:
            print("Pak Chanek sedang sedih.")
        elif sadness == happiness:
            print("Pak Chanek sedang sedih atau bahagia.")
        elif sadness == anger:
            print("Pak Chanek sedang sedih atau marah.")
        elif happiness == anger:
            print("Pak Chanek sedang senang atau marah.")
        else:
            print("Pak Chanek sedang marah.")

except FileNotFoundError:
    print("File tidak ada :(")