#Prmpt the user to enter a positive integer
integer = int(input("Enter the size of the pattern: "))

#while loop to iterate through each row
count = 0
while count != integer:
    for i in range(integer): #print one row of *
        print("*", end = "")
    print() #move to next line
    count += 1  # increment
