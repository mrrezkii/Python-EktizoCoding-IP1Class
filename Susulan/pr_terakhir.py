import random as rd

dadu_benar = rd.randint(1, 7)

tebak = 0
kesempatan = 3

while tebak < kesempatan:
    angka = int(input("Tebak angka dadu yang benar \t: "))
    tebak += 1
    if (angka < dadu_benar):
        print("Angka yang Anda tebak lebih kecil")
    elif (angka > dadu_benar):
        print("Angka yang Anda tebak lebih besar")
    else:
        print("Tebakan Anda benar")
        break
else:
    print("Coba lagi")