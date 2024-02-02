from restaurant import Restaurant


restaurant = Restaurant('kfc', 'fast food')
print(restaurant.number_served)
restaurant.number_served = 10
print(restaurant.number_served)

restaurant.set_number_served(20)
print(restaurant.number_served)

restaurant.increment_number_served(30)
print(restaurant.number_served)