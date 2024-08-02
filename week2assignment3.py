#This is the input
Weight = float(input("What is your weight in Kilograms?: "))
Height = float(input("What is your height in Meters?: "))

#This is the processing
BMI = Weight / (Height ** 2)

#This is the output
print("Your Body Mass Index (BMI) is: " + str(BMI))