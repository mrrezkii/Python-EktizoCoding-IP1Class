# bilangan = 1...n
# hitung rata bilangan
bilangan = int(input("masukan bilangan :"))

total = 0
for s in range(1, bilangan+1):

    total = total+s
rata = total/s

print("rata rata bilangan diatas adalah:", rata)
