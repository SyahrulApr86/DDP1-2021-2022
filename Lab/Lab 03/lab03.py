himp_a = input('Masukkan input himpunan A: ') # program meminta input himpunan dari user
himp_a += ',' # menambahkan koma di akhir string himp_a agar dapat slicing sampai karakter terakhir
jumlah_koma_a = himp_a.count(',') 

himp_b = input('Masukkan input himpunan B: ')
himp_b += ',' 
jumlah_koma_b = himp_b.count(',')

AxB = '{' # variabel untuk menampung elemen A x B

indeks_awal_a = 0 
for i in range(0, jumlah_koma_a): # membuat for loop untuk mengiterasi tiap karakter dari string himp_a
    anggota_A = '' 
    indeks_koma_a = himp_a.index(',', indeks_awal_a) 
    
    anggota_A += himp_a[indeks_awal_a: indeks_koma_a] 

    indeks_awal_a = indeks_koma_a + 1 
    
    indeks_awal_b = 0 
    for o in range(0, jumlah_koma_b): # membuat for loop untuk mengiterasi tiap karakter dari string himp_b
        anggota_B = '' 
        indeks_koma_b = himp_b.index(',', indeks_awal_b) 
    
        anggota_B += himp_b[indeks_awal_b: indeks_koma_b] 
    
        indeks_awal_b = indeks_koma_b + 1 

        anggota_AxB = f"({anggota_A},{anggota_B})" 
        AxB += anggota_AxB + ', ' 

AxB = AxB[:-2] +  '}' # menambah kurung kurawal untuk menutup himpunan

print(f"A x B = {AxB}") # memberi output berupa himpunan AxB