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



