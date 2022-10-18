#With each value in the list we display a simple message for each one
friends = ["Carlos", "Marcos", "Juan"]
for friend in friends:
    print(f"This was a good night, {friend}")
print("\nHope to see you next time guys!!\n\n")

#With each value in the list we display a simple message for each one
pizzas = ["Peperoni", "Cheese", "Extra Cheese"]
for pizza in pizzas: 
    print(f"I love {pizza} Pizza")
print("\nI really love pizza!!\n\n")

#With each value in the list we display a simple message for each one
animals = ["cat", "puma", "tigger"]
for animal in animals: 
    print(f"a {animal} would be a good pet")
print("\nAny of these animals would make a great pet!\n\n")

#a for loop to raise to the second power numbers in range 1-10
#squares = []
#for value in range(1, 11):
#    square = value ** 2
#    squares.append(square)
#print(squares)

#a list comprehension to raise to the second power numbers in range 1-10
squares = [value**2 for value in range(1,11)]
print(squares)

#a foor loop to raise to the second power numbers in range 1-10
#squares = []
#for value in range(1, 11):
#   squares.appendd(value**2)