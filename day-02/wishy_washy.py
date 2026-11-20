import random

def generate_minutes():
    return random.randint(30, 180)

def calc_amount(machine_type, minutes):
    hourly_rates = {
        "standard": 50.00,
        "heavy": 75.00,
        "industrial": 100.00
    }
    hours = minutes / 60
    machine = machine_type.strip().lower()
    amount_before_vat = hours * hourly_rates[machine]
    return round(amount_before_vat, 2)

def calc_total_amount(amount):
    vat_rate = 0.14
    vat_amount = round(amount * vat_rate, 2)
    total_payable = round(amount + vat_amount, 2)
    return vat_amount, total_payable

def display_summary(payments):
    num_customers = len(payments)
    total_combined = sum(payments)
    average_payment = total_combined / num_customers
    highest_payment = max(payments)
    lowest_payment = min(payments)

    print("\n==============================")
    print("        DAILY SUMMARY         ")
    print("==============================")
    print(f"Number of customers processed: {num_customers}")
    print(f"Combined amount payable:       R{total_combined:.2f}")
    print(f"Average payment per customer:  R{average_payment:.2f}")
    print(f"Highest payment:               R{highest_payment:.2f}")
    print(f"Lowest payment:                R{lowest_payment:.2f}")
    print("==============================")

def process_payments():
    num_customers = int(input("Enter the number of customers to process: "))
    payments = []

    for i in range(1, num_customers + 1):
        print(f"\n--- Customer {i} ---")
        
        # 1. Prompt for the customer name and machine type
        customer_name = input("Enter customer name: ").strip()
        machine_type = input("Enter machine type (standard, heavy, industrial): ").strip()

        # 2. Call generate_minutes() to obtain the simulated usage time
        minutes = generate_minutes()

        # 3. Call calc_amount() to calculate the amount before VAT
        amount_before_vat = calc_amount(machine_type, minutes)

        # 4. Call calc_total_amount() to obtain the VAT and total payable
        vat_amount, total_payable = calc_total_amount(amount_before_vat)

        # 5. Append the total payable to the payments list
        payments.append(total_payable)

        # 6. Display an invoice for the customer
        print("\n------------------------------")
        print("           INVOICE            ")
        print("------------------------------")
        print(f"Customer Name:     {customer_name}")
        print(f"Machine Type:      {machine_type.capitalize()}")
        print(f"Generated Minutes: {minutes}")
        print(f"Amount Before VAT: R{amount_before_vat:.2f}")
        print(f"VAT Amount:        R{vat_amount:.2f}")
        print(f"Total Payable:     R{total_payable:.2f}")
        print("------------------------------")

    # Pass the payments list to display_summary() after processing all customers
    display_summary(payments)

# Start the program
process_payments()