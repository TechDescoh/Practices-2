#a loop to add 1000000 numbers to a list,  we call the min number, the max number and the sum of all those numbers
numbers = []
for value in range(1, 1000001, 20):
    numbers.append(value)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#a list of the multiples of 3 from 3 to 30. 
odd_numbers = []
for value in range(3, 31, 3):
    odd_numbers.append(value*3)
print(odd_numbers)

#a list comprehension to generate a list of the first 10 cubes.
cubes = [value**3 for value in range(1, 11)]
print(cubes)