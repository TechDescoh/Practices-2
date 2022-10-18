# Here we ask for a value and after that we display a message
name = input("What is your name? ")
name = name.strip()
name = name.title()
request = print(f"There's a party tonight {name}!")

# While we can continue we ask if the person want to go the party. Put y if you want to go, n if you don't want to 
while True:
    ask = input("Do you want to go to the party? (y/n) ")
    
    #list of people that is invited to the party
    list = ["Juan", "Carlos", "Juanita"]

    #If you put y the program is going to display a message
    if ask.lower() == "y":
        print(
            f"Thank you so much {name}!!, this is the list now:\n")
        list.insert(0, name)
        print(list)
        break
    #If you put n the program is going to display a message
    elif ask.lower() == "n":
        print("It's ok, see you later!!")
        break
    #If you don't choose between y/n and you put an invalid option the program is going to display a message
    else:
        print("choose an option!!")
        continue
 