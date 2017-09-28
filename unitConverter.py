#Gary Li
#9/13/17
#unitConverter.py - converts units inputed by user

print('1) Kilometers to Miles')
print('2) Kilograms to Pounds')
print('3) Liters to Gallons')
print('4) Celsius to Fahrenheit')
print('5) Quit out of program')

while True:
    number = float(input('Choose a number: '))
    if number==1:
        kilometers = float(input('Enter number of kilometers: '))
        print(kilometers, 'is', kilometers*0.621371, 'miles')

    elif number==2:
        kilograms = float(input('Enter number of kilograms: '))
        print(kilograms, 'is', kilograms*2.20462, 'pounds')

    elif number==3:
        liters = float(input('Enter number of liters: '))
        print(liters, 'is', liters*0.264172, 'gallons')

    elif number==4:
        celsius = float(input('Enter Degrees in Celsius: '))
        print(celsius, 'is', (celsius*1.8)+32, 'degrees in Fahrenheit')
    elif number == 5:
        break