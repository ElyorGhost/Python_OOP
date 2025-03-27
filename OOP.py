# kogda funkciya naxoditsya vnutri classa, ona nazyvaetsya method
# class - eto plan, a object - eto realizaciya etogo plana
#from item import Item
from phone import Phone
      
item1 = Phone("jscPhone", 1000, 10, 2)

item1.apply_increment(0.2)

#item1.send_email()
print(item1.price)