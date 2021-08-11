listSchools = []
total = 0

print("DATA NUMBER OF STUDENTS IN JAKARTA\n==================================\n")

jumlah_sekolah = int(input("Number of Schools \t: "))

print("INPUT NUMBER OF STUDENTS\n------------------------\n")

for i in range(jumlah_sekolah):
    number = int(input("Number of students in school-" +str(i+1) +" :"))
    while number < 1 :
        print("Invalid")
        number = int(input("Number of students in school-" +str(i+1) +" :"))
    listSchools.append(number)
    total += listSchools[i]

print("total : ", total)
print("average : ", round((total / jumlah_sekolah), 2))