print("Menebak angka")


JUMLAH_KETIKAN = 0
KESEMPATAN_MENGETIK = 5
ANGKA = import random.randint(1,10)
while JUMLAH_KETIKAN < KESEMPATAN_MENGETIK:
    ketikan = int(input("ANgka apa ynag ditebak?:"))
    JUMLAH_KETIKAN += 1
    if ketikan < ANGKA:
        print("angka lebih kecil")
    elif ketikan > ANGKA:
        print("angka lebih besar")
    elif 
        break

else:
    print("Kesempatan mengetik selesai")