while True :
    password = input("Masukkan password : ")

    count = 0
    for _ in password :
        count += 1

    ada_huruf_kecil = False
    ada_huruf_besar = False
    ada_angka = False
    ada_karakter_khusus = False
    karakter_khusus = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
    angka = "0123456789"
    huruf_kecil = "abcdefghijklmnopqrstuvwxyz"
    huruf_besar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for char in password:                
        for h in huruf_kecil:
            if char == h:
                ada_huruf_kecil = True
                break
        for H in huruf_besar:
            if char == H:
                ada_huruf_besar = True
                break
        for n in angka:
            if char == n:
                ada_angka = True
                break    
        for special in karakter_khusus:
            if char == special:
                ada_karakter_khusus = True
                break

    if count >= 8:
        if ada_huruf_kecil:
            if ada_huruf_besar:
                if ada_angka:
                    if ada_karakter_khusus:
                        print("Password Valid!")
                        print("Selamat, password anda dapat digunakan!")
                        break
                    else:
                        print("Password harus memiliki minimal 1 karakter khusus")
                else:
                    print("Password harus memiliki minimal 1 angka")
            else:
                print("Password harus memiliki minimal 1 huruf besar")
        else:
            print("Password harus memiliki minimal 1 huruf kecil")
    else:
        print("Password harus memiliki minimal 8 karakter")
