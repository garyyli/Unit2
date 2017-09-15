#Gary Li
#9/15/17
#warmUp3.py - number divisible by 2,3, neither, or both

number = int(input('Enter a number: '))

if number%3 == 0 and number%2 == 0:
    print(number, 'is divisible by both')
elif number%3 == 0:
    print(number, 'is divisible by 3')
elif number%2 == 0:
    print(number, 'is divisible by 2')
else:
    print(number, 'is divisible by neither')
