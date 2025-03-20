def Slicing_Strings():    
    a = 'Hello World'
    print(a[2:]) # llo World
    print(a[:-1]) # Hello Worl
    print(a[:3]) # Hel
    print(a[1:5]) # ello 

def Modify_Strings():
    a = 'Hello World'
    print(a.upper()) # HELLO WORLD upper case
    print(a.lower()) # hello world lower case
    print(a.replace('H', 'J')) # Jello World harfflarni almashtiradi
    print(a.split(' ')) # ['Hello', 'World'] разбивает строку на подстроки, если находит экземпляры разделителя:

def String_Concatenation(): #Объединить переменную aс переменной bв переменную c:
    a = 'Hello'
    b = 'World'
    print(a + b) # HelloWorld
    print(a + ' ' + b) # Hello World

def Format_String():
    age = 36
    txt = "My name is John, and I am {}"
    tx = "My name is John, and I am" + age
    print(txt.format(age)) # My name is John, and I am 36

    #F-strings
    txt = f"My name is John, and I am {age}"
    print(txt) # My name is John, and I am 36

    #placeholders and Modifiers
    price = 49
    txt = "The price is {:.2f} dollars"
    print(txt.format(price)) # The price is 49.00 dollars

def Escape_Character():
    txt = "We are the so-called \"Vikings\" from the north."
    print(txt) # We are the so-called "Vikings" from the north.

def String_Methods():
    a = 'hello World'
    print(a.capitalize()) # Hello world 
    print(a.casefold()) # hello world
    print(a.center(20)) #    Hello World
    print(a.count('l')) # 3
    print(a.encode()) # b'Hello World'
    print(a.endswith('d')) # True
    print(a.expandtabs(2)) # Hello World
    print(a.find('o')) # 4
    print(a.index('o')) # 4
    print(a.isalnum()) # False
    print(a.isalpha()) # False
    print(a.isdecimal()) # False
    print(a.isdigit()) # False
    print(a.isidentifier()) # False
    print(a.islower()) # False
    print(a.isnumeric()) # False
    print(a.isprintable()) # True
    print(a.isspace()) # False
    print(a.istitle()) # True
    print(a.isupper()) # False
    print(a.join('123')) # 1Hello World2Hello World3
    print(a.ljust(20)) # Hello World
    print(a.lower()) # hello world
    print(a.lstrip()) # Hello World
    print(a.partition(' ')) # ('Hello', ' ', 'World')
    print(a.replace('H', 'J')) # Jello World
    print(a.rfind('o')) # 7
    print(a.rindex('o')) # 7
    print(a.rjust(20)) #          Hello World
    print(a.rpartition(' ')) # ('Hello', ' ', 'World')
    print(a.rsplit()) # ['Hello', 'World']
    print(a.rstrip()) # Hello World
    print(a.split()) # ['Hello', 'World']
    print(a.splitlines()) # ['Hello World']
    print(a.startswith('H')) # True
    print(a.strip()) # Hello World
    print(a.swapcase()) # hELLO wORLD
    print(a.title()) # Hello World
    print(a.upper()) # HELLO WORLD
    print(a.zfill(20)) # 000000000Hello World


String_Methods()