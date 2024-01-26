# Program untuk menentukan kategori gaji dan bonus karyawan

# Input gaji pokok karyawan
gaji_pokok = float(input("Masukkan gaji pokok karyawan: "))

# Kondisi untuk menentukan kategori gaji
if gaji_pokok < 0:
    print("Gaji tidak valid. Harap masukkan nilai yang benar.")
else:
    # Total bonus berdasarkan gaji pokok
    if gaji_pokok <= 1000000:
        bonus = gaji_pokok * 0.1
    elif 1000000 < gaji_pokok <= 2000000:
        bonus = gaji_pokok * 0.15
    else:
        bonus = gaji_pokok * 0.2

    # Total gaji setelah penambahan bonus
    total_gaji = gaji_pokok + bonus

    # Menentukan kategori gaji berdasarkan total gaji
    if total_gaji < 1000000:
        kategori_gaji = "Rendah"
    elif 1000000 <= total_gaji < 2000000:
        kategori_gaji = "Sedang"
    else:
        kategori_gaji = "Tinggi"

    # Menampilkan hasil
    print(f"\nGaji Pokok: Rp {gaji_pokok}")
    print(f"Bonus: Rp {bonus}")
    print(f"Total Gaji: Rp {total_gaji}")
    print(f"Kategori Gaji: {kategori_gaji}")
