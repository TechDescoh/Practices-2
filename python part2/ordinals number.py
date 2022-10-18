#set a list of numbers to the variable
ordinals_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#create a value for each value that is in variable
for ordinal_number in ordinals_numbers:
    #if in the variable there's the number 1, print 1 + st next to it
    if ordinal_number == 1:
        print(f"{ordinal_number}st")
    #if in the variable there's the number 2, print 2 + nd next to it
    elif ordinal_number == 2:
        print(f"{ordinal_number}nd")
    #if in the variable there's the number 3, print 3 + rd next to it
    elif ordinal_number == 3:
        print(f"{ordinal_number}rd")
    #convert the values from the temporarily variable to a string and add "th" to the rest of the nuumbers in the list
    else:
        print(str(ordinal_number) + "th")