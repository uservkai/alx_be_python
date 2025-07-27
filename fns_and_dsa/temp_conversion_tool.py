FAHRENHEIT_TO_CELCIUS_FACTOR = 5/9
CELCIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celcius(fahrenheit):
    temp_c = (fahrenheit - 32) * FAHRENHEIT_TO_CELCIUS_FACTOR
    print(f"{fahrenheit}°F is {temp_c}°C")
    return temp_c

def convert_to_fahrenheit(celcius):
        temp_f = (celcius * CELCIUS_TO_FAHRENHEIT_FACTOR) + 32
        print(f"{celcius}°C is {temp_f}°C")
        return temp_f


temp = float(input("Enter the temperature to convert: "))
unit = input("Is the temperature in Celcius or Fahrenheit? (C/F): ").upper()

if unit == "F":
    convert_to_celcius(temp)
elif unit == "C":
    convert_to_fahrenheit(temp)
else:
    print("Invalid Entry. Please enter 'C' or 'F'. ")
