# -*- coding: utf-8 -*-
# random lists and exercises with them with using a loop and list comprehension
import random


listRandomOne = random.sample(range(40), 14)
print("First list with random numbers: \n{}".format(listRandomOne))

listRandomTwo = random.sample(range(40),15)
print("Second list with random numbers: \n{}".format(listRandomTwo))
print("\n")

# common number with using a loop 
commonList = []
for item in listRandomOne:
    if item in listRandomTwo:
        commonList.append(item)
print("Common numbers from these two lists: \n{}".format(commonList))

# Differents numbers with using a loop
differentList = []
for item in listRandomOne:
    if item not in listRandomTwo:
        differentList.append(item)
print("Differents numbers form these two lists: \n{}".format(differentList))
        
        