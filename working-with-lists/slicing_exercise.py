#Slices
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Isaac', 'Jack']
print(f"The first three students are {students[0:3]}")
print(f"The middle three students are {students[4:7]}")
print(f"The last three students are {students[7:10]}")

#My pizza, your pizza
pizzas = ["Chicken", "Pepperoni", "Hawaiian"]
friend_pizzas = pizzas[:]

pizzas.append("Ostrich")
friend_pizzas.append("Beef")

print(f"My favorite pizzas are: {pizzas}")
print(f"My friend's favorite pizzas are: {friend_pizzas}")


#more loop
pizzas = ["Chicken", "Pepperoni", "Hawaiian"]
for pizza in pizzas[0:3]:
    print(f"First three pizzas are: {pizza}")

students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Isaac', 'Jack']
for student in students[:]:
    print(f"Hello {student} , school opens tomorrow.")
