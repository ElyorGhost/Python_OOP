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
        Parent.__init__(self, fname, lname) # Parent class ni chaqirish
        # Parent class ni chaqirish bilan biz bu class ni
        # Parent class ni o'z ichiga olamiz
        # va bu class ni obyektlarini chaqirish uchun ishlatamiz
        
         
class Student1(Parent):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print(f"Welcome {self.firstname} {self.lastname} to the class of {self.graduationyear}!")
    
# Создание объектов
x = Parent("Elyor", "Fattakhov")
x.printname()

x1 = Children("Diyyor", "Fattakhov")
x1.printname()

x2 = Student1("Doston", "Fattakhov", 2021)
x2.printname()
x2.welcome()