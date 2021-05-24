print('''
    Jenis es krim 
    1. Solo = Rp10.000
    2. Couple = Rp15.000
    3. Group = Rp25.000
    
    Toping
    1. No Topping = Rp0 
    2. Chocolate = Rp3.000
    3. Almond = Rp5.000
    4. Jelly = Rp6.000
''')

total = 0

jenis_es_krim = int(input("Kamu ingin jenis es krim apa ?     :"))
while jenis_es_krim < 1 or jenis_es_krim > 3:
    print("Kamu memasukkan pilihan yang salah")
    jenis_es_krim = int(input("Kamu ingin jenis es krim apa ?     :"))
else:
    if jenis_es_krim == 1:
        total += 10000
    elif jenis_es_krim == 2:
        total += 15000
    elif jenis_es_krim == 3:
        total += 25000

jenis_toping = int(input("Kamu ingin toping apa ?     :"))
while jenis_toping < 1 or jenis_toping > 4:
    print("Kamu memasukkan pilihan yang salah")
    jenis_toping = int(input("Kamu ingin toping apa ?     :"))
else:
    if jenis_toping == 1:
        total += 0
    elif jenis_toping == 2:
        total += 3000
    elif jenis_toping == 3:
        total += 5000
    elif jenis_toping == 4:
        total += 6000
        
print("Total yang harus kamu bayar adalah", total)