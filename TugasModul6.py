konversi_nilai = [["A" , 4.00],
                  ["A-" , 3.75],
                  ["B+" , 3.50],
                  ["B" , 3.00],
                  ["B-" , 2.75],
                  ["C+" , 2.50],
                  ["C" , 2.00],
                  ["D" , 1.00],
                  ["E" , 0.00]
                  ]

jumlah_mhs = int(input("Masukkan jumlah mahasiswa : "))
jumlah_mk = int(input("Masukkan jumlah mata kuliah : "))
data_mhs = []

for i in range(jumlah_mhs):
    nama = input(f"\nMasukkan nama mahasiswa ke-{i+1}: ")
    nilai_mk = []
    for j in range(jumlah_mk) :
        while True :
            nilai = input(f"Masukkan nilai huruf MK-{j+1} (A, A-, B+, B, B-, C+, C, D, E): ").upper()
            ditemukan = False
            for item in konversi_nilai :
                if item[0] == nilai:
                    nilai_mk.append(nilai)
                    ditemukan = True
                    break
            if ditemukan:
                break
            print("Nilai tidak valid, coba lagi.")
    data_mhs.append([nama, nilai_mk])

hasil_ip = []
for mhs in data_mhs:
    nama = mhs[0]
    nilai_huruf = mhs[1]
    total_ip = 0
    for nh in nilai_huruf:
        for item in konversi_nilai:
            if item[0] == nh:
                total_ip += item[1]
                break
    ip = total_ip / jumlah_mk
    hasil_ip.append([nama, ip])

n = len(hasil_ip)
for i in range(n):
    for j in range(0, n-i-1):
        if hasil_ip[j][1]<hasil_ip[j+1][1]:
            temp = hasil_ip[j]
            hasil_ip[j] = hasil_ip[j+1]
            hasil_ip[j+1] = temp

print("\nHasil indeks presentasi mahasiswa : ")
print(f"{'No':<10}{'Nama':<10}{'IP':<5}")
print("-"*25)
for i in range(len(hasil_ip)):
    no = i+1
    nama = hasil_ip[i][0]
    ip = hasil_ip[i][1]
    print(f"{no:<10}{nama:<10}{ip:.2f}")