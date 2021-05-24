#TOPIC OF RECURSION

#Print Multi Text with Recursion

def print_multi_text(num):
  if num > 0:
    print("Hello")
    print_multi_text(num-1)

num = 3
print_multi_text(num)

# num = 3
# 3 - 1 = 2
# 2 - 1 = 1
# 1 - 1 = 0 (Stop)

#End of Print Multi Text with Recursion

#Factorial v1

def factorial(max):
  if(max == 1):
    return 1
  return max * factorial(max-1)

print(factorial(5))


# factorial(5) = 5 * factorial(4) = 120
# factorial(4) = 4 * factorial(3) = 24
# factorial(3) = 3 * factorial(2) = 6
# factorial(2) = 2 * factorial(1)  = 2
# factorial(1) = 1

#End of Factorial v1

#Factorial v2

def factorial(n):
    if n < 0:
        return "invalid"
    elif n > 1:
        return n * factorial(n-1)
    elif n == 0:
        return 1
    else:
        return n
    
print(factorial(0))

# factorial(0) = 1

#End of Factorial v2

#factorial v3

def factorial(n, total):
  if n > 0:
    total = total * n
    n = n - 1
    factorial(n, total)
  else:
    print(total)
n = 5
total = 1
factorial(n, total)

# factorial(5, 1) = total = 5, n = 4
# factorial(4, 5) = total = 20, n = 3
# factorial(3, 20) = total = 60, n = 2
# factorial(2, 60) = total = 120, n = 1

#end of factorial v3

#Fibonacci v1

def fibonacci(a,b,max):
  if(max > 0):
    sum = a + b
    a = b
    b = sum
    print(sum, end=" ")
    fibonacci(a,b,max-1)

max = 6
a = 0
b = 1
if max <= 0:
  print("invalid")
elif max == 1:
  print(a)
elif max == 2:
  print(a, b)
elif max > 2:
  print(a, b, end=" ")
  fibonacci(a,b,max-2)

# print(0, 1)
# fibonacci(0, 1, 4) = sum = 1, a = 1, b = 1, print(1)
# fibonacci(1, 1, 4) = sum = 2, a = 1, b = 2, print(2)
# fibonacci(1, 2, 4) = sum = 3, a = 2, b = 3, print(3)
# fibonacci(2, 3, 4) = sum = 5, a = 3, b = 5, print(5)

#End of Fibonacci v1

#fibonacci v2

def fibonacci(num_1,num_2,n):
  print(num_1)
  if n > 0:
    total = num_1 + num_2
    n = n - 1
    fibonacci(num_2, total, n)
  else:
    print(num_2)

a = 0
b = 1
n = 10
fibonacci(a,b,n)


# fibonacci(0, 1, 10) = total = 1, n = 9
# fibonacci(1, 1, 9) = total = 2, n = 8
# fibonacci(1, 2, 8) = total = 3, n = 7
# fibonacci(2, 3, 7) = total = 5, n = 6
# fibonacci(3, 5, 6) = total = 8, n = 5
# fibonacci(5, 8, 5) = total = 13, n = 4
# fibonacci(8, 13, 4) = total = 21, n = 3
# fibonacci(13, 21, 3) = total = 34, n = 3
# fibonacci(21, 34, 2) = total = 55, n = 2
# fibonacci(34, 55, 2) = total = 89, n = 1
# fibonacci(55, 89, 1) = 89

#end of fibonacci v2

#Sum Recursive 

def sum_recursive(current_number):
    # Base case
    # Return the final state
    if current_number == 11:
        return 0

    # Recursive case
    # Thread the state through the recursive call
    else:
        return current_number +  sum_recursive(current_number + 1)
        
print(sum_recursive(1))

#REFERENCE: https://realpython.com/python-thinking-recursively/
#End of Sum Recursive 

#Exponentiation
'''
=== Notes ===
Exponentiation is a mathematical operation, written as b^n, involving two numbers, the base b and the exponent or power 
'''
''' 
def exponentiation(base, exponent):
  if(exponent == 0):
    return 1
  return base * exponentiation(base, exponent-1)

base = 2
exponent = 5
print(exponentiation(base, exponent))
'''
#End of Exponentiation