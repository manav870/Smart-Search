import requests

def convert_currency(amount, from_currency, to_currency="USD"):
    try:
        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(url).json()
        rate = response['rates'].get(to_currency)
        if rate:
            return round(amount * rate, 2)
        return "Conversion Error"
    except Exception as e:
        return f"Error: {e}"
