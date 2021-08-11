pas = "admin123"
l = 0
nama = "admin" 

user = input("masukan id anda:")
while user == nama:
    password = input("masukan password anda:")
    if password > pas:
        print("password salah")
    elif password < pas:
        print("password salah")
    else:
        ("login berhasil")
        l += 1 
        a = 0
        jumlah_sekolah = int(input("masukan jumlah sekolah ="))
        banyak_anak = int(input("masukan jumlah siswa dalam sekolah ="))
        while banyak_anak <= 0:
            a += jumlah_sekolah
            print("maaf kamu salah memasukan angka mohon diperiksa kembali")
           
        else:
            siswajakarta = [banyak_anak]
            print(siswajakarta)
            
        total = banyak_anak
        print("jumlah anak yang bersekolah di jakarta sebanyak",total)
        rata = banyak_anak/jumlah_sekolah
        print("rata rata anak yang bersekolah di jakarta sebanyak",rata)


else:
    print("dimohon mendaftar telebih dahulu")