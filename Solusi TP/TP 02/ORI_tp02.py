#Author: Ahmad Harori Zaki Ichsan

import string
import html_functions as html


# Take input of the input text name

header = '''Program untuk membuat word cloud dari text file
---------------------------------------------
hasilnya disimpan sebagai file html,
yang bisa ditampilkan di browser.

'''

print(header)

file_input = input("Silakkan masukkan nama file: ")
stop_words = []
count_words = []

print("\n")

# Puts all stop word into stopWords list
with open(file="stopwords.txt") as file:
    stop_words_file = file.readlines()
    for word in stop_words_file:
        stop_words.append(word.strip()) # Remove all whitespaces

# Read text from the input text
with open(file=file_input) as file:
    text_per_line = file.readlines()

# Iterate per line
for line in text_per_line:
    words_per_line = line.split()

    # Iterate per word
    for word in words_per_line:

        # Remove any leading and/or trailing punctuation
        clean_word = word.strip(string.punctuation).lower()
     
        if clean_word not in stop_words: # Count this word only if it's not a stop word
            is_in_count_words = False
            for index in range(len(count_words)):
                # If the word exist in countWords, add the count of that word
                if count_words[index][1] == clean_word: 
                    is_in_count_words = True
                    count_words[index][0] += 1
                    break

            # If the word doesn't exist in countWords, append to countWords and set the count to 1
            if not is_in_count_words:
                count_words.append([1,clean_word])

# Sort countWords based on the count in descending order
count_words.sort(reverse=True)

# Prints the output to terminal 
print(f"{file_input} :")
print("56 kata diurutkan berdasarkan jumlah kemunculan dalam pasangan (jumlah:kata)\n")
for i in range(56):
    if ((i + 1) % 4) == 0:
        print("{:>2}:{:<13}".format(count_words[i][0],count_words[i][1]))
    else:
        print("{:>2}:{:<13}".format(count_words[i][0],count_words[i][1]), end="")

# Take the top 56 of countWords
top_56 = count_words[:56]

# Get the highest and lowest count
highest_count = top_56[0][0]
lowest_count = top_56[-1][0]

# Adapted from 
# https://www.geeksforgeeks.org/python-sort-list-according-second-element-sublist/
def Sort(li):
  
    '''
    Sort the list based on the index 1 of its sublist
    Required -- li (list) to be sorted
    '''
    return(sorted(li, key = lambda x: x[1]))

# Sorts the list alphabetically
sort_alphabet = Sort(top_56)

# Container for the body of html
body = ""

# Puts HTML tag into each words and concatenate them all
for c,w in sort_alphabet:
    body += html.make_HTML_word(w,c,highest_count,lowest_count) + " "

# Generate the HTML file
html.print_HTML_file(html.make_HTML_box(body), file_input)

print()
input("Tekan enter untuk keluar...")