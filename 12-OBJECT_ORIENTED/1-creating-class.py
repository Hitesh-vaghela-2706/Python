# What is class in programming with example?
# A class is a way of organizing information about a different type of data so a programmer can reuse elements 
# when making multiple instances of that data type—for example, if a programmer wanted to make three 
# instances of Car , maybe a BMW, a Ferrari, and a Ford instance.

# In object-oriented programming, a class is a template definition of the methods and variables in a 
# particular kind of object. Thus, an object is a specific instance of a class; it contains real values
# instead of variables. The class is one of the defining ideas of object-oriented programming.


# in python we use class keyword for creating a class.

class Item:
    pass

# create instances/objects of class manually
item1 = Item()
item1.name = "android phone" # adding attributes to the instance
item1.price = 12000
item1.ram = 6

item2 = Item()
item2.name = "iphone"
item2.price = 80000
item2.ram = 4
# printing class object as dictionary
print(Item.__dict__)
# but dict is mainly used for print all attributes at
# instance level or object level
print(item1.__dict__)
print(item2.__dict__)
# printing value of object
print(item2.name)