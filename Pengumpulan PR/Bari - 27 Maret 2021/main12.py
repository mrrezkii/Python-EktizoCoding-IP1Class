jumlah_ulangan= 0
kesempatan= 10
while jumlah_ulangan < kesempatan:
    user = input("username:")
    pas = input("password:")
if user != "admin" and pas != "admin123":
    print("username atau password kamu salah")
elif user == "admin" and pas == "admin123":
    print("JUMLAH ANAK DI 3 SEKOLAH JAKARTA YANG TERSEBUT")
    sekolah_yang_disebut= int(input("Mau lihat data banyak anak di sekolah yang mana:"))
    if sekolah_yang_disebut < 1 or sekolah_yang_disebut > 3:
        print("ERROR")
    else:
        if sekolah_yang_disebut == 1:
            print("Jumlah anak ada 300")
    elif sekolah_yang_disebut == 2:
            print("Jumlah anak ada 500")
    elif sekolah_yang_disebut == 3:
            print("Jumlah anak ada 450")
   
    lis = [300, 500, 450]
    n = len

    total = lis
    total = total + lis[i]

    average = total / n

    print("Total anak - anak dari keseluruhan sekolah                   : " , total)
    print("Rata - rata dari keseluruhan anak - anak dari ketiga sekolah : " , average)

else:
    print("kesempatan selesai")