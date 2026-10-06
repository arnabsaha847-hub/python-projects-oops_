def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

choice = input("Enter C for Celsius to Fahrenheit or F for Fahrenheit to Celsius: ")

if choice.upper() == "C":
    c = float(input("Enter temperature in Celsius: "))
    print("Temperature in Fahrenheit:", celsius_to_fahrenheit(c))

elif choice.upper() == "F":
    f = float(input("Enter temperature in Fahrenheit: "))
    print("Temperature in Celsius:", fahrenheit_to_celsius(f))

else:
    print("Invalid choice")