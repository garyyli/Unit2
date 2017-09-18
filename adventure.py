#Gary Li
#9/15/17
#adventure.py - adventure game

earthquake = input('You wake up to find hour house shaking.  Do you stay in the house? ')
if earthquake == 'yes':
    print("It's an earthquake, idiot. Your house collapses and falls on you, killing you.")
else:
    meteors = input("You run outside and find that your entire city is being bombarded by a meteor shower. Do you run to your neighbor's house to ask what's going on? ")
    if meteors == 'no':
        print("It's a meteor shower, idiot. A hot ball of flaming rock slams into you, decimating you.")
    else:
        neighbor = input("You run into your neighbor's house and find that he has turned into a zombie.  You see a knife on the table as he rumble over to you and attack.  Do you grab it? ")
        if neighbor == 'no':
            print("You're truly a special kind of stupid.  The zombie rips your head off your neck and sinks it's rotten teeth into your flesh.  You deserve to die.")
        else:
            knife = input("You grab the knife.  Do you swing low or swing high? Choose one: high or low")
            if knife == 'high':
                print("You try to swing at the zombie's head but he cleverly dodges it before ripping the knife out of your hand as slashing at your midsection.  You are blind with pain and pass out as the zombie begins to devour your cut up midsection.")
            else:
                print("You try to swing low at the zombie's leg but he jumps before grabbing your head and digging his fingerhails into your scalp.  He pulls you down and begins to chomp on your neck as you try to defend yourself, put to no prevail.  GG")