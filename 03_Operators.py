#Arithmetic Operators
x =10
y = 6

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def modulo(x, y):
    return x % y #qoldiqni chiqaradi

def exponentiation(x,y):
    return x**y # x ni y darajaga ko'taradi

def floor_division(x, y):# Результат: 1 (потому что 10 / 6 = 1.666, дробная часть отбрасывается)
    return x//y ## выполняет целочисленное деление (или деление с округлением вниз).
                ## Он делит одно число на другое и возвращает целую часть результата, 
                ## отбрасывая дробную часть.



print(modulo(x,y))