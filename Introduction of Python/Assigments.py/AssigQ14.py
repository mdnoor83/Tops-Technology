"""14)Write a python program to sum of the first n positive integers."""

# Input a positive integer from the user
n = int(input("Enter a positive integer: "))

# Calculate the sum of the first n positive integers
sum_of_integers = n * (n + 1) // 2

print(f"The sum of the first {n} positive integers is: {sum_of_integers}")
