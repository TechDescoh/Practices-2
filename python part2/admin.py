#set values for the variable 
usernames = []
#Here we call the list, we make sure that the list is not empty
if usernames:
#if "admin" is in the variable the program will display a special message
    for username in usernames:
        if username == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}")
#If the list is empty we display this message
else: 
    print("We need to find some users")


#set values for the variable 
usernames2 = ["maria", "carlos", "fernando", "cristian", "admin", "varmilo"]
#Here we call the list, we make sure that the list is not empty
if usernames2:
#if "admin" is in the variable the program will display a special message
    for username2 in usernames2:
        if username2 == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username2}")
#If the list is empty we display this message
else: 
    print("We need to find some users")