
# Import modul datetime untuk mengambil waktu dan tanggal saat ini
from datetime import datetime

# Mendapatkan tanggal dan waktu saat ini
tanggal_dan_waktu_hari_ini = datetime.now()
format_tanggal = tanggal_dan_waktu_hari_ini.strftime("%Y-%m-%d %H:%M:%S")
print("Tanggal        :", format_tanggal)

print('==========MOU-MOU FOOD==========')

# Input informasi pembeli
Nama_Pembeli = input('Nama_Pembeli  :  ')
Alamat = ('MOU-MOU FOOD CABANG BEKASI')
No_Telepon = ('0812345678910')

# Fungsi untuk menampilkan daftar menu
def daftar_menu():
    print(" No | Nama Menu   | Harga")
    print("-------------------------------")
    print(" 1  | WANTON      | 15000")
    print(" 2  | KWETIAW     | 12000")
    print(" 3  | DIMSUM      | 12000")
    print(" 4  | BAPAO       | 10000")
    print(" 5  | SIOMAY      | 15000")
    print("-------------------------------")
    kode = int(input("Masukkan nomor menu  : "))
    # Menghitung total harga pesanan berdasarkan pilihan menu
    if kode == 1:
        jumlah1 = int(input("Masukkan jumlah Pesanan : "))
        total1 = 15000 * jumlah1
        total.append(total1)
        tanya()
    elif kode == 2:
        jumlah2 = int(input("Masukkan jumlah pesanan : "))
        total2 = 12000 * jumlah2
        total.append(total2)
        tanya()
    elif kode == 3:
        jumlah3 = int(input("Masukkan jumlah pesanan : "))
        total3 = 12000 * jumlah3 
        total.append(total3)
        tanya()
    elif kode == 4:
        jumlah4 = int(input("Masukkan jumlah pesanan : "))
        total4 = 10000 * jumlah4
        total.append(total4)
        tanya()
    elif kode == 5:
        jumlah5 = int(input("Masukkan jumlah pesanan : "))
        total5 = 15000 * jumlah5   
        total.append(total5)
        tanya()
    return

# Fungsi untuk menanyakan apakah ingin menambah pesanan atau tidak
def tanya():
    print("\n-------------------------------")
    tanya = input("Ingin tambah pesanan? [y = Ya/t = Tidak] : ")
    print("-------------------------------")
    if tanya == "y":
        daftar_menu()
    elif tanya == "t":
        akhir()
    else:
        print("Anda salah memasukkan perintah, tolong isi kembali")

# Fungsi untuk menampilkan struk belanja
def akhir():
    for harga in total:
        print("SubTotal         : ", sum(total))
        diskon = 0
        a = sum(total)
        # Menghitung diskon berdasarkan total pembelian
        if a > 200000:
            diskon = a * 1/100
        elif a > 100000:
            diskon = a * 5/100
        else:
            diskon = 0
        print("Potongan Harga   : ", diskon)
        totalakhir = a - diskon
        print("Total            : ", totalakhir)
        print("-------------------------------")
        jumlah_uang_yang_dibayar = int(input("Jumlah uang yang dibayar   :  "))
        kembalian = jumlah_uang_yang_dibayar - totalakhir
        print("Kembalian        : ", kembalian)

        # Menampilkan struk belanja
        print("\n==================================")
        print("========== S T R U K   B E L I =========")
        print("==================================")
        print("Nama\t\t :", Nama_Pembeli)
        print('Alamat           :'  ,Alamat)
        print('No_Telepon       :'  ,No_Telepon)
        print("Tanggal          :", format_tanggal)
        print("Kembalian        : Rp", kembalian)
        print("Potongan Harga   : ", diskon)
        totalakhir = a - diskon
        print("Total            : ", totalakhir)
        print("-------------------------------")
        print("Kembalian        : ", kembalian) 
        print("==================================")
        print("==================================")
        print("-------------------------------")
        print("          Terima Kasih         ")

# Memanggil fungsi untuk menampilkan daftar menu
daftar_menu()