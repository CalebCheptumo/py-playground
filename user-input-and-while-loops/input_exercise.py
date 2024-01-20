# Rental car
car = input("What type of car would you like to rent? ")
print(f"Let me see if i can find you a {car}")


# Restaurant seating
seats = input("How many people are in their dinner group? ")
seats = int(seats)

if seats > 8:
    print("You will have to wait for a table")
else:
    print("Your table is ready")
