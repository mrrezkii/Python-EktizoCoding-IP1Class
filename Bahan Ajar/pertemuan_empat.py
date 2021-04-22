# Case Study 1

jawaban = input("Apakah kamu ingin memasukkan nama ? (Ya/Tidak)   ")

jumlah = 0

while jawaban == 'Ya' or jawaban == 'ya':
    jumlah += 1
    nama = input("Masukkan nama :")
    jawaban = input("Ulangi ? (Ya/Tidak)   ")

print("Kamu telah memasukkan sebanyak", jumlah, "nama yeeah")


# Case Study 2

angka_tebakan = 5
jumlah_tebakan = 0
kesempatan_menebak = 3

while jumlah_tebakan < kesempatan_menebak:
    tebakan = int(input("Coba tebak angka 1-10 : "))
    jumlah_tebakan += 1
    if tebakan < angka_tebakan:
        print("Angka yang Anda tebak lebih kecil dari angka yang benar")
    elif tebakan > angka_tebakan:
        print("Angka yang Anda tebak lebih besar dari angka yang benar")
    else:
        print("Selamat kamu menebak angka yang benar, kamu berhasil menebak dengan benar sebanyak",
              angka_tebakan, "kali")
        break
else:
    print("Kamu gagal menebak bro, jawaban yang benar adalah", angka_tebakan)
