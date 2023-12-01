class CashRegister:
    def __init__(self, discount=0):
        self.items = []
        self.prices = []
        self.quantities = []
        self.discount = discount
        self.last_transaction_amount = 0


    def add_item(self, item, price, quantity=1):
        self.items.append(item)
        self.prices.append(price)
        self.quantities.append(quantity)
        self.last_transaction_amount = price * quantity  # Update last_transaction_amount



    def calculate_discount(self):
        return self.last_transaction_amount * (self.discount / 100)

    def apply_discount(self):
        discount_amount = self.calculate_discount()
        self.last_transaction_amount -= discount_amount
        self.last_transaction_amount = round(self.last_transaction_amount, 2)  # Round to 2 decimal places
        return self.last_transaction_amount



    @property
    def total(self):
        total_amount = sum([price * quantity for price, quantity in zip(self.prices, self.quantities)])
        return total_amount - self.calculate_discount()


    def void_last_transaction(self):
        self.items.pop()
        self.prices.pop()
        self.quantities.pop()
        self.last_transaction_amount = 0

    def setup_method(self):
        self.cash_register = CashRegister()
        self.cash_register_with_discount = CashRegister(discount=20)
