# program meminta user memasukkan nama file input
nama_input = input("Masukkan nama file input: ")

try: # handling ketika file tidak ada
    file_input = open(nama_input, "r") # membaca file input
except FileNotFoundError:
    print("File input tidak ada :(")
    print("Program akan segera diberhentikan...")
    exit()

# membaca file dan membuat list baris
baca = file_input.read() 
list_baris = baca.splitlines()
list_baris_baru = []

# kontainer untuk aspek mood
happiness = 50
sadness = 50
anger = 50

# funtion untuk perubahan aspek mood
def smile():
    global happiness
    global sadness
    happiness += 9
    sadness -= 6

def sad():
    global sadness
    global anger
    sadness += 10
    anger -= 8

def angry():
    global anger
    global happiness
    anger += 13
    happiness -= 5

# function apabila aspek mood diluar jangkauan
def maks_min_mood(mood):
    if mood > 100:
        mood = 100
    if mood < 0:
        mood = 0
    return mood

# conditional statement jika file ada tapi kosong
if list_baris == []:
    print("File input ada tapi kosong :(")
    print("Program akan segera diberhentikan...")
    exit()

else:
    for baris_ke in range(0, len(list_baris)): # iterasi tiap baris
        list_kata = list_baris[baris_ke].split(' ')
        baris_baru = []

        try: # handling ketika baris kosong
            # conditional statement untuk pengirim chat
            if list_kata[0] == 'Pak' and list_kata[1] == 'Chanek:':
                for kata in list_kata: # iterasi tiap kata dalam tiap baris
                    if kata == "(smile)":
                        baris_baru += ["\U0001f603"]
                        smile()
                    elif kata == "(sad)":
                        baris_baru += ["\U0001f622"]
                        sad()
                    elif kata == "(angry)":
                        baris_baru += ["\U0001f621"]
                        angry()
                    else:
                        baris_baru += [kata]
            
            else: 
                for kata in list_kata: # iterasi tiap kata dalam tiap baris
                    if kata == "(smile)":
                        baris_baru += ["\U0001f603"]
                    elif kata == "(sad)":
                        baris_baru += ["\U0001f622"]
                    elif kata == "(angry)":
                        baris_baru += ["\U0001f621"]
                    else:
                        baris_baru += [kata]

            baris_baru =" ".join(baris_baru) # membuat baris baru
            list_baris_baru += [baris_baru] # memasukkan baris baru ke list

        except IndexError:
            continue

    chat_baru = '\n'.join(list_baris_baru)  # menggabungkan baris-baris yang ada dalam list


happiness = maks_min_mood(happiness)
sadness = maks_min_mood(sadness)
anger = maks_min_mood(anger)

# conditional statement untuk pengambilan kesimpulan
if happiness > sadness and happiness > anger:
    kesimpulan = "Pak Chanek sedang bahagia."
elif sadness > happiness and sadness > anger:
    kesimpulan = "Pak Chanek sedang sedih."
elif anger > happiness and anger > sadness:
    kesimpulan = "Pak Chanek sedang marah."
elif happiness == sadness and happiness > anger:
    kesimpulan = "Pak Chanek sedang bahagia atau sedih."
elif happiness == anger and happiness > sadness:
    kesimpulan = "Pak Chanek sedang bahagia atau marah."
elif sadness == anger and sadness > happiness:
    kesimpulan = "Pak Chanek sedang sedih atau marah."
elif sadness == anger == happiness:
    kesimpulan = "Kesimpulan tidak ditemukan."

# output
print(f"""
{chat_baru}

Mengukur suasana hati....

##### Hasil Pengukuran #####
Happiness = {happiness} | Sadness = {sadness} | Anger = {anger}

##### Kesimpulan #####
{kesimpulan}""")

file_input.close() 