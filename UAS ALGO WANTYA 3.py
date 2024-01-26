def pilih_baju(cuaca, acara, suka_warna_cerah):
    """
    Fungsi ini memberikan rekomendasi baju berdasarkan cuaca, acara, dan preferensi warna.
    """
    if cuaca.lower() == "panas":
        if acara.lower() == "formal":
            print("Sarankan memakai baju formal ringan, seperti kemeja dan celana pendek.")
        elif acara.lower() == "kasual":
            if suka_warna_cerah:
                print("Sarankan memakai kaos berwarna cerah dan celana pendek.")
            else:
                print("Sarankan memakai kaos dan celana pendek.")
    elif cuaca.lower() == "dingin":
        if acara.lower() == "formal":
            print("Sarankan memakai setelan jas atau blazer dengan celana panjang.")
        elif acara.lower() == "kasual":
            print("Sarankan memakai sweater atau jaket hangat dengan celana panjang.")
    else:
        print("Cuaca tidak dikenali. Mohon masukkan 'panas' atau 'dingin'.")

# Meminta pengguna untuk memasukkan informasi
cuaca_hari_ini = input("Bagaimana cuaca hari ini? (panas/dingin): ")
jenis_acara = input("Apa jenis acara yang akan Anda hadiri? (formal/kasual): ")
suka_warna_cerah = input("Apakah Anda suka warna cerah? (ya/tidak): ").lower() == 'ya'

# Memanggil fungsi untuk memberikan rekomendasi baju
pilih_baju(cuaca_hari_ini, jenis_acara, suka_warna_cerah)

