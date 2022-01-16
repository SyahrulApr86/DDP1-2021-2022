# Membuat class user
class User() :
    def __init__(self, user_name, tipe):
        """
        Constructor untuk class User
        """
        self.__user_name = user_name
        self.__tipe = tipe
    
    # Getter dan Setter
    def get_name(self):
        return self.__user_name

    def get_tipe(self):
        return self.__tipe

# membuat kelas seller yang merupakan inheritance dari kelas user
class Seller(User) : 
    def __init__(self, user_name):
        """
        Constructor untuk class Seller
        """
        # constructor untuk Seller
        super().__init__(user_name, "SELLER")
        self.__pemasukan = 0
        self.list_barang_jual = []

    # Getter dan Setter
    def get_pemasukan(self) : 
        return self.__pemasukan

    def set_pemasukan(self, uang) : 
        self.__pemasukan += uang

    # fungsi untuk menambahkan produk milik objek
    def tambah_product(self, barang, harga, stok):
        # menambahkan objek product ke dalam list produk sendiri dan list semua produk
        list_product.append(Product(nama = barang, harga = int(harga), stock = int(stok), seller = self.get_name()))
        self.list_barang_jual.append(Product(nama = barang, harga = int(harga), stock = int(stok), seller = self.get_name()))
        self.list_barang_jual = sorted(self.list_barang_jual)

    # fungsi untuk menampilkan daftar produk milik objek
    def lihat_produk_jualan_saya(self) : 
        print("\nBerikut merupakan barang jualan saya")
        print("-------------------------------------")
        print("  Nama Produk   |   Harga   |  Stock ")
        print("-------------------------------------")
        # iterasi untuk menampilkan data objek produk milik sendiri
        for product in self.list_barang_jual : 
            print(f"{product.get_nama():<16}|{product.get_harga():<11}|{product.get_stock():<7}")
        print("-------------------------------------\n")

    # fungsi untuk menampilkan menu Seller
    def menu(self) : 
        global main_flag
        print(f"Selamat datang {self.get_name()},")
        print("berikut menu yang bisa Anda lakukan:")
        print("1. TAMBAHKAN_PRODUK")
        print("2. LIHAT_DAFTAR_PRODUK_SAYA")
        print("3. LOG_OUT")
        print()

        # loop untuk pemilihan perintah di kelas seller
        while True:
            print(f"Pemasukan anda {self.__pemasukan},")
            perintah = input("Apa yang ingin Anda lakukan? ")

            # perintah 1 menambah produk sendiri
            if perintah == "1":
                input_produk = input("Masukkan data produk : ")
                print()
                produk = input_produk.split()

                # handling jika produk sudah ada dalam list produk sendiri
                if produk[0] in self.list_barang_jual:
                    print("Produk sudah pernah terdaftar.")
                    break

                self.tambah_product(produk[0], produk[1], produk[2])
            
            # perintah 2 menampilkan list produk sendiri
            elif perintah == "2":
                self.lihat_produk_jualan_saya()

            # perintah 3 keluar akun 
            elif perintah == "3":
                print(f"Anda telah keluar dari akun {self.get_name()}\n")
                main_flag = False
                break
                

# membuat kelas Buyer yang merupakan inheritance dari kelas user
class Buyer(User) : 
    # Constructor untuk kelas Buyer
    def __init__(self, user_name, saldo):
        """
        Constructor untuk class Buyer
        """
        super().__init__(user_name, "BUYER")
        self.__saldo = saldo
        self.list_barang_beli = []

    # Getter dan setter
    def get_saldo(self) : 
        return self.__saldo

    def set_saldo(self, uang) : 
        self.__saldo -= uang

    # fungsi untuk membeli product
    def beli_product(self, barang, harga, penjual):
        self.set_saldo(int(harga)) # mengubah saldo Buyer
        get_user(penjual, list_user).set_pemasukan(int(harga)) # mengubah pemasukan Seller
        
        # mengubah stok produk pada daftar produk Seller
        for i in get_user(penjual, list_user).list_barang_jual:
            if i.get_name() == get_product(barang).get_name():
                i.set_stock()
                
        # mengubah stok produk pada daftar produk keseluruhan
        get_product(barang).set_stock()
        self.list_barang_beli.append(barang) #manambahkan barang ke list barang yang dibeli
        self.list_barang_beli = sorted(self.list_barang_beli)

    # fungsi untuk menampilkan daftar produk yang ada di Dekdepedia
    def lihat_semua_produk(self):
        global list_product
        print("Berikut merupakan daftar produk di Dekdepedia")
        print("-----------------------------------------------")
        print("  Nama Produk  |   Harga   | Stock |  Penjual")
        print("-----------------------------------------------")
        list_product = sorted(list_product)
        # iterasi untuk menampilkan data semua produk di Dekdepedia
        for product in list_product:
            print(f"{product.get_nama():<15}|{product.get_harga():<11}|{product.get_stock():<7}|{product.get_seller():<9}")
        print("-----------------------------------------------\n")

    # fungsi untuk menampilkan daftar produk yang dibeli oleh objek
    def riwayat_pembelian_saya(self):
        print("\nBerikut merupakan barang yang saya beli")
        print("----------------------------------------")
        print(" Nama Produk   |   Harga   |  Penjual")
        print("----------------------------------------")
        # iterasi untuk menampilkan riwayat pembelian Buyer
        for product in self.list_barang_beli:
            print(f"{get_product(product).get_nama():<15}|{get_product(product).get_harga():<11}|{get_product(product).get_seller():<9}")
        print("----------------------------------------\n")

    # fungsi untuk menampilkan menu Buyer
    def menu(self) : 
        global main_flag
        global list_product
        print(f"Selamat datang {self.get_name()},")
        print("berikut menu yang bisa Anda lakukan:")
        print("1. LIHAT_SEMUA_PRODUK")
        print("2. BELI_PRODUK")
        print("3. RIWAYAT_PEMBELIAN_SAYA")
        print("4. LOG_OUT")
        print()

        # loop untuk pemilihan perintah di kelas Buyer
        while True:
            print(f"Saldo anda {self.__saldo},")
            perintah = input("Apa yang ingin Anda lakukan? ")

            # perintah 1 menampilkan semua produk di Dekdepedia
            if perintah == "1":
                print()
                self.lihat_semua_produk()

            # perintah 2 membeli barang
            elif perintah == "2":
                barang = input("Masukkan barang yang ingin dibeli : ")
                barang = get_product(barang)

                # conditionals sesuai status dari keterdiaan barang, saldo, dan stok
                if barang.get_stock() == 0:
                    print("Maaf, stok produk telah habis.\n")

                elif barang not in list_product:
                    print(f"Barang dengan nama {barang} tidak ditemukan dalam Dekdepedia.")

                elif barang.get_harga() > self.__saldo:
                    print(f"Maaf, saldo Anda tidak cukup untuk membeli {barang.get_nama()}.\n")

                else:
                    print(f"Berhasil membeli {barang.get_nama()} dari {barang.get_seller()}.\n")
                    self.beli_product(barang.get_nama(), barang.get_harga(), barang.get_seller())
                    
            # perintah 3 melihat riwayat pembelian buyer
            elif perintah == "3":
                print()
                self.riwayat_pembelian_saya()

            # perintah 4 keluar dari akun Buyer
            elif perintah == "4":
                print(f"Anda telah keluar dari akun {self.get_name()}\n")
                main_flag = False
                break

# membuat class product
class Product() : 
    def __init__(self, nama, harga, stock, seller):
        self.__nama = nama
        self.__harga = harga
        self.__stock = stock
        self.__seller = seller

    # Getter dan Setter
    def get_nama(self):
        return self.__nama

    def get_name(self):
        return self.__nama
    
    def get_harga(self):
        return self.__harga

    def get_stock(self):
        return self.__stock

    def set_stock(self):
        self.__stock -= 1

    def get_seller(self):
        return self.__seller

    # membuat fungsi less than agar bisa membandingkan objek
    def __lt__(self, other):
        self_mag = self.get_nama()
        other_mag = other.get_nama()
        return self_mag < other_mag

# inisiasi kontainer
list_user = []
list_product = []
list_nama_user = []


# fungsi untuk mendapatkan user dan produk yang dibutuhkan
def get_user(name, list_user):
    """
    Method untuk mengembalikan user dengan user_name sesuai parameter
    """
    for user in list_user:
        if user.get_name() == name:
            return user
    return None

def get_product(name):
    """
    Method untuk mengembalikan product dengan name sesuai parameter
    """
    for product in list_product:
        if product.get_name() == name:
            return product
    return None

# fungsi untuk menjalankan program utama
def main():
    main_flag = True

    # looping untuk pemilihan menu
    while main_flag:
        print("Selamat datang di Dekdepedia!")
        print("Silakan memilih salah satu menu di bawah:")
        print("1. Sign Up")
        print("2. Log In")
        print("3. Exit")
        print()
        pilih = input("Pilihan Anda: ")
        
        # input akun
        if (pilih == "1") : 
            banyak_user = int(input("Jumlah akun yang ingin didaftarkan : "))
            
            print("Data akun: ")
            for i in range (banyak_user) : 
                data_user_input = input(str(i+1)+". ")
                data_user = data_user_input.split()
                
                # cek validasi akun
                if data_user[0] == 'SELLER' and len(data_user) != 2:
                    print("Akun tidak valid.")

                elif not data_user[0] == 'BUYER' and not data_user[0] == 'SELLER':
                    print("Akun tidak valid.")

                elif data_user[0] == 'BUYER' and len(data_user) != 3:
                    print("Akun tidak valid.")


                elif data_user[0] == 'BUYER' and data_user[2].isnumeric() and int(data_user[2]) < 0:
                    print("Akun tidak valid.")
                
                elif len(data_user) < 2:
                    print("Akun tidak valid.")

                elif data_user[1] in list_nama_user:
                    print("Username sudah terdaftar.")

                elif data_user[1] not in list_user:
                    try:
                        if data_user[0] == 'BUYER':
                            if data_user[2].isnumeric():
                                list_nama_user.append(data_user[1])
                                
                                list_user.append(Buyer(user_name = data_user[1], saldo = int(data_user[2])))
                            else: 
                                print("Akun tidak valid.")

                        elif data_user[0] == "SELLER":
                            list_nama_user.append(data_user[1])
                            list_user.append(Seller(user_name = data_user[1]))
                    except IndexError:
                        pass

                elif not data_user[1].isalnum():
                    print("Akun tidak valid.")

            print()

        # login
        elif (pilih == "2") : 
            user_name_login = input("user_name : ")
            user_logged_in = get_user(user_name_login, list_user)

            if user_logged_in == None:
                print(f"Akun dengan user_name {user_name_login} tidak ditemukan\n")
                continue
            
            print(f"Anda telah masuk dalam akun {user_name_login} sebagai {user_logged_in.get_tipe()}\n")
            user_logged_in.menu()

        # akhiri program
        elif (pilih == "3") : 
            print("Terima kasih telah menggunakan Dekdepedia!")
            exit()

# menjalankan program
if __name__ == "__main__":
    main()
