from car import Car , ElectricCar #  import the Car class from the car module tells python to open the car.py file and copy all the classes from it into this program.
import car # import the car module and then access the classes we need by using dot notation.
my_new_car=Car('audi','a4',2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading=23
my_new_car.read_odometer()



my_tesla = ElectricCar('tesla','model s',2019)
print(my_tesla.get_descriptive_name())

my_toyota=Car('toyota','corolla',2019)
print(my_toyota.get_descriptive_name())


my_tesla = car.ElectricCar('tesla','model s',2019)
print(my_tesla.get_descriptive_name())

my_toyota = car.Car('toyota','corolla',2019)
print(my_toyota.get_descriptive_name())
