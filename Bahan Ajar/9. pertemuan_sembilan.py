#Exercise 1 - Show List

scores = [90, 80, 85, 70, 75]
for i in range(0, 5):
  print("Skor Siswa No.", i + 1, "=", scores[i])

#End of Exercise 1

#Exercise 2 - Add List and Show List

scores = []
for i in range(0, 5):
  new_score = int(input("Masukkan skor ke : "))
  scores.append(new_score)
for i in range(0, 5):
  print("Skor Siswa No.", i + 1, "=", scores[i])
  

#End of Exercise 2 - Add List and Show List

#Exercise 3 - Get total and Average with validation

total = 0
avg = 0
scores = []
for i in range(0, 5):
  new_score = int(input("Masukkan skor ke : "))
  while new_score < 0 or new_score > 100:
    print("Skor tidak valid, skor harus diantara 0 - 100")
    new_score = int(input("Masukkan skor ke : "))
  scores.append(new_score)
  total = total + scores[i]

for i in range(0, 5):
  print("Skor Siswa No.", i + 1, "=", scores[i])
print("Total skor = ", total)
avg = total / 5
print("Rata-rata skor =", avg)
