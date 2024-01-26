from datetime import datetime

def hitung_usia(tanggal_lahir):
    """
    Fungsi ini menghitung usia berdasarkan tanggal lahir.
    """
    today = datetime.today()
    tanggal_lahir = datetime.strptime(tanggal_lahir, "%Y-%m-%d")
    usia = today.year - tanggal_lahir.year - ((today.month, today.day) < (tanggal_lahir.month, tanggal_lahir.day))
    return usia

def cek_lansia(tanggal_lahir):
    """
    Fungsi ini menentukan apakah seseorang masuk kategori lansia berdasarkan usia.
    Lansia jika usia >= 60 tahun.
    """
    usia = hitung_usia(tanggal_lahir)
    return usia >= 60

def main():
    """
    Fungsi utama yang mengatur eksekusi program.
    """
    print("Program Penentu Usia Lansia\n")

    # Meminta pengguna untuk memasukkan tanggal lahir
    tanggal_lahir_str = input("Masukkan tanggal lahir (YYYY-MM-DD): ")

    try:
        # Memanggil fungsi untuk menentukan apakah lansia
        lansia = cek_lansia(tanggal_lahir_str)

        # Menampilkan hasil
        if lansia:
            print("Anda masuk kategori lansia.")
        else:
            print("Anda belum masuk kategori lansia.")
    except ValueError:
        print("Format tanggal lahir tidak valid. Gunakan format YYYY-MM-DD.")

if __name__ == "__main__":
    main()