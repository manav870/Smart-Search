import requests

def convert_currency(amount, from_currency, to_currency="USD"):
    try:
        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        
        if 'rates' not in data:
            return "Invalid response format"
        
        rate = data['rates'].get(to_currency)
        if rate:
            return round(amount * rate, 2)
        return "Conversion Error: Rate not found"
    except requests.exceptions.RequestException as e:
        return f"Request error: {e}"
    except ValueError:
        return "Error parsing response"
    except Exception as e:
        return f"An unexpected error occurred: {e}"
