#Pizza Toppings
prompt  = "What topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(f"You'll add {message} topping to your pizza!")