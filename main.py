import matplotlib.pyplot as plt

def input_nilai(jumlah):
    data = []
    print("=== Input Nilai Mahasiswa ===")
    for i in range(jumlah):
        while True:
            try:
                n = int(input(f"Masukkan nilai ke-{i+1}: "))
                if 0 <= n <= 100:
                    data.append(n)
                    break
                else:
                    print("Nilai harus 0 - 100!")
            except:
                print("Input harus angka!")
    return data


#  memproses data
def proses_nilai(data):
    tertinggi = data[0]
    terendah = data[0]
    total = 0
    lulus = 0

    for n in data:
        if n > tertinggi:
            tertinggi = n
        if n < terendah:
            terendah = n

        total += n

        if n >= 60:
            lulus += 1

    rata_rata = total / len(data)
    tidak_lulus = len(data) - lulus

    return tertinggi, terendah, rata_rata, lulus, tidak_lulus


# menampilkan hasil
def tampilkan_hasil(data, tertinggi, terendah, rata, lulus , tidak_lulus):
    print("\n=== Hasil ===")
    print("Data nilai       :", data)
    print("Nilai tertinggi  :", tertinggi)
    print("Nilai terendah   :", terendah)
    print("Rata-rata        :", rata)
    print("Jumlah lulus     :", lulus)
    print("Tidak lulus      :", tidak_lulus)


# grafik
def tampilkan_grafik(tertinggi, terendah, lulus, tidak_lulus):
    # grafik nilai
    plt.figure()
    plt.bar(["Tertinggi", "Terendah"], [tertinggi, terendah])
    plt.title("Perbandingan Nilai")
    plt.xlabel("Kategori")
    plt.ylabel("Nilai")
    plt.show()

    # grafik lulus
    plt.figure()
    plt.bar(["Lulus", "Tidak Lulus"], [lulus, tidak_lulus])
    plt.title("Data Kelulusan")
    plt.xlabel("Kategori")
    plt.ylabel("Jumlah Mahasiswa")
    plt.show()


# output
nilai = input_nilai(10)
tertinggi, terendah, rata, lulus, tidak_lulus = proses_nilai(nilai)

tampilkan_hasil(nilai, tertinggi, terendah, rata, lulus, tidak_lulus)
tampilkan_grafik(tertinggi, terendah, lulus, tidak_lulus)