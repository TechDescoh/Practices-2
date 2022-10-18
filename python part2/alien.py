#set a value to the variable
alien_color = 'yellow'

#if the value of the variable match with any of the opcions it print a message
if alien_color == 'green':
    print("you earn 5 coins")
if alien_color.lower() == 'yellow':
    print("you earn 10 coins")

alien_color2 = "Green"
if alien_color2.lower() == "green":
    print("\nyou earn 5 coins")
elif alien_color2.lower() == "red":
    print("you earn 15 coins")
else:
    print("you earn 20 coins")

alien_color3 = "red"
if alien_color3.lower() == "green":
    print("you earn 5 coins")
elif alien_color3.lower() == "red":
    print("you earn 15 coins")
else:
    print("you earn 20 coins")

alien_color4 = "yellow"
if alien_color4.lower() == "green":
    print("you earn 5 coins")
elif alien_color4.lower() == "red":
    print("you earn 15 coins")
else:
    print("you earn 20 coins")