import streamlit as st

st.markdown("""
    <style>
        /* Styling for title and subtitle */
        .title {
            color: #0d6efd;
            text-align: center;
            font-size: 2.5rem;
            font-weight: bold;
        }
        .subtitle {
            color: #6c757d;
            text-align: center;
            font-size: 1.2rem;
        }
    </style>
""", unsafe_allow_html=True)

# Title of Project
st.markdown("<h1 class='title'>🔁 Unit Converter App</h1>", unsafe_allow_html=True)
st.markdown("<h4 class='subtitle'>Convert📏Length, ⚖️Weight, 🌡️Temperature, 🥤Volume, 🚀Speed, ⏳Time, 🔋Energy, ⚡Power, 🌪️Pressure and 💾Digital Storage Instantly</h4>", unsafe_allow_html=True)

# categories of units
categories = ["Length", "Weight", "Temperature", "Volume", "Speed", "Time", "Energy", "Power", "Pressure", "Digital Storage"]
choice = st.selectbox("**🔹 Choose a Category**", categories)

# 1. Conversion Logic (Categories / Dictionary)
conversion_dict = {
    "Length": {
        "mm": {"cm": 0.1, "m": 0.001, "km": 0.000001, "in": 0.03937},
        "cm": {"m": 0.01, "in": 0.3937},
        "m": {"km": 0.001, "in": 39.37, "ft": 3.2808, "yd": 1.0936},
        "km": {"mi": 0.6214},
        "in": {"cm": 2.54, "mm": 25.4},
        "ft": {"m": 0.3048, "in": 12},
        "yd": {"m": 0.9144},
        "mi": {"km": 1.609}
    },
    "Weight": {
        "mg": {"g": 0.001},
        "g": {"kg": 0.001},
        "kg": {"t": 0.001, "lb": 2.2046},
        "lb": {"kg": 0.4536, "oz": 16},
        "oz": {"g": 28.35},
        "st": {"kg": 6.35}
    },
    "Temperature": {
        "°C": {"°F": lambda t: (t * 9/5) + 32, "K": lambda t: t + 273.15}, 
        "°F": {"°C": lambda t: (t - 32) * 5/9},
        "K": {"°C": lambda t: t - 273.15}
    },
    "Volume": {
        "mL": {"L": 0.001},
        "L": {"m³": 0.001}, 
        "US": {"L": 3.785},
        "pt": {"L": 0.4732}
    },
    "Speed": {
        "m/s": {"km/h": 3.6},
        "km/h": {"mph": 0.6214},
        "mph": {"km/h": 1.609},
        "kn": {"km/h": 1.852}
    },
    "Time": {
        "s": {"min": 0.01667},
        "min": {"h": 0.01667},
        "h": {"d": 0.04167},
        "d": {"wk": 0.1429},
        "wk": {"mo": 0.2295},
        "mo": {"yr": 0.08333}
    },
    "Energy": {
        "J": {"kJ": 0.001, "cal": 0.239},
        "kcal": {"J": 4184}
    },
    "Power": {
        "W": {"kW": 0.001},
        "kW": {"hp": 1.341}
    },
    "Pressure": {
        "Pa": {"kPa": 0.001},
        "kPa": {"bar": 0.01},
        "bar": {"atm": 0.9869},
        "atm": {"psi": 14.696}
    },
    "Digital Storage": {
        "b": {"B": 0.125},
        "B": {"KB": 0.001},
        "KB": {"MB": 0.001},
        "MB": {"GB": 0.001},
        "GB": {"TB": 0.001}
    }
    }

# Sidebar Heading
st.sidebar.header("📌 Conversion Details")

# Conversion Table
conversion_table = {
    "Length": {
        "mm": ["cm", "m", "km", "in"],
        "cm": ["m", "in"],
        "m": ["km", "in", "ft", "yd"],
        "km": ["mi"],
        "in": ["cm", "mm"],
        "ft": ["m", "in"],
        "yd": ["m"],
        "mi": ["km"]
    },
    "Weight": {
        "mg": ["g"],
        "g": ["kg"],
        "kg": ["t", "lb"],
        "lb": ["kg", "oz"],
        "oz": ["g"],
        "st": ["kg"]
    },
    "Temperature": {
        "°C": ["°F", "K"], 
        "°F": ["°C"],
        "K": ["°C"]
    },
     "Volume": {
        "mL": ["L"],
        "L": ["m³"], 
        "US": ["L"],
        "pt": ["L"]
    },
    "Speed": {
        "m/s": ["km/h"],
        "km/h": ["mph"],
        "mph": ["km/h"],
        "kn": ["km/h"]
    },
     "Time": {
        "s": ["min"],
        "min": ["h"],
        "h": ["d"],
        "d": ["wk"],
        "wk": ["mo"],
        "mo": ["yr"]
    },
    "Energy": {
        "J": ["kJ", "cal"],
        "kcal": ["J"]
    },
     "Power": {
        "W": ["kW"],
        "kW": ["hp"]
    },
    "Pressure": {
        "Pa": ["kPa"],
        "kPa": ["bar"],
        "bar": ["atm"],
        "atm": ["psi"]
    },
    "Digital Storage": {
        "b": ["B"],
        "B": ["KB"],
        "KB": ["MB"],
        "MB": ["GB"],
        "GB": ["TB"]
    }
    }

# Show Conversion Details in Sidebar Dynamically
if choice in conversion_table:
    st.sidebar.write("ℹ️ **Hint:** Follow the format below for unit conversions 👇:")
    st.sidebar.write(f"### 🔹 {choice} Conversions:")
    st.sidebar.write("**Convert From → Convert To**")
    for unit, conversions in conversion_table[choice].items():
        st.sidebar.write(f"**{unit}** → {', '.join(conversions)}")
    st.sidebar.write("✅ Only select conversions that are available in the Convertion Section 👆!")

# User Input Value for Conversion
value = st.number_input("**🔢 Enter Value for Conversion**", min_value=0.0)

if choice in conversion_table:
    valid_units_choice = list(conversion_table[choice].keys())
    from_units = st.selectbox("**📍 Convert From**", valid_units_choice)
    to_units = st.selectbox("**🎯 Convert To**", [i for i in valid_units_choice if i != from_units])


# Convert Button 
    if st.button("Convert"):
        if choice in conversion_dict:
            conversions = conversion_dict[choice]
            if from_units in conversions and to_units in conversions[from_units]:
                conversion_value = conversions[from_units][to_units]
                if callable(conversion_value):
                    result = conversion_value(value)
                else:
                    result = value * conversion_value
                st.success(f"Converted Value: {result:.2f} {to_units}")
            else:
                st.error("Conversion not available for selected units!")

