banyak = int(input("Masukkan banyak bilangan : "))

total = 0
for i in range(1, banyak + 1):
    bil= int(input("Masukkan bilangan yang akan di rata - rata: "))
    total+=bil
    
rata_rata = total / banyak
print("Rata - rata Anda adalah:" , rata_rata)
