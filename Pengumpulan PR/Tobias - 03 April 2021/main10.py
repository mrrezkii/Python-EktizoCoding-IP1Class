
translate = {
    "bread": "roti",
    "class": "kelas",
    "food": "makanan",
    "student": "pelajar",
    "book": "buku",
}
print (translate)

for key, value in translate.items():
    print (key,"=",value) 
    
del translate["book"]
print(translate)

translate["food"] = "makanann"
print(translate)

translate.update({"water" : "air"})
print(translate)

translate.clear()
print(translate)