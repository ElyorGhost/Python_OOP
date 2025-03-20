# Create a Parent Class 

# Родительский класс — это класс, 
# от которого наследуется, также называемый базовым классом.

# Любой класс может быть родительским классом, поэтому 
# синтаксис такой же, как и при создании любого другого класса:


class Parent:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)

# Создайте класс, который наследует класс Parent

class Children(Parent):
    def __init__(self, fname, lname):
        pass 
        

x = Parent("Elyor", "Fattakhov")
x.printname()

x1 = Children("Diyyor", "Fattakhov")

x1.printname()