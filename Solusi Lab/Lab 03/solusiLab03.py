# user input
A = input("Masukkan input himpunan A: ") + ","
B = input("Masukkan input himpunan B: ") + ","

# string untuk output
AxB = "A x B = { "
# menyimpan value string B
copyB = B

# looping untuk membuat cartesian product
while len(A)>0:
    # menyimpan elemen sebelum koma menjadi tempA
    tempA = A[0:A.find(",")]
    A = A[A.find(",")+1:]
    B = copyB
    while len(B)>0:
        # menyimpan elemen sebelum koma menjadi tempB
        tempB = B[0:B.find(",")]
        B = B[B.find(",")+1:]
        # concatenate string
        AxB += f"({tempA}, {tempB}), "

# merapikan dan mencetak output
AxB = AxB[:-2] + " }"
print(AxB)
