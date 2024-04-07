# parent class 
class Item:
    list1 = []
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.list1.append(self)
    
    def total_price(self):
        return self.price*self.quantity
    
    def __repr__(self):
        return f"object('{self.name}')"

item1 = Item("keyboard",300,4)
item2 = Item("mouse",170,8)
item3 = Item("printer",2480,2)
print(Item.list1)

#child class
class Phone(Item):
    list2 = []
    def __init__(self,name,price,quantity,ram):
        # self.name = name
        # self.price = price
        # self.quantity = quantity
    # instead  writing these three lines we will use 
    # super keyword and inherit it from parent class
        super().__init__(name,price,quantity)
        self.ram = ram
        Phone.list2.append(self)

    # def __repr__(self):
    #     return f"object('{self.name}')" 
    # we no need to write representation in child 
    # class if we wrote in parent class
phone1 = Phone("redmi",16000,4,6)
phone2 = Phone("samsung",5000,8,4)
print(Phone.list2)
# this way we able to use parent class functions
# in child class
for i in Phone.list2:
    print(f"total price of {i.quantity} {i.name} phone is :-", i.total_price())