# -*- coding: utf-8 -*-
# try/except
try:
    2 / 0
except:
    print("Nie dzieli sie przez zero")
# %%

try:
    2 / 0
except ZeroDivisionError:
    print("nie dzieli sie przez zero")
except TypeError:
    print("zly typ")
    
    
# %%
# dodawanie int do str
try:
    52 + '4'
except TypeError:
    print('Nie dodaje się tekst do liczby')
    
    
# %%
# Konwersja str w int
try: 
    int('tekst')
except ValueError:
    print('Wprowadzony został tekst, powinna byc liczba')

# %%

while True:
    try:
        x = int(input("podaj liczbe: "))
        break
    except ValueError:
        print("nie wprowadzile poprawnej wartosci")
        
        
# %%
try:
    with open('tekst.txt', 'r') as file:
        for line in file:
            print(line)
except FileNotFoundError:
    print("plik nie istnieje")
    
    
# %%
raise TypeError("Błąd")

# %%
def divide(x, y):
    try:
        x = int(x)
        y = int(y)
        return x/y
    except ZeroDivisionError:
        print("nie dziel przez zero")
    except ValueError:
        print('Musisz wprowadzić liczbe')
divide(3, 0)
divide('1', '2')
divide('1', 'ss')

# %%
result = "You can't divide with 0"
a=5
b=0
try:
    result=a/b
except ZeroDivisionError:
    print(result)

# %%
a = [1, 3, 5]
try:
    a.get()
except:
    pass

print(a)


# %%
msg="You can't add int to string"
a="Hello World!"
try:
    a + 10
except:
    print(msg)
    
    
# %%
#Type your answer below.
msg="You're out of list range"
lst=[5, 10, 20]

try:
    print(lst[5])
except: 
    print(msg)
