# -*- coding: utf-8 -*-

"""
Separate even numbers from odd numbers
* with the help of a loop
** using list comprehension
*** Create a function


"""
listNumber = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 50, 58, 5, 45, 11, 47 ]
listEvenNumber = []
listOddNumber = []
for number in listNumber:
    if number % 2 == 0:
        listEvenNumber.append(number)
    elif number % 2 != 0:
        listOddNumber.append(number)
print('Only even number from basic list: \n{}'.format(listEvenNumber))

print('Only odd number from basic list: \n{}'.format(listOddNumber))
# %%
listNumber = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 50, 58, 5, 45, 11, 47 ]
listComprehension = [number for number in listNumber if number % 2 == 0]

print("Only even elements in the list: \n{}".format(listComprehension))
# %%
listNumber = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 50, 58, 5, 45, 11, 47 ]

def evenOrOdd(numbers):
    listEvenNumber = []
    listOddNumber = []
    for number in listNumber:
        if number % 2 == 0:
            listEvenNumber.append(number)
        elif number % 2 != 0:
            listOddNumber.append(number)
    print('Only even number from basic list: \n{}'.format(listEvenNumber))
    
    print('Only odd number from basic list: \n{}'.format(listOddNumber))

rraz = evenOrOdd(listNumber)
