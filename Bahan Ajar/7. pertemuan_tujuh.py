#TOPIC OF FUNCTION

#Simple Message v1
'''
def welcome_message():
  print("Hi")
  print("What can we help you?")

welcome_message()
'''
#End of Simple Message v1

#Simple Message v2
'''
def welcome_message(name):
  print("Hi", name)
  print("What can we help you?")

name = "Andy"
welcome_message(name)
'''
#End of Simple Message v2

#Area of Rectangle and Volume of Blocks
'''
def multiplier(number1, number2):
    result = number1 * number2
    return result
panjang = 10
lebar = 5
luas = multiplier(panjang, lebar)
print(luas)

tinggi = 20
volume = multiplier(luas, tinggi)
print(volume)
'''
#End of Area of Rectangle and Volume of Blocks

#Area of Rectangle and Volume of Blocks Version 2
'''
def inputNumber ( prompt ):
    while(True):
        number = int(input("Input " + prompt + " : "))
        if (number < 0):
            print ('Invalid')
        else:
            break
    return number

def multiplier ( number1, number2 ):
    result = number1 * number2
    return result

panjang = inputNumber("Panjang") 
lebar = inputNumber("Lebar") 
tinggi = inputNumber("Tinggi") 

luas = multiplier (panjang, lebar)
volume = multiplier (luas, tinggi)

print("Luas", luas, "cm2")
print("Volume", volume, "cm3")
'''
#End of Area of Rectangle and Volume of Blocks Version 2

#Money Changer
'''
def inputAmount():
  amount = int(input("Amount: "))
  return amount

def convertCurrency(amount, rate):
  result = amount * rate
  return result

def printResult(currency, amount, result, currencyResult):
  print("For buying", currency, amount, "you have to pay", currencyResult, result)
   
amount = inputAmount()
rate = 15000
result = convertCurrency(amount, rate)
printResult ("USD", amount, result, "IDR")
'''
#End of Money Changer


def convertIDRtoUSD(amount, rate = 0.000070):
    result = amount * rate
    return result

def convertUSDtoIDR(amount, rate = 14375):
    result = amount * rate
    return result


idr = int(input("Masukkan jumlah uang dalam bentuk rupiah   :"))
print("Jika di konversi ke USD maka hasilnya", convertIDRtoUSD(idr))

usd = int(input("Masukkan jumlah uang dalam bentuk dollar   :"))
print("Jika di konversi ke USD maka hasilnya", convertUSDtoIDR(usd))