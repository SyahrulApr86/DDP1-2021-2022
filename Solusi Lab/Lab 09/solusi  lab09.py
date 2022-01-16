class User:
    def __init__(self, username, tipe):
        self.__username = username
        self.__tipe = tipe
    
    def getUsername(self):
        return self.__username
    
    def getTipe(self):
        return self.__tipe


class Buyer(User):
    def __init__(self, username, saldo):
        super().__init__(username, "BUYER")
        self.__saldo = int(saldo)
        self.__daftar_beli = []
    
    def getSaldo(self):
        return self.__saldo
    
    def minSaldo(self, min):
        self.__saldo -= min
    
    def addDaftarBeli(self, produk):
        self.__daftar_beli.append(produk)
    
    def printDaftarBeli(self):
        self.__daftar_beli.sort(key= lambda obj: obj.getNama())
        print("\nBerikut merupakan barang yang saya beli")
        print("-------------------------------------")
        print(" Nama Produk   |   Harga   | Penjual")
        print("-------------------------------------")
        for barang in self.__daftar_beli:
            print(f"{barang.getNama():<14} | {barang.getHarga():<9} | {barang.getSeller().getUsername()}")
        print("-------------------------------------")
    


class Seller(User):
    def __init__(self, username):
        super().__init__(username, "SELLER")
        self.__pemasukan = 0
        self.__daftar_jual = []
    
    def getPemasukan(self):
        return self.__pemasukan
    
    def addPemasukan(self, add):
        self.__pemasukan += add
    
    def getDaftarJual(self):
        return self.__daftar_jual

    def printDaftarJual(self):
        self.__daftar_jual.sort(key= lambda obj: obj.getNama())
        print("\nBerikut merupakan barang jualan saya")
        print("-------------------------------------")
        print(" Nama Produk   |   Harga   |  Stock ")
        print("-------------------------------------")
        for barang in self.__daftar_jual:
            print(f"{barang.getNama():<14} | {barang.getHarga():<9} | {barang.getStok()}")
        print("-------------------------------------")
        
    
    def addDaftarJual(self, produk):
        self.__daftar_jual.append(produk)


class Product:
    def __init__(self, nama, harga, stok, seller):
        self.__nama = nama
        self.__harga = harga
        self.__stok = stok
        self.__seller = seller
    
    def getNama(self):
        return self.__nama
    
    def getHarga(self):
        return self.__harga
    
    def getStok(self):
        return self.__stok
    
    def minStok(self):
        self.__stok -= 1

    def getSeller(self):
        return self.__seller

    def __lt__(self, other): # less than, self < other ekuivalem dengan self.__lt__(other)
        return self.__nama < other.getNama()

    def __eq__(self, other): # self == other -> ekuivalen dengan self.__eq__(other)
        return self.__nama == other.getNama()


def sign_up():
    jumlah_user = int(input("Jumlah akun yang ingin didaftarkan: "))

    print("Data akun:")
    counter = 1
    for counter in range(1, jumlah_user+1):
        data = input(f"{counter}. ").split()
        if (len(data) < 2 or len(data) > 3):
            print("Akun tidak valid.")

        else:
            if (data[0] == "BUYER" and len(data) == 3):
                username = data[1]
                saldo = data[2]

                if (not saldo.isdigit):
                    print("Akun tidak valid.")
                else:
                    if (username in daftar_user):
                        print("Username sudah terdaftar.")
                    else:
                        daftar_user[username] = Buyer(username, saldo)
                        counter += 1

            elif (data[0] == "SELLER" and len(data) == 2):
                username = data[1]

                if (username in daftar_user):
                    print("Username sudah terdaftar.")
                else:
                    daftar_user[username] = Seller(username)

            else:
                print("Akun tidak valid")

def log_in():
    username = input("user_name: ")
    if (username not in daftar_user):
        print(f"Akun dengan user_name {username} tidak ditemukan")
        return None
    
    else:
        print(f"Anda telah masuk dalam akun {username} sebagai {daftar_user[username].getTipe()}")
        return daftar_user[username]


def printDaftarProduk(daftar_product):
    print("\nBerikut merupakan daftar produk di Dekdepedia")
    print("-----------------------------------------------")
    print(" Nama Produk   |   Harga   | Stock |  Penjual")
    print("-----------------------------------------------")
    for nama, barang in sorted(daftar_product.items()):
        print(f"{nama:<14} | {barang.getHarga():<9} | {barang.getStok():<5} | {barang.getSeller().getUsername()}")
    print("-----------------------------------------------")
    

daftar_user = {} # keynya adalah nama user (string), valuenya object user
daftar_product = {} # keynya nama produk (string), valuenya object produk

welcome_msg = """Selamat datang di Dekdepedia!
Silakan memilih salah satu menu di bawah:
1. Sign Up\n2. Log In\n3. Exit"""

menu = "-1"
while menu != "3":
    print("\n" + welcome_msg)
    menu = input("Pilihan Anda: ")
    
    if menu == "1":
        sign_up()

    elif menu == "2":
        user = log_in()
        if user is not None:
            # seller
            if user.getTipe() == "SELLER":
                print(f"\nSelamat datang {user.getUsername()},")
                print("berikut menu yang bisa Anda lakukan:")
                print("1. TAMBAHKAN_PRODUK\n2. LIHAT_DAFTAR_PRODUK_SAYA\n3. LOG_OUT")

                login_menu = "-1"
                while login_menu != "3":
                    print(f"\nPemasukan Anda {user.getPemasukan()}")
                    login_menu = input("Apa yang ingin Anda lakukan? ")

                    if login_menu == "1": # minta tambah produk
                        nama, harga, stok = input("Masukkan data produk: ").split()
                        if nama in user.getDaftarJual():
                            print("Produk sudah pernah terdaftar")
                        else:
                            produk = Product(nama, int(harga), int(stok), user)
                            user.addDaftarJual(produk)
                            daftar_product[nama] = produk
                    
                    elif login_menu == "2":
                        user.printDaftarJual()
                    
                    elif login_menu == "3":
                        print(f"Anda telah keluar dari akun {user.getUsername()}")
                    
                    else:
                        print("Perintah tidak valid")
            
            # buyer
            else:
                print(f"\nSelamat datang {user.getUsername()},")
                print("berikut menu yang bisa Anda lakukan:")
                print("1. LIHAT_SEMUA_PRODUK\n2. BELI_PRODUK\n3. RIWAYAT_PEMBELIAN_SAYA\n4. LOG_OUT")

                login_menu = "-1"
                while login_menu != "4":
                    print(f"\nSaldo Anda {user.getSaldo()},")
                    login_menu = input("Apa yang ingin Anda lakukan? ")

                    if login_menu == "1":
                        printDaftarProduk(daftar_product)
                    
                    elif login_menu == "2":
                        nama_barang = input("Masukkan barang yang ingin dibeli: ")
                        if nama_barang not in daftar_product:
                            print(f"Barang dengan nama {nama_barang} tidak ditemukan dalam Dekdepedia.")
                        
                        elif daftar_product[nama_barang].getStok() < 1:
                            print("Maaf, stok produk telah habis.")
                        
                        elif daftar_product[nama_barang].getHarga() > user.getSaldo():
                            print(f"Maaf, saldo Anda tidak cukup untuk membeli {nama_barang}")
                        
                        else:
                            seller = daftar_product[nama_barang].getSeller()
                            print(f"Berhasil membeli {nama_barang} dari {seller.getUsername()}")
                            seller.addPemasukan(daftar_product[nama_barang].getHarga())

                            user.minSaldo(daftar_product[nama_barang].getHarga())
                            user.addDaftarBeli(daftar_product[nama_barang])

                            daftar_product[nama_barang].minStok()

                    elif login_menu == "3":
                        user.printDaftarBeli()

                    elif login_menu == "4":
                        print(f"Anda telah keluar dari akun {user.getUsername()}")
                    
                    else:
                        print("Perintah tidak valid")
                    

    elif menu == "3":
        print("Terima kasih telah menggunakan Dekdepedia!")