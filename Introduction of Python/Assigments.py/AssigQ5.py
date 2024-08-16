"""5)Write a Python program to get the Factorial number of given numbers.
"""
num = int(input("Enter your Number : "))
fact = 1
a = 1
while a <= num:
    fact = fact*a
    a = a+1

print("The factorial of ", num, "Is", fact)