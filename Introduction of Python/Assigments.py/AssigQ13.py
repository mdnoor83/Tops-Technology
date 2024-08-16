"""13) Write a Python program that will return true if the two given
integer values are equal or their sum or difference is 5"""

# Input two integers from the user
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

# Check the conditions
result = (a == b) or (a + b == 5) or (abs(a - b) == 5)

print(f"The result is: {result}")
