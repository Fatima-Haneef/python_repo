#revese a list
my_list = [1, 2, 3, 4, 5]
reversed_list = []

for i in range(len(my_list) - 1, -1, -1):
    reversed_list.append(my_list[i])

print("Reversed list:", reversed_list)

#turn every item of a list into its square
my_list = [1, 2, 3, 4, 5]
squared_list = []

for num in my_list:
    squared_list.append(num * num)

print("Squared list:", squared_list)

#remove empty strings from a list of strings
my_list = ["hello", "", "world", "", "python", " "]
filtered_list = []

for item in my_list:
    if item != "":  
        filtered_list.append(item)

print("List without empty strings:", filtered_list)

# add new item to the list after a specific item
my_list = [1, 2, 3, 4, 5]
new_item = 10
specific_item = 3
new_list = []

for item in my_list:
    new_list.append(item)
    if item == specific_item:
        new_list.append(new_item)

print("Updated list:", new_list)

#replace list's item with new value if found 
my_list = [1, 2, 3, 4, 5]
old_value = 3
new_value = 10
updated_list = []

for item in my_list:
    if item == old_value:
        updated_list.append(new_value)
    else:
        updated_list.append(item)

print("Updated list:", updated_list)
