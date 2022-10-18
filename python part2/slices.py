#Using slice we call the first three items of the list
names = ["martina", "alex", "marta", "fernando", "andrew"]
for name in names:
    name = names[:3]
print(f"The first three items in the list are {name}")

#Using slice we call the middle items of the list
for name in names: 
    name = names[1:4]
print(f"Three items from the middle of the list are {name}")

#Using slice we call the last three items of the list
for name in names:
    name = names[2:5]
print(f"Last three items in the list are {name}")