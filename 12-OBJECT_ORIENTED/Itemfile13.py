class Item:
    discount = 0.85
    all_list = []
    def __init__(self,name,ssd,price,ram=4):
        self.__name = name
        self.ram = ram
        self.ssd = ssd
        self.price = price
        #appendind instances in list
        Item.all_list.append(self)
    def calc(self):
        return self.price*self.ram
    def apply_disc(self):
        return self.price*self.discount
    def __repr__(self):
        return f"hitesh{self.__class__.__name__}('{self.name}','{self.ram}','{self.price}','{self.ssd}')"
        # code for restrict change attribute
    @property
    def name(self):
        return self.__name
        #code for allow change in attributes
    @name.setter
    def name(self,value):
        print("want to overwrite name?")
        self.__name = value

item1 = Item("hp",216,30000)
item2 = Item("lenovo",512,40000)
item3 = Item("dell",512,35000)
item4 = Item("asus",1024,27000)
print(Item.all_list)
