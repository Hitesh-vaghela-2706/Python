class Item:
    def __init__(self,name,ssd,price): 
        self.name = name
        self.ssd = ssd
        self.price = price
        # valdation using assert to ansure the data is 
        # correct which we entering
        assert ssd <= 1024,f"ssd value must be less than 1024"
        assert price <= 25000,f"price value must be less than 25000"

item1 = Item("lenovo", 2065, 24000)
print(item1.ssd)
# it raise error bcz ssd value is grater than 1024
print(item1.__dict__)

item2 = Item("dell", 556, 27000)
print(item2.ssd)
 # it raise error bcz ssd value is grater than 25000
print(item2.__dict__)