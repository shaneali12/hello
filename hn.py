import streamlit as st
import requests

st.set_page_config(page_title="Currency Converter", layout="centered")
st.title("💱 Currency Converter")
st.write("Created By Shan E Ali", wide=20)

# API Call
url = "https://api.exchangerate-api.com/v4/latest/USD"  # Default base for all rates
response = requests.get(url)
data = response.json()
rates = data["rates"]

# Currency list
currencies = list(rates.keys())

# User Input
from_currency = st.selectbox("From Currency", currencies, index=currencies.index("USD"))
to_currency = st.selectbox("To Currency", currencies, index=currencies.index("PKR"))
amount = st.number_input (f"Amount", min_value=0.0)

# Convert
if st.button("Convert"):
    # Get rates for base as from_currency
    new_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    new_data = requests.get(new_url).json()
    rate = new_data["rates"][to_currency]
    converted = amount * rate
    st.success(f"{amount} {from_currency} = {converted} {to_currency}")