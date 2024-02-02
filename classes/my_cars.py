from car import Car # import the Car class from the car module . imported car form its module Car
from electric_car import ElectricCar # import the ElectricCar class directly from the electric_car module. imported ElectricCar from its module ElectricCar


my_tesla = ElectricCar('tesla','model s',2019)
print(my_tesla.get_descriptive_name())

my_toyota = Car('toyota','corolla',2019)
print(my_toyota.get_descriptive_name())