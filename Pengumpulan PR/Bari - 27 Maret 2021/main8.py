def penjumlahan(angka):
    if angka == 11:
        return 0
    else:
        return angka + penjumlahan(angka + 1)

print(penjumlahan(1))