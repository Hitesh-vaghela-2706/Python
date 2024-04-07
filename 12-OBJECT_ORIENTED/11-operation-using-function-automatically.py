class Item:
    list1 = []
    discount = 0.84
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.list1.append(self)
    
    def total_price(self):
        return self.price*self.quantity
    
    def discount_price(self):
        return self.price*self.quantity*self.discount
    
    def __repr__(self):
        return f"object('{self.name}')"

item1 = Item("keyboard",300,4)
item2 = Item("mouse",170,8)
item3 = Item("printer",2480,2)
print(Item.list1)

# using loop for performing operation on every
# object like total price,discount etc..
j = 1
final_total_original = 0
final_total_discounted = 0
for i in Item.list1:
    print(f"original price of {i.quantity} {i.name} is -->",i.total_price())
    print(f"discounted price of {i.quantity} {i.name} is -->",i.discount_price())
    final_total_original += i.total_price()
    final_total_discounted += i.discount_price()
    j = j + 1
print("final total original price is :- ",final_total_original)
print("final total discounted price is :- ",final_total_discounted)
