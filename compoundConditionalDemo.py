#Gary Li
#9/14/17
#compoundConditionalDemo.py

num= float(input('Enter a number: '))
if num > 0 and num%7 == 0:
    print('Your number positive and divisible by 7')
elif num > 0:
    print('Your number is positive and not divisible by 7 :(')
elif num < 0 and num%7 == 0:
    print('Your number is negative and divisible by 7')
elif num < 0:
    print('Your number is negative and not divisible by 7 :(')
