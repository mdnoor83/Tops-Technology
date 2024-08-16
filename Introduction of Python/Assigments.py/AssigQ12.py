"""12) Write a Python program to sum of three given integers. However, if
two values are equal sum will be zero."""

# Input three integers from the user
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
c = int(input("Enter the third integer: "))

# Initialize the sum
sum = 0

# Check if any two values are equal
if a != b and b != c and a != c:
    sum = a + b + c

print(f"The sum of the three integers is: {sum}")

