#Gary Li
#9/14/17
#insulter.py - generates insults

from random import randint
number = randint(1,5)

name = input('Enter your name: ')

if number == 1:
    print('You lack the presence of friends')

elif number == 2:
    print('You LITERALLY have no friends')

elif number == 3:
    print('You have ZERO friends')

elif number == 4:
    print('You have no companions')

elif number == 5:
    print('You actually have NADA AMIGOS')