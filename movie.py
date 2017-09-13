#Gary Li
#9/13/17
#movie.py- tells user the most scandalous type of movie they can watch based on age

age=int(input('Enter your age: '))

if age>=17:
    print('You can watch R movies')
elif age>=13:
    print('You can watch PG-13 movies')
else:
    print('You can watch PG movies (with a parent)')
