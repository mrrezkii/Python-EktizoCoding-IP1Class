pin = 1111
percobaan = 0
kesempatan_mencoba = 3

while percobaan < kesempatan_mencoba:
    coba = int(input("masukan pin anda:"))
    percobaan += 1
    if coba < pin:
        print("WRONG PIN PLEASE TRY AGAIN")
    elif coba > pin:
        print("WRONG PIN PLEASE TRY AGAIN")
    else:
        print("SUCCESS")

        break
else:
    print("FAIL")
