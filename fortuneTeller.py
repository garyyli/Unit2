#Gary Li
#9/13/17
#fortuneTeller.py - gives user a fortune

color = input('Pick red or blue: ')
number = int(input('Pick a number from 1-4: '))

if color=='red' and number==1:
    print ('You will die tomorrow')

elif color=='red' and number == 2:
    print ('You will find one million dollars on the ground')
    
elif color=='red' and number == 3:
    print ('You will die alone')

elif color=='red' and number == 4:
    print ('You will lose your phone')

elif color=='blue' and number == 1:
    print ('You will get sick tomorrow')

elif color=='blue' and number == 2:
    print ('You will fail your next test')
    
elif color=='blue' and number == 3:
    print ('You will break your leg')

elif color=='blue' and number == 4:
    print ('You will get hit by a bus')