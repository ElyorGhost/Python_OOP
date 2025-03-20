# class bu obyektni konstruktori va metodlari bilan birga yaratish uchun ishlatiladi


class MyClass:
    x = 5
     

p1 = MyClass()      #bu oddiy klass odatiy dasturlarda ishlatilmaydi
print(p1.x)  # 5

class Person:
    def __init__(self, name, age): # __init__ bilan biz boshlang'ich qiymatlarni o'zimiz tanlaymiz
                                   #__init__ bu ishga tushirish funksiyasi
                                   #__init__ obyektni boshlash uchun 
                                   # ishlatiladigan dastlabki sozlamalarni bajaradi
                                   # __init__()вызывается автоматически каждый раз, 
                                   # когда класс используется для создания нового объекта.
        self.name = name
        self.age = age
    
    def __str__(self): #bu metod obyektni string ko'rinishida chiqaradi
        return f"Name: {self.name}, Age: {self.age}" 
        

p1 = Person("John", 36)

print(p1.name) #John
print(p1.age)  #36
print(p1) #Name: John, Age: 36

class Student:
    def __init__(self, name, age): # Self является ссылкой на текущий экземпляр класса 
                                   # и используется для доступа к переменным, принадлежащим классу.
        self.name = name           # self ni hoxlagan nom bilan o'zlashtirish mumkin
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)
    
    def __str__(self):
        return f"Hello my name is {self.name}, I'm {self.age}years old."

p2 = Student("Elyor", 27)
print(p2)

p2.age = 28 # obyektni qiymatini o'zgartirish
print(p2) #Hello my name is Elyor, I'm 28years old.

del p1.age # obyektni qiymatini o'chirish

del p1 # obyektni o'chirish