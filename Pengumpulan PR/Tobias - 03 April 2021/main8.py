def fa(n):
    if n==1:
        return 1 
    else:
        return n+fa (n-1)
        
n = int(input("masukan angka = "))
s=1
f=1 

print(n, "=", fa(n))