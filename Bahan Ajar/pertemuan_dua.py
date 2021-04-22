# Nasabah bank

saldo = 200000
ambil = int(input("Masukkan jumlah uang yang ingin di ambil : "))
batas_minimum = 50000
sisa_saldo = saldo - ambil

if sisa_saldo < batas_minimum:
    print("Anda tidak dapat mengambil uang, saldo tidak cukup")
else:
    print("Uang berhasil di ambil")
    print("Sisa Saldo Anda", sisa_saldo)

# Cek umur

umur = int(input("Masukkan umur Anda : "))

if 0 < umur <= 5:
    print("Masa balita")
elif 5 < umur <= 12:
    print("Masa kanak - kanak")
elif 12 < umur <= 25:
    print("Masa remaja")
elif 25 < umur <= 45:
    print("Masa dewasa")
elif 45 < umur <= 65:
    print("Masa tua")
elif 65 < umur:
    print("Masa manula")

# Diskon barang

barang1 = 24000
barang2 = 24000
barang3 = 2000

totalharga = barang1 + barang2 + barang3

if totalharga >= 50000:
    diskon = 5/100 * totalharga
    harga_setelah_diskon = totalharga - diskon
    print("Anda cukup membayar", harga_setelah_diskon)
else:
    print("Anda harus membayar", totalharga)
