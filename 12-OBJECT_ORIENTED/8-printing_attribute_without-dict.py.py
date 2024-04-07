class Item:
    list1 = []
    def __init__(self,name,ssd,price):
        self.name = name
        self.ssd = ssd
        self.price = price
        Item.list1.append(self)

item1 = Item("hp",216,30000)
item2 = Item("lenovo",512,40000)
item3 = Item("dell",512,35000)
item4 = Item("asus",1024,27000)

# printing list so it give list of four
# objects which we created and not give
# attributes of that objects
print(Item.list1)

# for printing attributes of list...
j = 1
for i in Item.list1:
    print(f"item{j} --> ","name = ",i.name,"ssd = ",i.ssd,"price = ",i.price)
    j = j + 1
# also we able to print using __dict__ method
# at object level as we seen before
for i in Item.list1:
    print(i.__dict__)
