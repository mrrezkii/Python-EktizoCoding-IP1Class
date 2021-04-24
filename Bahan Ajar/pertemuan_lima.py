# Case Study 1

for a in range(1, 11):
    print(2, "x", a, "=", 2 * a)

for b in range(1, 11):
    for c in range(1, 11):
        print(b, "x", c, "=", b * c)

'''
b = 1 {1,2,3 ... 10}
b = 2 {1,2,3 ... 10}}
b = 3 {1,2,3 ... 10}
.
.
b = 10 {1,2,3 ... 10}


'''

print()

# Case Study 2

tinggi = 5
for i in range(0, tinggi):
    for j in range(0, i+1):
        print("*", end=" ")
    print()

'''
i = 0 {0}
i = 1 {0, 1}
i = 2 {0, 1, 2}
i = 3 {0, 1, 2, 3}
i = 4 {0, 1, 2, 3, 4}


*
* *
* * *
* * * *
* * * * *
'''

print()

# Case Study 3

tinggi = 5
for i in range(1, tinggi + 1):
    for j in range(0, i):
        print(i, end=" ")
    print()

'''
i = 1 {0}
i = 2 {0, 1}
i = 3 {0, 1, 2}
i = 4 {0, 1, 2, 3}
i = 5 {0, 1, 2, 3, 4}


1
2 2 
3 3 3
4 4 4 4
5 5 5 5
'''

print()

# Case Study 4

tinggi = 5
for i in range(1, tinggi + 1):
    for j in range(1, i):
        print(j, end=" ")
    print()

print()

'''
~i = 1 {}~
i = 2 {1}
i = 3 {1, 2}
i = 4 {1, 2, 3}
i = 5 {1, 2, 3, 4}

1
1 2
1 2 3
1 2 3 4

'''

# Case Study 5

tinggi = 5
b = 0
for i in range(tinggi, 0, -1):
    b += 1
    for j in range(1, i+1):
        print(b, end=" ")
    print()

'''
i = 5 {1, 2, 3, 4, 5}  // b = 1
i = 4 {1, 2, 3, 4} // b = 2
i = 3 {1, 2, 3} // b = 3
i = 2 {1, 2} // b = 4
i = 1 {1} // b = 5


1 1 1 1 1
2 2 2 2
3 3 3
4 4
5

'''

print()
# Case Study 6 (Challenge)

tinggi = 5
for i in range(tinggi, 0, -1):
    for j in range(1, i+1):
        print(i, end=" ")
    print()

'''
i = 5 {1, 2, 3, 4, 5}
i = 4 {1, 2, 3, 4}
i = 3 {1, 2, 3}
i = 2 {1, 2}
i = 1 {1}

'''

print()

# Case Study 7 (Challenge)

tinggi = 5
for i in range(tinggi, 0, -1):
    for j in range(0, i):
        print(tinggi, end=" ")
    print()


'''
i = 5 {0, 1, 2, 3, 4}
i = 4 {0, 1, 2, 3}
i = 3 {0, 1, 2}
i = 2 {0, 1}
i = 1 {0}

5 5 5 5 5
5 5 5 5
5 5 5
5 5
5

'''

print()
