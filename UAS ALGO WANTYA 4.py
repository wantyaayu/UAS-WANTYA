def hitung_bmi(berat_badan, tinggi_badan):
    """
    Fungsi ini menghitung Indeks Massa Tubuh (BMI) berdasarkan berat dan tinggi badan.
    Formula BMI: BMI = berat_badan / (tinggi_badan ** 2)
    """
    bmi = berat_badan / (tinggi_badan ** 2)
    return bmi
def kategori_bmi(bmi):
    """
    Fungsi ini memberikan kategori BMI berdasarkan nilai BMI.
    """
    if bmi < 20:
        return "Kurus"
    elif 20 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Gemuk"
    else:
        return "Obesitas"
def main():
    """
    Fungsi utama yang mengatur eksekusi program.
    """
    print("Program Kalkulator BMI\n")

    # Meminta pengguna untuk memasukkan berat dan tinggi badan
    berat = float(input("Masukkan berat badan (kg): "))
    tinggi = float(input("Masukkan tinggi badan (m): "))

    # Memanggil fungsi untuk menghitung BMI
    bmi = hitung_bmi(berat, tinggi)

    # Menampilkan hasil BMI
    print(f"\nBMI Anda: {bmi:.2f}")

    # Menampilkan kategori BMI
    kategori = kategori_bmi(bmi)
    print(f"Kategori BMI: {kategori}")

if __name__ == "__main__":
    main()
