# import modul modul yang dibutuhkan
from string import punctuation
from collections import Counter
from html_functions import *


print(f"""Program untuk membuat word cloud dari text file
---------------------------------------------
hasilnya disimpan sebagai file html,
yang bisa ditampilkan di browser.
""")

# meminta input nama file dari user
nama_input = input("Silakan masukan nama file: ")
print()

# membaca file stopwords.txt
file_stopwords = open('stopwords.txt', "r")


try: # handling ketika file tidak ada
    file_input = open(nama_input, "r") # membaca file input
except FileNotFoundError:
    print(f"""File input tidak ada :(""")
    print("Program selesai. Tekan enter untuk keluar...")
    exit()
except OSError:
    print("File input tidak ada :(")
    print("Program selesai. Tekan enter untuk keluar...")
    exit()


# memasukkan setiap kata dari teks input pada sebuah list
list_kata = file_input.read().split()
stopwords = file_stopwords.read().split()

# handling ketika file ada tapi kosong
if list_kata == []:
    print("File input ada tapi kosong :(")
    print("Program akan segera diberhentikan...")
    exit()

print(f"{nama_input} :")

# menghilangkan stopwords dari teks dan mengubah semua huruf menjadi huruf kecil
# dan memasukkannya ke dalam list
result_words  = []
for word in list_kata:
    word = word.casefold()
    word = word.strip(punctuation)
    if word not in stopwords:
        result_words.append(word)

result = ' '.join(result_words)

# mengubah list menjadi class Counter
result_words_counter = Counter(result_words)

arranged = []
k = len(result_words_counter)


# mengurutkan setiap elemen di class Counter dan memasukkannya ke dalam list 
# berdasarkan jumlah kemunculan
for w in sorted(result_words_counter.most_common(k), key=(lambda w: w[1]), reverse=True):
    w = list(w)
    arranged.append(w)

# membuat fungsi untuk mengambil karakter pertama
def ambil_huruf_pertama(data):
    return data[0]

# membuat list yang akan diisi kata dengan awalan sama
sub_list = []

# pengurutan dari z-a kata dengan jumlah kemunculan sama 
arranged2 = []
for index_of_arranged in range(len(arranged)):
    sub_list.append(arranged[index_of_arranged])
    try:
        if arranged[index_of_arranged + 1][1] == arranged[index_of_arranged][1]:
            continue

        elif arranged[index_of_arranged + 1][1] != arranged[index_of_arranged][1]:
            arranged_sub_list = sorted(sub_list, key = ambil_huruf_pertama, reverse = True)
            arranged2 += arranged_sub_list
            sub_list = []

    except IndexError:
        arranged_sub_list = sorted(sub_list, key = ambil_huruf_pertama, reverse = True)
        arranged2 += arranged_sub_list
        continue

# handling ketika kata yang unik kurang dari 56
try:
    arranged2 = arranged2[:56]
except IndexError:
    arranged2 = arranged2[:]


print(f"{len(arranged2)} kata diurutkan berdasarkan jumlah kemunculan dalam pasangan ")
print("(jumlah:kata)")
print()

# menentukan kata terpanjang untuk menentukan allignment
maks_word = arranged2[0][1]
min_word = arranged2[-1][1]
max_length = 0
for i in range(0, len(arranged2)):
    length = len(arranged2[i][0])
    if length > max_length:
        max_length = length

# print tabel berukuran 4 x 14
for index in range(0, len(arranged2), 4):
    try:
        kolom1 = f"{arranged2[index][1]:>2}:{arranged2[index][0]}"
        print(f"{kolom1:<{max_length + 10}}", end = "")
    except IndexError:
        pass

    try:
        kolom2 = f"{arranged2[index + 1][1]:>2}:{arranged2[index + 1][0]}"
        print(f"{kolom2:<{max_length + 10}}", end = "")
    except IndexError:
        pass
    
    try:
        kolom3 = f"{arranged2[index + 2][1]:>2}:{arranged2[index + 2][0]}"
        print(f"{kolom3:<{max_length + 10}}", end = "")
    except IndexError:
        pass
    
    try:
        kolom4 = f"{arranged2[index + 3][1]:>2}:{arranged2[index + 3][0]}"
        print(f"{kolom4:<{max_length + 10}}", end = "\n")
    except IndexError:
        pass
    
print()
print()
print('Tekan Enter untuk keluar …')


html = ''
# mengurutkan berdasarkan alfabet
arranged3 = sorted(arranged2, key = ambil_huruf_pertama, reverse = False)

# konversi kata ke HTML tag
for index in range(0, len(arranged3), 4):
    try:
        html += make_HTML_word(arranged3[index][0], arranged3[index][1], maks_word, min_word) + '\n'
    except IndexError:
        pass

    try:
        html += make_HTML_word(arranged3[index + 1][0], arranged3[index + 1][1], maks_word, min_word) + '\n'
    except IndexError:
        pass
    
    try:
        html += make_HTML_word(arranged3[index + 2][0], arranged3[index + 2][1], maks_word, min_word) + '\n'
    except IndexError:
        pass
    
    try:
        html += make_HTML_word(arranged3[index + 3][0], arranged3[index + 3][1], maks_word, min_word) + '\n'
    except IndexError:
        pass

# membuat HTML box
html_box = make_HTML_box(html)
# membuat HTML file
html_file = print_HTML_file(html_box, nama_input)

# menutup file input
file_input.close() 

# https://www.programiz.com/python-programming/methods/string/casefold#:~:text=String%20format_map()-,Python%20String%20casefold(),i.e.%20ignores%20cases%20when%20comparing.
# https://stackoverflow.com/questions/25346058/removing-list-of-words-from-a-string/25346119
# https://www.geeksforgeeks.org/string-punctuation-in-python/
# https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python
# https://kopiding.in/fungsi-sorted-python/