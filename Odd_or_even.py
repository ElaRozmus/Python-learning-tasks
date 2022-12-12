# -*- coding: utf-8 -*-


number = int(input("Give one number: "))

if number % 2 == 0:
    print('{} - This number is even '.format(number))
else:
    print('{} - this number is odd '.format(number))

# %%
# If the number is a multiple of 4, print out a different message.

number = int(input("Give one number: "))


if number % 2 == 0 and number % 4 == 0 and number >= 4:
    print('{} - This number is even '.format(number))
    print('{} is a multiple of 4'.format(number))
else:
    print('{} - this number is odd '.format(number))

# %%
number = int(input("Give one number: "))


if number % 2 == 0:
    print('{} - This number is even '.format(number))    
    if number % 4 == 0 and number >= 4:
        print('{} is a multiple of 4'.format(number))
else:
    print('{} - this number is odd '.format(number))
    
    
# %%

num = int(input("Give number: "))
check = int(input("Give another number: "))

if num % check == 0:
    print('{} check divides evenly into num {}'.format(check, num))
elif num % check !=0:
    print("{} check does not divide evenly on num {}".format(check, num))
# %%
number = int(input("Enter a number: "))

if number % 4 == 0:
    print("Ooh fancy, your number is divisible by four!")
elif number % 2 == 0:
    print("Awesome, " + str(number) + " is an even number.")
else:
    print("Well that's odd, " + str(number) + " is an odd number.")
# %%
number = int(input("Give one number: "))

if number % 4 == 0:
    print('{} is a multiple of 4'.format(number))
elif number % 2 == 0:
    print('{} - This number is even '.format(number))
else:
    print('{} - this number is odd '.format(number))    
    