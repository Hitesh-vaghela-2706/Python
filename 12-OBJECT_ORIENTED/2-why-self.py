class Item:
    def __init__(self):
        print("self is called")
        print(self.__dict__)
# when we use self it check for all object created 
# and take one by one all object as input for created function
item1 = Item()
item1.name = 'Purvi'
item1.age = 22
item2 = Item() # these are empty objects created
item2.name = 'Reshma'
item2.age = 21
item3 = Item() 
item3.name = 'Hitesh'
item3.age = 23
# here i created a 3 objects so three times function runs
# therefor three time prints self is called

# if we add data in object then also it work same
