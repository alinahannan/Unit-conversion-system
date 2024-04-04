import streamlit as st

# Temperature conversion functions
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

# Length conversion functions
def meters_to_feet(meters):
    return meters * 3.281

def feet_to_meters(feet):
    return feet / 3.281

# Weight conversion functions
def kilograms_to_pounds(kilograms):
    return kilograms * 2.205

def pounds_to_kilograms(pounds):
    return pounds / 2.205

# Area conversion functions
def square_meters_to_square_feet(square_meters):
    return square_meters * 10.764

def square_feet_to_square_meters(square_feet):
    return square_feet / 10.764

# Volume conversion functions
def liters_to_gallons(liters):
    return liters * 0.264

def gallons_to_liters(gallons):
    return gallons / 0.264

# Streamlit UI
st.title("Unit Converter")

conversion_type = st.selectbox("Select conversion type:", ["Temperature", "Length", "Weight", "Area", "Volume"])

if conversion_type == "Temperature":
    temperature = st.number_input("Enter temperature:")
    conversion_from = st.selectbox("Convert from:", ["Celsius", "Fahrenheit", "Kelvin"])
    conversion_to = st.selectbox("Convert to:", ["Celsius", "Fahrenheit", "Kelvin"])
    
    if conversion_from == conversion_to:
        st.warning("Please select different units for conversion.")
    else:
        if conversion_from == "Celsius":
            if conversion_to == "Fahrenheit":
                result = celsius_to_fahrenheit(temperature)
            elif conversion_to == "Kelvin":
                result = celsius_to_kelvin(temperature)
        elif conversion_from == "Fahrenheit":
            if conversion_to == "Celsius":
                result = fahrenheit_to_celsius(temperature)
            elif conversion_to == "Kelvin":
                result = fahrenheit_to_kelvin(temperature)
        elif conversion_from == "Kelvin":
            if conversion_to == "Celsius":
                result = kelvin_to_celsius(temperature)
            elif conversion_to == "Fahrenheit":
                result = kelvin_to_fahrenheit(temperature)

        if result is not None:
            st.success(f"The converted temperature is {result:.2f} {conversion_to}.")

elif conversion_type == "Length":
    length = st.number_input("Enter length:")
    conversion_from = st.selectbox("Convert from:", ["Meters", "Feet"])
    conversion_to = st.selectbox("Convert to:", ["Meters", "Feet"])
    
    if conversion_from == conversion_to:
        st.warning("Please select different units for conversion.")
    else:
        if conversion_from == "Meters":
            result = meters_to_feet(length) if conversion_to == "Feet" else length
        else:
            result = feet_to_meters(length) if conversion_to == "Meters" else length

        st.success(f"The converted length is {result:.2f} {conversion_to}.")

elif conversion_type == "Weight":
    weight = st.number_input("Enter weight:")
    conversion_from = st.selectbox("Convert from:", ["Kilograms", "Pounds"])
    conversion_to = st.selectbox("Convert to:", ["Kilograms", "Pounds"])
    
    if conversion_from == conversion_to:
        st.warning("Please select different units for conversion.")
    else:
        if conversion_from == "Kilograms":
            result = kilograms_to_pounds(weight) if conversion_to == "Pounds" else weight
        else:
            result = pounds_to_kilograms(weight) if conversion_to == "Kilograms" else weight

        st.success(f"The converted weight is {result:.2f} {conversion_to}.")

elif conversion_type == "Area":
    area = st.number_input("Enter area:")
    conversion_from = st.selectbox("Convert from:", ["Square Meters", "Square Feet"])
    conversion_to = st.selectbox("Convert to:", ["Square Meters", "Square Feet"])
    
    if conversion_from == conversion_to:
        st.warning("Please select different units for conversion.")
    else:
        if conversion_from == "Square Meters":
            result = square_meters_to_square_feet(area) if conversion_to == "Square Feet" else area
        else:
            result = square_feet_to_square_meters(area) if conversion_to == "Square Meters" else area

        st.success(f"The converted area is {result:.2f} {conversion_to}.")

elif conversion_type == "Volume":
    volume = st.number_input("Enter volume:")
    conversion_from = st.selectbox("Convert from:", ["Liters", "Gallons"])
    conversion_to = st.selectbox("Convert to:", ["Liters", "Gallons"])
    
    if conversion_from == conversion_to:
        st.warning("Please select different units for conversion.")
    else:
        if conversion_from == "Liters":
            result = liters_to_gallons(volume) if conversion_to == "Gallons" else volume
        else:
            result = gallons_to_liters(volume) if conversion_to == "Liters" else volume

        st.success(f"The converted volume is {result:.2f} {conversion_to}.")
