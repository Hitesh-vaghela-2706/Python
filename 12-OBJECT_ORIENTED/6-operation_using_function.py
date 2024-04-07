class Item:
    def __init__(self,price,ram=4):
        self.price = price
        self.ram = ram

    def calculate_price_by_ram(self):
        return self.price/self.ram

item1 = Item(12000)
item2 = Item(24000)

print(item1.calculate_price_by_ram())