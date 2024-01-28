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