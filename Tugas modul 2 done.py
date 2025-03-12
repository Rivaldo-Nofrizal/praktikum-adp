#Daftar film dan harga tiket
print("Film yang sedang tayang")
print("|===========================================================|")
print("|    Kode Film   |       Judul Film      |   harga Tiket    |")
print("|===========================================================|")
print("|        1       |   Petaka Gunung Gede  |     Rp.65000     |")
print("|        2       |       Modal Nekat     |     Rp.60000     |")
print("|        3       |   1 Kakak 7 Ponakan   |     Rp.55000     |")
print("|        4       |        Agak Laen      |     Rp.60000     |")
print("|        5       |          Vina         |     Rp.65000     |")
print("|===========================================================|")
#memilih film  dan jumlah tiket yang dibeli
kode_film = int(input("Pilih Kode Film : "))
if kode_film == 1:
    harga_tiket =65000
elif kode_film == 2 :
    harga_tiket =60000
elif kode_film == 3 :
    harga_tiket =55000
elif kode_film == 4 :
    harga_tiket = 60000
elif kode_film == 5 :
    harga_tiket = 65000
else:
    print("Film Tidak Ditemukan")
jumlah_tiket = int(input("Masukkan Jumlah Tiket : "))
satuan = harga_tiket
jumlah_harga = jumlah_tiket*harga_tiket
if 100000<=jumlah_harga<250000 :
    potongan=jumlah_harga*0.15
elif jumlah_harga>=250000 :
    potongan=jumlah_harga*0.35
else :
    potongan=jumlah_harga*0
total=jumlah_harga-potongan
nama= str(input("Masukkan Nama Anda : "))
#Menampilkan Struk Pembelian
print("-------STRUK PEMESANAN-------")
print(f"Nama            : {nama}")
if kode_film == 1:
    print("Judul Film      : Petaka Gunung Gede")
elif kode_film == 2 :
    print("Judul Film      : Modal Nekat")
elif kode_film == 3 :
    print("Judul Film      : 1 Kakak 7 Ponakan")
elif kode_film == 4 :
    print("Judul Film      : Agak Laen")
elif kode_film == 5 :
    print("Judul Film      : Vina")
else:
    print("Film Tidak Ditemukan")
print(f"Jumlah Tiket    : {jumlah_tiket}")
print(f"Harga Satuan    : {satuan}")
print(f"Potongan Harga  : {potongan}")
print(f"Total Harga     : {total}")
print("---------TERIMAKASIH---------")