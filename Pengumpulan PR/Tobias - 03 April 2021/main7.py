def convertUSDtoIDR(amount, rate = 14.306):
    result = amount * rate
    return result
    
    
masukkanUang = int(input("masukan uang yang akan mdi konversi ke bentuk rupiah  :"))
print("hasil dari konversi adalah", convertUSDtoIDR(masukkanUang))