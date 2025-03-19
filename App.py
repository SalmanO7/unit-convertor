import streamlit as st

conversion_factors = {
    ("meters", "kilometers"): 0.001,
    ("kilometers", "meters"): 1000,
    ("meters", "centimeters"): 100,
    ("centimeters", "meters"): 0.01,
    ("meters", "millimeters"): 1000,
    ("millimeters", "meters"): 0.001,
    ("grams", "kilograms"): 0.001,
    ("kilograms", "grams"): 1000,
    ("grams", "pounds"): 0.00220462,
    ("pounds", "grams"): 453.592,
    ("kilograms", "pounds"): 2.20462,
    ("pounds", "kilograms"): 0.453592,
    ("liters", "milliliters"): 1000,
    ("milliliters", "liters"): 0.001,
}

def unit_converts(value, from_unit, to_unit):
    """Convert the given value from one unit to another."""
    if from_unit == to_unit:
        return value  
    
    key = (from_unit, to_unit)  
    
    if key in conversion_factors:
        return value * conversion_factors[key]
    else:
        return None  
    
st.title("Unit Converter App 👀")

value = st.number_input("Enter a value to convert", min_value=1.0, step=0.1)

from_units = sorted(set([pair[0] for pair in conversion_factors.keys()]))
from_unit = st.selectbox("Select a unit to convert from", from_units)

valid_to_units = sorted([pair[1] for pair in conversion_factors.keys() if pair[0] == from_unit])
to_unit = st.selectbox("Select a unit to convert to", valid_to_units)

if st.button("Convert"):
    result = unit_converts(value, from_unit, to_unit)

    if result is not None:
        st.success(f"Converted Value: {result}")
    else:
        st.error(f"Conversion from {from_unit} to {to_unit} is not supported!")

st.write("Made by Muhammad Salman ❤️")
