input_name = input("Masukkan nama file input: ")
output_name = input("Masukkan nama file output: ")

try:
    input_file = open(input_name, "r")
    output_file = open(output_name, "w")

    count_mention = 0
    count_hashtag = 0
    count_url = 0

    if len(open(input_name, "r").read()) == 0:
        print("File input ada tapi kosong :(")
    else:
        # File dibaca perbaris
        for line in input_file:
            output = ""
            idx = 0

            while(idx < len(line)):
                if line[idx] == "@":
                    output += "(M)"
                    count_mention += 1
                elif line[idx] == "#":
                    output += "(H)"
                    count_hashtag += 1
                elif line[idx:idx + 4] == "www.":
                    output += "(U)"
                    count_url += 1
                else:
                    output += line[idx]
                    idx += 1
                    continue

                # Lanjut ke kata berikutnya
                while line[idx] != ' ' and line[idx] != "\n":
                    idx += 1
                    if idx == len(line): break

            print(output, end = "", file = output_file)

        print(file = output_file)
        print(  f"\n##############\n"
              + f"Mention :{count_mention:5d}\n"
              + f"Hashtag :{count_hashtag:5d}\n"
              + f"Url     :{count_url:5d}", file=output_file)
        
        print(f"Output berhasil ditulis pada {output_name}")

except FileNotFoundError:
    print("File input tidak ada :(")

finally:
    input("Program selesai. Tekan enter untuk keluar...")
