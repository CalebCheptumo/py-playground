from car import Car #  import the Car class from the car module tells python to open the car.py file and copy all the classes from it into this program.

my_new_car=Car('audi','a4',2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading=23
my_new_car.read_odometer()