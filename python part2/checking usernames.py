#set the list of current users (usernames taken)
current_users = ["varmilo", "glevion", "mariana", "desco", "juan carlos", "cristian", "mateo"]
#set a list of new usernames
new_users = ["glevion", "varmilo", "marcos", "arcos", "felipe"]

#create a empty list
current_users_lower = []

#copy the values from current_users and use .lower to add the names to the empty list in lowercase
for user in current_users:
    current_users_lower.append(user.lower)

#create a value for the loop calling the new_users list
for new_user in new_users:
    #if a value from the new_user list is in the current_users list print this message
    if new_user.lower() in current_users:
        print(f"sorry {new_user} is already taken")
    #if a value from the New_user list isn't in the current_users list print this message
    else:
        print(f"{new_user} still available")