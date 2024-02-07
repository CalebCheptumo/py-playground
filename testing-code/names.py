from name_function import get_formatted_name # import the function get_formatted_name() from the module name_function

print("Enter 'q' at any time to quit.") # prompt the user to enter 'q' to quit
while True:
    first = input("\nPlease give me a first name: ") # prompt the user to enter a first name
    if first == 'q': # if the user enters 'q', break the loop
        break
    last = input("Please give me a last name: ") # prompt the user to enter a last name
    if last == 'q': # if the user enters 'q', break the loop
        break

    formatted_name = get_formatted_name(first, last) # call the function get_formatted_name() with the arguments first and last
    print(f"\tNeatly formatted name: {formatted_name}.") # print the formatted name