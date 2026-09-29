
def Convert_temperature(value , unit):
    if unit == "c":
        return (value * 9/5) + 32
    elif unit == "f":
        return (value - 32) * 5/9
    else:
        return "Invalid unit. Please use 'c' for Celsius or 'f' for Fahrenheit."
    
#testing
print("25 degrees Celsius is equal to", Convert_temperature(25, "c"), "degrees Fahrenheit.")
print("77 degrees Fahrenheit is equal to", Convert_temperature(77, "f"), "degrees Celsius.")
print("100 degrees Celsius is equal to", Convert_temperature(100, "c"), "degrees Fahrenheit.")