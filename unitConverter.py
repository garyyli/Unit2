#Gary Li
#9/13/17
#unitConverter.py - converts units inputed by user

print('1) Kilometers to Miles')
print('2) Kilograms to Pounds')
print('3) Liters to Gallons')
print('4) Celsius to Fahrenheit')

number = float(input('Choose a number: '))

for i in range (1,5):
    if number==1:
        kilometers = float(input('Enter number of kilometers: '))
        print(kilometers, 'is', kilometers*0.621371, 'miles')

    if number==2:
        kilograms = float(input('Enter number of kilograms: '))
        print(kilograms, 'is', kilograms*2.20462, 'pounds')

    if number==3:
        liters = float(input('Enter number of liters: '))
        print(liters, 'is', liters*0.264172, 'gallons')

    if number==4:
        celsius = float(input('Enter Degrees in Celsius: '))
        print(celsius, 'is', (celsius*1.8)+32, 'degrees in Fahrenheit')