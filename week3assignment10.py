

#Input
age_input = input("Enter your age: ")

#Processing
if age_input.isdigit():
    age = int(age_input)

    if age > 0:
        if age < 18:
            print("Minor")
        elif 18 <= age <= 65:
            print("Adult")
        else:
            print("Senior Citizen")
    else:
        print("Error: Age must be a positive number!")
else:
    print("Error: Invalid Input. Please enter a positive number.")