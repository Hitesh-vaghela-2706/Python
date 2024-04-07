# this way we able to create object automatically
class Item:
    def __init__(self,name,price,ram=4):
        self.name = name
        self.price = price
        self.ram = ram

#add value to objects
item1 = Item("Mi Not-7", 8000) 
#calling calss and adding values to it.
# here no need to write ram attribute for individual bcz we set ram
# in our function but in function only last value we will able 
# to set default
item2 = Item("Mi Not-8",10000)
item3 = Item("Mi Not-9",12000,6)

# printing values of object
print("\t",item1.name,"\t",item2.price,"\t",item2.ram,"\t",item3.ram)
# here item2 ram is displayed 4 bcz it is default and we not provided ram but
# item3 ram will be displayed 6 bcz it is given..