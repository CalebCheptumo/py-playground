#Pizza Toppings
prompt  = "What topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(f"You'll add {message} topping to your pizza!")


# Movie Tickets
prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    age = input(prompt)
    
    if age == 'quit':
        break

    age = int(age)
    if age < 3:
        print("Your ticket is free")
    elif age <= 12:
        print("Your ticket is $10")
    else:
        print("Your ticket is $15")


# Three Exits
prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished: "

active = True
while active:
    age = input(prompt)
    
    if age == 'quit':
        active = False
        break

    age = int(age)
    if age < 3:
        print("Your ticket is free")
    elif age <= 12:
        print("Your ticket is $10")
    else:
        print("Your ticket is $15")



#infinity loop

number = 0
while number < 5:
    print(number)



#deli
sandwich_orders = ['tuna', 'chicken', 'veggie', 'beef', 'turkey']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich)



#no pastrami
sandwich_orders = ['tuna', 'chicken', 'pastrami', 'beef', 'turkey', 'pastrami', 'veggie', 'pastrami']
finished_sandwiches = []

print("The deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich)



#dream vacation
poll_results = {}

while True:
    name = input("What's your name? ")
    place = input("If you could visit one place in the world, where would you go? ")

    poll_results[name] = place

    repeat = input("Would you like another person to vote? (yes/ no) ")
    if repeat.lower() != 'yes':
        break

print("\n--- Poll Results ---")
for name, place in poll_results.items():
    print(f"{name.title()} would like to visit {place.title()}.")


