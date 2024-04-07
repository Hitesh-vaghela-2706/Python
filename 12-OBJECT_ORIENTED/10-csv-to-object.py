import csv
class Item:
    list1 = []
    def __init__(self,name,ssd,price,ram):
        self.name = name
        self.ssd = ssd
        self.price = price
        self.ram = ram
        Item.list1.append(self)

    def __repr__(self):
        return f"Item('{self.name}','{self.ssd}','{self.price}','{self.ram}')"

    @classmethod
    def csv_read(cls):
        with open('csv-to-object.csv',"r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for i in items:
            Item(
                name = str(i.get('name')),
                ssd = int(i.get('ssd')),
                price = int(i.get('price')),
                ram = int(i.get('ram'))
        )

Item.csv_read()
#accesing particular data in class
for i in Item.list1:
    if(i.ssd >= 217 ):
        print(i)

#accesing all data in class
print(Item.list1) 