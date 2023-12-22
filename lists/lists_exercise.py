my_friends = ["Joseph", "Glenn", "Sally"]
print(my_friends[0])
print(my_friends[1])
print(my_friends[2])


print(f"Hi, {my_friends[0]} how are you doing ?")
print(f"Wozaa, {my_friends[1]} i was wondering if you could help me with something ?")
print(f"Hello, beautiful {my_friends[2]} i have missed you so much.")


music = ["Rnb" ,"AfroBeat" ,"Reggae" ,"Hip-pop" ,"Gospel"] 
print(f"My favorite {music[1]} song is YAWA by Fireboy DML")


dinner_friends = ["Joseph", "Glenn", "Sally"]
print(f"Hi, {dinner_friends[0]} would you like to come over for dinner ?")
print(f"Hi, {dinner_friends[1]} there is a new movie out, would you like to come over and watch it ?")
print(f"Hi beautiful {dinner_friends[2]} i have missed you so much, would you like to come over for dinner ?")

dinner_friends = ["Joseph", "Glenn", "Sally"]
not_coming = dinner_friends.pop(0)
print(f"Unfortunately {not_coming} wont be able to make to dinner.")
dinner_friends.insert(0 ,"Maggy")
print(dinner_friends)
print(f"Hi, {dinner_friends[0]} i would like to invite you to dinner.")
print(f"Hi, {dinner_friends[1]} i would like to invite you to dinner.")
print(f"Hi {dinner_friends[2]} i would like to invite you to dinner.")


print(dinner_friends)
dinner_friends.insert( 0 ,"Juliet")
dinner_friends.insert(2,"Vivian")
dinner_friends.append("Linda")
print(dinner_friends)

print(f"Hi, {dinner_friends[0]} i would like to invite you to dinner.")
print(f"Hi, {dinner_friends[1]} i would like to invite you to dinner.")
print(f"Hi, {dinner_friends[2]} i would like to invite you to dinner.")
print(f"Hi, {dinner_friends[3]} i would like to invite you to dinner.")
print(f"Hi, {dinner_friends[4]} i would like to invite you to dinner.")
print(f"Hi, {dinner_friends[5]} i would like to invite you to dinner.")


print(dinner_friends)
print("You can only invite two people for dinner")
not_inviting = dinner_friends.pop()
print(f"Sorry {not_inviting} i wont be able to invite you ")
not_inviting = dinner_friends.pop()
print(f"Sorry {not_inviting} i wont be able to invite you")
not_inviting = dinner_friends.pop()
print(f"Sorry {not_inviting} i wont be able to invite you")
not_inviting = dinner_friends.pop()
print(f"Sorry {not_inviting} i wont be able to invite you")
print(dinner_friends)
print(f"Hi {dinner_friends[0]} you are still invited to dinner")
print(f"Hi {dinner_friends[1]} you are still invited to dinner")

print(dinner_friends)
del dinner_friends[-2] #deleting the last 2 items in the list
print(dinner_friends)