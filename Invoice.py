class Invoice:

    def __init__(self):
        self.items = {}

    def addProduct(self, qnt, price, discount, fed_tax, state_tax):
        self.items['qnt'] = qnt
        self.items['unit_price'] = price
        self.items['discount'] = discount
        self.items['fed_tax'] = fed_tax
        self.items['state_tax'] = state_tax
        return self.items

    def totalImpurePrice(self, products):
        total_impure_price = 0
        for k, v in products.items():
            total_impure_price += float(v['unit_price']) * int(v['qnt'])
        total_impure_price = round(total_impure_price, 2)
        return total_impure_price

    def totalDiscount(self, products):
        total_discount = 0
        for k, v in products.items():
            total_discount += (int(v['qnt']) * float(v['unit_price'])) * float(v['discount']) / 100
        total_discount = round(total_discount, 2)
        self.total_discount = total_discount
        return total_discount

    def totalFedTax(self, products):
        total_fed_tax = 0
        for k, v in products.items():
            total_fed_tax += (int(v['qnt']) * float(v['unit_price']) * float(v['fed_tax']) / 100)
        total_fed_tax = round(total_fed_tax, 2)
        self.total_fed_tax = total_fed_tax
        return total_fed_tax

    def totalStateTax(self, products):
        total_state_tax = 0
        for k, v in products.items():
            total_state_tax += (int(v['qnt']) * float(v['unit_price']) * float(v['state_tax']) / 100)
        total_state_tax = round(total_state_tax, 2)
        self.total_state_tax = total_state_tax
        return total_state_tax

    def totalPurePrice(self, products):
        total_pure_price = self.totalImpurePrice(products) - self.totalDiscount(products) + self.totalFedTax(products) \
                         + self.totalStateTax(products)
        return total_pure_price

    def inputAnswer(self, input_value):
        while True:
            userInput = input(input_value)
            if userInput in ['y', 'n']:
                return userInput
            print("y or n! Try again.")

    def inputNumber(self, input_value):
        while True:
            try:
                userInput = float(input(input_value))
            except ValueError:
                print("Not a number! Try again.")
            else:
                return userInput
