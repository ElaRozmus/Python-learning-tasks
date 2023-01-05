# -*- coding: utf-8 -*-

#  a function that takes two arguments, name and age, and print their #value.Modified to bmi calculator
from enum import IntEnum


gender = input("""choose m for a man
w for a woman
Place for your decision:  """).lower()

weighT = int(input("Please enter your weight: "))
heighT = int(input("Please enter you height: "))
agE = int(input("Please enter you age: "))

choose = input("""please choose yuor activity: 
1 = sedentary lifestyle (you do not show any physical activity)
2 = very little activity (office job, no exercise, some walking)
3 = little activity (no exercise, your work need some light physical effort)
4 = middle activity (regular training)
5 = hight activity (everyday training, you have phisical job or activity lifestyle)
6 = Very high activity (training twice a day, very highly physical job)
Place for you decision: """)

def bmi_calculator(weight, height):
    return  round(weight / (height / 100)**2)
 

def men_bmr_calculator(age, weight, height):
    return round(66 + (13.7 * weight) + (5 * height) - (6.8 * age))

def women_bmr_calculator(age, weight, height):
    return round(655 + (9.6 * weight) + (1.7 * height) - (4.7 * age))
    
    
bmi = bmi_calculator(weighT, heighT)
print(f'Your BMI is: {bmi}')
 
if bmi <= 16.0 and bmi <= 18.49:
    print("You have underweight")
elif bmi >= 18.5 and bmi <= 24.99:
    print("Your weight is allright")
elif bmi >= 25.0 and bmi <= 29.99:
    print("You have obesity")
elif bmi >= 30.0:
    print("you have obesity")

chooseEnum = IntEnum("chooseEnum","sedentary very little middle hight Very")
   
if choose == chooseEnum.sedentary and gender == "m":
    men = men_bmr_calculator(agE,weighT,heighT)
    print(f'your caloric needs is: {men} kcal')
    cpm = men * 1.0
    print(f'Your CPM is: {cpm}')
elif choose == chooseEnum.very and gender == "m":
    men = men_bmr_calculator(agE,weighT,heighT)
    print(f'your caloric needs is: {men} kcal')
    cpm = men * 1.2
    print(f'Your CPM is: {cpm}')
elif choose == chooseEnum.little and gender == "m":
    men = men_bmr_calculator(agE,weighT,heighT)
    print(f'your caloric needs is: {men} kcal')
    cpm = men * 1.4
    print(f'Your CPM is: {cpm}')
elif choose == chooseEnum.middle  and gender == "m":
    men = men_bmr_calculator(agE,weighT,heighT)
    print(f'your caloric needs is: {men} kcal')
    cpm = men * 1.6
    print(f'Your CPM is: {cpm}')
elif choose == chooseEnum.hight and gender == "m":
    men = men_bmr_calculator(agE,weighT,heighT)
    print(f'your caloric needs is: {men} kcal')
    cpm = men * 1.8
    print(f'Your CPM is: {cpm}')
elif choose == chooseEnum.Very and gender == "m":
    men = men_bmr_calculator(agE,weighT,heighT)
    print(f'your caloric needs is: {men} kcal')
    cpm = men * 2.0
    print(f'Your CPM is: {cpm}')

if choose == chooseEnum.sedentary and gender == "w":
    women = women_bmr_calculator(agE,weighT,heighT)
    print(f'your caloric needs is: {women} kcal')
    cpm = women * 1.0
    print(f'Your CPM is: {cpm}')
elif choose == chooseEnum.very and gender == "w":
    women = women_bmr_calculator(agE,weighT,heighT)
    print(f'your caloric needs is: {women} kcal')
    cpm = men * 1.2
    print(f'Your CPM is: {cpm}')
elif choose == chooseEnum.little and gender == "w":
    women = women_bmr_calculator(agE,weighT,heighT)
    print(f'your caloric needs is: {women} kcal')
    cpm = men * 1.4
    print(f'Your CPM is: {cpm}')
elif choose == chooseEnum.middle and gender == "w":
    women = women_bmr_calculator(agE,weighT,heighT)
    print(f'your caloric needs is: {women} kcal')
    cpm = men * 1.6
    print(f'Your CPM is: {cpm}')
elif choose == chooseEnum.hight and gender == "w":
    women = women_bmr_calculator(agE,weighT,heighT)
    print(f'your caloric needs is: {women} kcal')
    cpm = men * 1.8
    print(f'Your CPM is: {cpm}')
elif choose == chooseEnum.Very and gender == "w":
    women = women_bmr_calculator(agE,weighT,heighT)
    print(f'your caloric needs is: {women} kcal')
    cpm = men * 2.0
    print(f'Your CPM is: {cpm}')
else:
    print("Please write only m or w, nothing else :)")
