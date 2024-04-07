from Itemfile13 import Item

class Phone(Item):
    all_list = []
    def __init__(self,name,ram,price,broken):
        super().__init__(name,ram,price)
        self.broken = broken
        Phone.all_list.append(self)

phone1 = Phone("redmi", 6 ,16000,4)
phone2 = Phone("samsung", 4 ,5000,8)
print(phone2.calc())
print(phone1.apply_disc())
print(Phone.all_list)