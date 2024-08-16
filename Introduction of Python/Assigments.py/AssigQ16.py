"""16) Write a Python program to count the number of characters
(character frequency) in a string
"""

# Input a string from the user
input_string = input("Enter a string: ")

# Initialize an empty dictionary to store character frequencies
char_frequency = {}

# Count the frequency of each character in the string
for char in input_string:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

# Print the character frequencies
for char, frequency in char_frequency.items():
    print(f"Character '{char}' appears {frequency} times.")
