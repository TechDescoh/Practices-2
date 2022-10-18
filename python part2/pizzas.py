my_pizzas = ["Peperoni", "Cheese", "Extra Cheese"]
friends_pizza = my_pizzas[0:3]

my_pizzas.append("Hawaiana")
friends_pizza.append("vegetarian")

for pizzas in my_pizzas:
    print(f"My favorite pizzas are {pizzas}\n")

for friend_pizzas in friends_pizza:
    print(f"My friend's favorite pizzas are {friend_pizzas}\n\n\n")



my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

for food in my_foods:
    print(f"{food}")
for friend_food in friend_foods:
    print(f"{friend_food}")


