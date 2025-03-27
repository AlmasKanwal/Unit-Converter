# import streamlit as st

# # Title of Project
# st.markdown("<h1 class='title'>🔁 Unit Converter App</h1>", unsafe_allow_html=True)
# # st.markdown("<h4 class=subtitle'>Convert📏Length, ⚖️Weight, 🌡️Temperature, 🥤Volume, 🚀Speed, ⏳Time, 🔋Energy, ⚡Power, 🌪️Pressure and 💾Digital Storage Instantly</h4>", unsafe_allow_html=True)
# st.markdown("<h3 class=subtitle'>Convert Length, Weight, Temperature and more!</h3>", unsafe_allow_html=True)

# # categories of units
# categories = ["Length", "Weight", "Temperature", "Volume", "Speed", "Time", "Energy", "Power", "Pressure", "Digital Storage"]
# choice = st.selectbox("Choose a Category", categories)

# # 1. Length Category
# def length_converter(value, from_unit, to_unit):
#     conversions = {
#         "mm": {"cm": 0.1, "m": 0.001, "km": 0.000001, "in": 0.03937},
#         "cm": {"m": 0.01, "in": 0.3937},
#         "m": {"km": 0.001, "in": 39.37, "ft": 3.2808, "yd": 1.0936},
#         "km": {"mi": 0.6214},
#         "in": {"cm": 2.54, "mm": 25.4},
#         "ft": {"m": 0.3048, "in": 12},
#         "yd": {"m": 0.9144},
#         "mi": {"km": 1.609}
#     }
#     return value * conversions[from_unit][to_unit]

# # 2. Weight Category
# def weight_converter(value, from_unit, to_unit):
#     conversions = {
#         "mg": {"g": 0.001},
#         "g": {"kg": 0.001},
#         "kg": {"t": 0.001, "lb": 2.2046},
#         "lb": {"kg": 0.4536, "oz": 16},
#         "oz": {"g": 28.35},
#         "st": {"kg": 6.35}
#     }
#     return value * conversions[from_unit][to_unit]

# # 3. Temperature Category
# def temperature_converter(value, from_unit, to_unit):
#     if from_unit == "°C" and to_unit == "°F": 
#         return (value * 9/5) + 32
#     elif from_unit == "°F" and to_unit == "°C":
#         return (value - 32) * 5/9
#     elif from_unit == "°C" and to_unit == "K":
#         return value + 273.15
#     elif from_unit == "K" and to_unit == "°C":
#         return value - 273.15
    
# # 4. Volume Category
# def volume_converter(value, from_unit, to_unit):
#     conversions = {
#         "mL": {"L": 0.001},
#         "L": {"m³": 0.001}, 
#         "US": {"L": 3.785},
#         "pt": {"L": 0.4732}
#     }
#     return value * conversions[from_unit][to_unit]

# # 5. Speed Category
# def speed_converter(value, from_unit, to_unit):
#     conversions = {
#         "m/s": {"km/h": 3.6},
#         "km/h": {"mph": 0.6214},
#         "mph": {"km/h": 1.609},
#         "kn": {"km/h": 1.852}
#     }
#     return value * conversions[from_unit][to_unit]

# # 6. Time Category
# def time_converter(value, from_unit, to_unit):
#     conversions = {
#         "s": {"min": 0.01667},
#         "min": {"h": 0.01667},
#         "h": {"d": 0.04167},
#         "d": {"wk": 0.1429},
#         "wk": {"mo": 0.2295},
#         "mo": {"yr": 0.08333}
#     }
#     return value * conversions[from_unit][to_unit]

# # 7. Energy Category
# def energy_converter(value, from_unit, to_unit):
#     conversions = {
#         "J": {"kJ": 0.001, "cal": 0.239},
#         "kcal": {"J": 4184}
#     }
#     return value * conversions[from_unit][to_unit]

# # 8. Power Category
# def power_converter(value, from_unit, to_unit):
#     conversions = {
#         "W": {"kW": 0.001},
#         "kW": {"hp": 1.341}
#     }
#     return value * conversions[from_unit][to_unit]

# # 9. Pressure Category
# def pressure_converter(value, from_unit, to_unit):
#     conversions = {
#         "Pa": {"kPa": 0.001},
#         "kPa": {"bar": 0.01},
#         "bar": {"atm": 0.9869},
#         "atm": {"psi": 14.696}
#     }
#     return value * conversions[from_unit][to_unit]

# # 10. Digital Storage Category
# def digital_storage_converter(value, from_unit, to_unit):
#     conversions = {
#         "b": {"B": 0.125},
#         "B": {"KB": 0.001},
#         "KB": {"MB": 0.001},
#         "MB": {"GB": 0.001},
#         "GB": {"TB": 0.001}
#     }
#     return value * conversions[from_unit][to_unit]

# value = st.number_input("Enter Value for Conversion")

# # Unit Choices 
# if choice == "Length":
#     from_unit = st.selectbox("Convert From", ["mm", "cm", "m", "km", "in", "ft", "yd", "mi"])
#     to_unit = st.selectbox("Convert To", [i for i in ["mm", "cm", "m", "km", "in", "ft", "yd", "mi"] if i != from_unit])
#     result = length_converter(value, from_unit, to_unit)

# elif choice == "Weight":
#     from_unit = st.selectbox("Convert From", ["mg", "g", "kg", "lb", "oz"])
#     to_unit = st.selectbox("Convert To", [i for i in ["g", "kg", "t", "oz"]])
#     result = weight_converter(value, from_unit, to_unit)

# elif choice == "Temperature":




# # Submit 
# if st.button("Convert"):
#     st.success(f"Converted Value: {result:.2f} {to_unit}")


