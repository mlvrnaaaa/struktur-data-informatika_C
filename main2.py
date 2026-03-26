import matplotlib.pyplot as plt

nilai = []
for i in range(10):
    n = int(input(f"Masukkan nilai ke-{i+1}: "))
    nilai.append(n)

# memproses data
nilai_tertinggi = max(nilai)
nilai_terendah = min(nilai)
rata_rata = sum(nilai) / len(nilai)

# menghitung kelulusan
lulus = 0
for n in nilai:
    if n >= 60:
        lulus += 1
tidak_lulus = len(nilai) - lulus

# output hasil
print("\n=== HASIL ===")
print("Data nilai:", nilai)
print("Nilai tertinggi:", nilai_tertinggi)
print("Nilai terendah:", nilai_terendah)
print("Rata-rata:", rata_rata)
print("Jumlah lulus:", lulus)
print("Jumlah tidak lulus:", tidak_lulus)

# grafik nilai tertinggi & terendah
plt.figure()
plt.bar(["Tertinggi", "Terendah"], [nilai_tertinggi, nilai_terendah])
plt.title("Perbandingan Nilai Tertinggi & Terendah")
plt.xlabel("Kategori")
plt.ylabel("Nilai")
plt.show()

# grafik kelulusan
plt.figure()
plt.bar(["Lulus", "Tidak Lulus"], [lulus, tidak_lulus])
plt.title("Data Kelulusan Mahasiswa")
plt.xlabel("Kategori")
plt.ylabel("Jumlah Mahasiswa")
plt.show()