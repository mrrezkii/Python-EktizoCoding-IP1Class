PIN = 1679
JUMLAH_KETIKAN_PIN = 0
KESEMPATAN_MENGETIK = 3

while JUMLAH_KETIKAN_PIN < KESEMPATAN_MENGETIK:
    ketikan = int(input("Enter PIN:"))
    JUMLAH_KETIKAN_PIN += 1
    if ketikan != PIN:
        print("Fail")
    elif ketikan == PIN:
        print("Success")
        break

else:
    print("Kesempatan mengetik selesai")
