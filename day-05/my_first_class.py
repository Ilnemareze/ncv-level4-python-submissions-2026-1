class Product:
    VAT_RATE = 0.15
    PERCENTAGE = 0.1

    def __init__(self, code, name, price, colour):
        self.code = code
        self.name = name
        self.colour = colour
        
        # Convert price to float so math calculations work properly
        price = float(price)
        if price < 0:
            raise ValueError("Price can not be negative!!")
        self.price = price

    def __str__(self):
        return f"{self.code} - {self.name}({self.colour}): R{self.price:.2f}"

    # Calculates the VAT in rands
    def calc_vat(self):
        return self.price * self.VAT_RATE

    # Add VAT rands to price
    def calc_price_including_vat(self):
        return self.price + self.calc_vat()

    # Calculate discount in rands
    def calc_discount(self):
        return self.calc_price_including_vat() * self.PERCENTAGE

    # Subtract discount rands from price including VAT
    def apply_discount(self):
        return self.calc_price_including_vat() - self.calc_discount()


# Output
def main():
    product1 = Product("home01", "Airfrier", "100", "black")
    print(product1)
    print(f"VAT: R{product1.calc_vat():.2f}")
    print(f"Product including VAT: R{product1.calc_price_including_vat():.2f}")
    print(f"10% Discount amount: R{product1.calc_discount():.2f}")
    print(f"Payable: R{product1.apply_discount():.2f}")


# Program start
if __name__ == "__main__":
    main()
