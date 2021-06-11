
gates = [20, 10, 30, 60, 40]
n = len(gates)
print("Jumlah kendaraan di tol Jakarta")
for i in range(n):
    print("Gates" , i+1, "=" , gates[i])
    
total = gates[0]
highest = gates[0]
lowest = gates[0]
no_high = 1
no_low = 1

for i in range(n):
    if(gates[i] > highest):
        highest = gates[i]
        no_high = i + 1
    if(gates[i] < lowest):
        lowest = gates[i]
        no_low = i + 1
        
    total = total + gates[i]
    
    
average = total / n

print("Gates paling ramai                : gate" , no_high, "dengan jumlah kendaraan" , highest)
print("Gates paling sepi                 : gate" , no_low, "dengan jumlah kendaraan" , lowest)
print("Total dari keseluruhan gate       : " , total)
print("Rata - rata dari keseluruhan gate : " , average)