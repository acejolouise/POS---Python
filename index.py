class Product:
    def __init__(self, name, price, barcode):
        self.name = name
        self.price = price
        self.barcode = barcode

class CashierSystem:
    def __init__(self):
        self.inventory = {
            "123456": Product("Gatas", 120.00, "123456"),
            "789012": Product("Pandesal", 57.00, "789012"),
            "345678": Product("Itlog", 12.00, "345678"),
            "901234": Product("Bigas", 44.00, "901234")
        }
        self.cart = []
        self.discount_rate = 0.1

    def scan_item(self, barcode):
        if barcode in self.inventory:
            self.cart.append(self.inventory[barcode])
            print(f"Scanned: {self.inventory[barcode].name} - ₱{self.inventory[barcode].price:.2f}")
        else:
            print("Item not found!")

    def calculate_subtotal(self):
        return sum(item.price for item in self.cart)

    def apply_discount(self, subtotal):
        # Apply 10% discount if total is over ₱500
        if subtotal > 500:
            discount = subtotal * self.discount_rate
            print(f"Applied {self.discount_rate * 100}% discount: -₱{discount:.2f}")
            return subtotal - discount
        return subtotal

    def calculate_total(self):
        subtotal = self.calculate_subtotal()
        return self.apply_discount(subtotal)

    def process_payment(self, amount_paid):
        total = self.calculate_total()
        if amount_paid >= total:
            change = amount_paid - total
            print(f"Payment successful! Change: ₱{change:.2f}")
            self.print_receipt()
            self.cart = []  # Clear cart after payment
            return True
        else:
            print(f"Insufficient payment. Total due: ₱{total:.2f}")
            return False

    def print_receipt(self):
        print("\n=== Receipt ===")
        for item in self.cart:
            print(f"{item.name}: ₱{item.price:.2f}")
        subtotal = self.calculate_subtotal()
        total = self.calculate_total()
        print(f"Subtotal: ₱{subtotal:.2f}")
        if total != subtotal:
            print(f"Discount applied: -₱{(subtotal - total):.2f}")
        print(f"Total: ₱{total:.2f}")
        print("==============\n")

    def run(self):
        print("Welcome to the Cashier System!")
        while True:
            print("\nOptions: (1) Scan Item (2) View Cart (3) Checkout (4) Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                barcode = input("Enter barcode: ")
                self.scan_item(barcode)

            elif choice == "2":
                if self.cart:
                    print("\nCurrent Cart:")
                    for item in self.cart:
                        print(f"{item.name}: ₱{item.price:.2f}")
                    print(f"Subtotal: ₱{self.calculate_subtotal():.2f}")
                else:
                    print("Cart is empty!")

            elif choice == "3":
                if not self.cart:
                    print("Cart is empty!")
                    continue
                total = self.calculate_total()
                print(f"Total due: ₱{total:.2f}")
                try:
                    amount_paid = float(input("Enter payment amount: ₱"))
                    self.process_payment(amount_paid)
                except ValueError:
                    print("Invalid amount entered!")

            elif choice == "4":
                print("Thank you for using the Cashier System!")
                break

            else:
                print("Invalid option!")


if __name__ == "__main__":
    cashier = CashierSystem()
    cashier.run()