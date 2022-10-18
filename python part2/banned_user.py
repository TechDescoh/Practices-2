#set a couple of names into the "ban" list
ban = ["carlos", "desco", "varmilo"]

#ask to the user the username
user = input("What is your user?: ")

#if the username is in the ban list = else, elif = if
if user not in ban:
    print(f"{user.title()} you can chat in the group")
else:
    print(f"{user.title()} you're banned, you can't chat in the group")