def convert_temperature(temperature, unit):
    if unit == 'F':
        # Convert Fahrenheit to Celsius
        converted_temperature = (temperature - 32) * 5 / 9
    elif unit == 'C':
        # Convert Celsius to Fahrenheit
        converted_temperature = (temperature * 9 / 5) + 32
    else:
        return "Invalid unit. Please provide 'F' for Fahrenheit or 'C' for Celsius."
    
    # Round the result to 2 decimal places
    converted_temperature = round(converted_temperature, 2)
    return converted_temperature

# Convert Fahrenheit to Celsius
fahrenheit_temperature = 100.0
celsius_result = convert_temperature(fahrenheit_temperature, 'F')
print(f"{fahrenheit_temperature}°F is {celsius_result}°C")

# Convert Celsius to Fahrenheit
celsius_temperature = 37.78
fahrenheit_result = convert_temperature(celsius_temperature, 'C')
print(f"{celsius_temperature}°C is {fahrenheit_result}°F")
