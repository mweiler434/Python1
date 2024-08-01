#This is the input
Principal = int(input("What is the Principal Amount?: "))
Rate = int(input("What is the Interest Rate in percentage?: "))
Time = int(input("What is the Time Period in Years?: "))

#This is the processing
Interest = Principal*Rate*Time/100

#This is the output
print("The Calculated Simple Interest is:", Interest)