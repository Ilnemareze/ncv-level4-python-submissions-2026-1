def amount_due(facility_code, hours):
    rates = {
        "squa": 13.00,
        "swim": 12.00,
        "gym": 11.00,
        "wei": 8.00
    }
    code = facility_code.strip().lower()
    hourly_rate = rates[code]
    return hourly_rate * hours

def final_amount_due(amount):
    vat_rate = 0.14
    return amount + (amount * vat_rate)

def display(name, final_amount):
    print("\n--- Payment Receipt ---")
    print(f"Customer Name: {name}")
    print(f"Amount Due:    R{final_amount:.2f}")

def process_payment():
    name = input("Enter customer's name: ").strip()
    facility_code = input("Enter facility code (squa, swim, gym, wei): ").strip()
    hours = float(input("Enter number of hours: "))

    subtotal = amount_due(facility_code, hours)

    final_total = final_amount_due(subtotal)

    display(name, final_total)

process_payment()
