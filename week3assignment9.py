

#Input
char_input = input("Enter a single character: ")

#Processing
if len(char_input) == 1 and char_input.isalpha():
    char = char_input.lower()
    if char in 'aeiou':
        print("The character is a Vowel.")
    else:
        #Output
        print("The character is a Consonant.")
else:
    if len(char_input) != 1:
        #Output
        print("Error: Please enter only one character.")
    else:
        #Output
        print("Error: The input is not a letter.")