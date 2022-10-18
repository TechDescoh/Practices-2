#set a value for the variable
favorite_fruits = ["apple", "orange", "banana"]

#Write five if statements. Each should check whether a certain kind of fruit is in your list.
if "banana" in favorite_fruits:
    print("You really like bananas")
if "pear" in favorite_fruits:
    print("You really like pears")
if "apple" in favorite_fruits:
    print("You really like apples")
if "orange" in favorite_fruits:
    print("You really like oranges")
if "mandarin" in favorite_fruits:
    print("You really like mandarines")

#other way to do this is doing a for loop calling the values from the variable, like this:
for favorite_fruit in favorite_fruits:
    print(f"\nYou really like {favorite_fruit}")
