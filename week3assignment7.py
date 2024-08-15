#This is the input
year = int(input("Please Enter a Year: "))

#This is the processing to determine whether the year is a leap year or not
if (year % 4 == 0 and year % 100 != 0) or (year%400 == 0):
    is_leap_year = True
else:
    is_leap_year = False

#This is the output
if is_leap_year:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
