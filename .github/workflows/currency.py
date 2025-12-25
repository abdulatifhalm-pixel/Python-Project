# Simple Currency Converter
# Works offline with sample exchange rates

def currency_converter(amount, from_currency, to_currency):
    # Exchange rates relative to 1 USD (you can update these)
    rates = {
        'USD': 1.0,
        'EUR': 0.93,
        'GBP': 0.79,
        'INR': 83.2,
        'JPY': 151.2,
        'afg': 0.99
    }

    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    if from_currency not in rates or to_currency not in rates:
        return "❌ Unsupported currency!"

    # Convert from base -> USD -> target
    amount_in_usd = amount / rates[from_currency]
    converted_amount = amount_in_usd * rates[to_currency]
    return round(converted_amount, 2)


# Main program
print("💱 Simple Currency Converter 💱")
print("Available currencies: USD, EUR, GBP, INR, JPY, afg")

try:
    amount = float(input("Enter amount: "))
    from_curr = input("From currency: ")
    to_curr = input("To currency: ")

    result = currency_converter(amount, from_curr, to_curr)
    print(f"\n💰 {amount} {from_curr.upper()} = {result} {to_curr.upper()}")
except ValueError:
    print("❌ Please enter a valid number for amount.")
