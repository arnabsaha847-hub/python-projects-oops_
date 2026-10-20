
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total(self):
        return self.price * self.quantity


class Bill:
    def __init__(self, tax_rate=5):
        self.products = []
        self.tax_rate = tax_rate

    def add_product(self, product):
        self.products.append(product)

    def display_bill(self):
        print("\n" + "=" * 60)
        print("                 CUSTOMER BILL")
        print("=" * 60)
        print(f"{'Product':<20}{'Price':>10}{'Qty':>8}{'Total':>12}")
        print("-" * 60)

        subtotal = 0

        for product in self.products:
            total = product.get_total()
            subtotal += total
            print(f"{product.name:<20}{product.price:>10.2f}"
                  f"{product.quantity:>8}{total:>12.2f}")

        tax = subtotal * self.tax_rate / 100
        grand_total = subtotal + tax

        print("-" * 60)
        print(f"{'Subtotal:':>46} {subtotal:>10.2f}")
        print(f"{'Tax (' + str(self.tax_rate) + '%):':>46} {tax:>10.2f}")
        print("=" * 60)
        print(f"{'Grand Total:':>46} {grand_total:>10.2f}")
        print("=" * 60)


# Creating products
p1 = Product("Notebook", 50, 2)
p2 = Product("Pen", 10, 5)
p3 = Product("School Bag", 800, 1)

# Creating bill
bill = Bill(5)

bill.add_product(p1)
bill.add_product(p2)
bill.add_product(p3)

# Display final bill
bill.display_bill()
