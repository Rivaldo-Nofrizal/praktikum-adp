M = int(input("Masukkan Modal Awal: "))
r = float(input("Masukkan Suku Bunga Tahunan (%): "))
T = float(input("Masukkan Target Investasi: "))
tahun = 0
for tahun in range (1,M) :
    M += M*(r/100)
    print  (f"Tahun ke-{tahun} : Rp{M:}")
    if M>=T:
        break
print(f"Target tercapai dalam {tahun} tahun!")
