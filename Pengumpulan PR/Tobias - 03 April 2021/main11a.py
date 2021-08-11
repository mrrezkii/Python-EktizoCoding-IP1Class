
import code 
jumlah = 0
kesempatan = 5



while jumlah < kesempatan:
    kode = int(input("masukan kode:"))
    jumlah += 1
    if kode < code.code:
        print ("ACCESS DENIED")
    elif kode > code.code:
         print ("ACCESS DENIED")
    else:
        print ("ACCESS SUCCESS")

else:
    print ("PLEASE TRY AGAIN LATER")

