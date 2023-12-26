#Slicing accessing parts of lists.
#syntax: list_name(start:stop)
#start is inclusive, stop is exclusive
#start defaults to 0, stop defaults to end of list

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September']
print(months[0:3])


#you can also include step
#syntax: list_name(start:stop:step)

print(months[0:4:2]) #will slice form index 0 to 4 with a step of 2

#looping through a slice
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September']
for month in months[:3]: #looping through the first 3 months
    print(month)


#copying a list
#syntax: list_name[:]
#this will create a new list with the same values as the original list
#this is useful when you want to make a copy of a list and modify the copy
    
towns = ['Nairobi', 'Mombasa', 'Kisumu', 'Nakuru', 'Eldoret', 'Thika', 'Kitale', 'Malindi', 'Garissa', 'Kakamega']
towns_copy = towns[:]
print(f"Original list: {towns}")
print(f"Copy of the list : {towns_copy}")


#prove that we actually have two different lists
towns.append("Notatown")
towns_copy.append("Notatown_copy")
print(f"Original list: {towns}")
print(f"Copy of the list : {towns_copy}")


#negative indexing
#syntax: list_name[-index] 
#negative indexing starts from the end of the list
#-1 is the last element, -2 is the second last element and so on

towns = ['Nairobi', 'Mombasa', 'Kisumu', 'Nakuru', 'Eldoret', 'Thika', 'Kitale', 'Malindi', 'Garissa', 'Kakamega']
print(towns[-1:]) #prints the last element
print(towns[-2:]) #prints the second last element
print(towns[-3:]) #prints the third last element

#using is to check if two lists are the same
cars = ['Toyota', 'Nissan', 'Subaru', 'Mitsubishi', 'Honda', 'Mazda', 'Suzuki', 'Isuzu', 'Volkswagen', 'Ford']
favorite_cars = cars[:]
print(cars is favorite_cars) #returns false because they are two different lists
print(cars == favorite_cars) #returns true because they have the same values

#slicing assignment
#syntax: list_name[start:stop] = [new_values]
#modify part of a list

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September']
months[1:3] = ['New February', 'New March']
print(months)