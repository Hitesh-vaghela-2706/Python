class Item:
    # list1 = []
    def __init__(self,name,ssd,price,ram=4):
        self.name = name
        self.ssd = ssd
        self.price = price
        self.ram = ram # if we not write this so it is not linked with object
        # so in output we not get ram which we select as default
        # Item.list1.append(self)

item1 = Item("hp",216,30000)
item2 = Item("lenovo",512,40000)
# also able to instantiate a extra attribute which we want in any object
item2.has_numpad = False 
item3 = Item("dell",512,35000)
item4 = Item("asus",1024,27000)

#printing object2 to check wheather newly instantiate object is
# present in in object2 or not
print(item2.__dict__)

# for i in Item.list1:
#     print(i.__dict__)
# print(Item.list1)