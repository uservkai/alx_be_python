#user inputs a number
number = int(input("Enter a number to see its multiplication table: "))

#for loop to iterate through the loops
for i in range (1, 11):
    result = number * i
    print (f"{number} * {i} = {result}" )
