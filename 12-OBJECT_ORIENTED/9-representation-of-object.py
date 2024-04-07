# __repr__ is used for represent the objects 

class Item:
    all_list = []
    def __init__(self,name,ssd,price,ram=4):
        self.name = name
        self.ram = ram
        self.ssd = ssd
        self.price = price
        #appendind instances in list
        Item.all_list.append(self)
    
    def __repr__(self):
        return f"object('{self.name}')"
        # return f"Item('{self.name}','{self.ram}','{self.price}','{self.ssd}')"
        # if we use this as a repr than we get whole data as a name of object

item1 = Item("hp",216,30000)
item2 = Item("lenovo",512,40000)
item3 = Item("dell",512,35000)
item4 = Item("asus",1024,27000)

#printing instances 
print(Item.all_list) #return all object list but it is complicate to understand
# so overcome this we used a repr magic method so we able to print attribute of class
# as we want

for i in Item.all_list:
    print(i) # printing all objects in class