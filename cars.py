cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print("in~", 'bmw' in cars)
print("not in~", 'bmw' not in cars)