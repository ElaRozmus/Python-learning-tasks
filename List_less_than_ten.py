# -*- coding: utf-8 -*-

listOfNumber = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for number in listOfNumber:
    if number < 5:
        print(number)
# %%

listOfNumber = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

secondListOfNumber = []
for number in listOfNumber:
    if number < 5:
        secondListOfNumber.append(number)

print('List of numbers less than 5: \n{}'.format(secondListOfNumber))
# %%
"""
 in one line
"""
listOfNumber = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

comprehensionList = [number for number in listOfNumber if number < 5]
print(comprehensionList)
# %%

userNumber = int(input("Enter number: "))

listOfNumber = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
numberOfListFromUser = []


for number in listOfNumber:
    if number < 5 :
        numberOfListFromUser.append(number)
print(numberOfListFromUser)
