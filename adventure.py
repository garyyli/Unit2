#Gary Li
#9/15/17
#adventure.py - adventure game

earthquake = input('You wake up to find hour house shaking.  Do you stay in the house? ')
if earthquake == 'yes':
    print("It's an earthquake, idiot. Your house collapses and falls on you, killing you.")
else:
    meteors = input("You run outside and find that your entire city is being bombarded by a meteor shower. Do you run to your neighbor's house to ask what's going on? ")
if meteors == 'no':
    print("It's a meteor shower, idiot. A hot ball of flaming rock slams into you, killing you.")
else:
    neighbor