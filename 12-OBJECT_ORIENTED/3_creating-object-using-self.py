# this way we able to create object automatically
class Item:
    def __init__(self,name,price,ram):
        self.name = name
        self.price = price
        self.ram = ram

#add value to objects
item1 = Item("Mi Not-7", 8000, 3) #calling class and adding values to it.
item2 = Item("Mi Not-8",10000,4)
item3 = Item("Mi Not-9",12000,6)

# printing values of object
print("\t",item1.name,"\t",item2.price,"\t",item3.ram)
print(vars(item2))