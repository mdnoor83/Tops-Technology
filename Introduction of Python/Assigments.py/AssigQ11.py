"""11) Write a Python program to test whether a passed letter is a vowel
or not.
"""

Alpha = ['a','e','i','o','u','A','E','I','O','U']
input1  = input("Enter the character = ")

if (input1 in Alpha):
    print("Vowels!")
else:
    print("It's not!")