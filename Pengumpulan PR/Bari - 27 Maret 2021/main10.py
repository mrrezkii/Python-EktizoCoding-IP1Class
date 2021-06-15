kamus = {
    "Bed" : "Tempat Tidur",
    "Closet" : "Lemari",
    "Chair" : "Kursi"
    
}
print(kamus["Bed"])
kamus["Bed"] = "Tidur"
print()
print(kamus["Bed"])
print()
for key in kamus:
    print(key)
print()
for value in kamus.values():
    print(value)
print()
for key, value in kamus.items():
    print(key, '=' , value)
print()
kamus.pop("Closet")
print(kamus)