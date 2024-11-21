feet_inches = input("Enter feet and inches: ")

def convert(feet_inches):
    [feet, inches] = feet_inches.split(" ")
    meters = float(feet) * 0.3048 + float(inches) * 0.0254
    # return f"{feet} feet and {inches} inches is equal to {meters} meters."
    # Decoupling is the process of separating the code that handles one task from the code that handles another
    return meters
    
    # parts = feet_inches.split(" ")
    # print(f'Feet: {parts[0]}')


# print(convert(feet_inches=feet_inches))
result = convert(feet_inches)

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")