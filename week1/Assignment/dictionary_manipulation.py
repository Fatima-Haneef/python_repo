#check if a value exists in the dictionary
my_dict = {"a": 10, "b": 20, "c": 30}
search_value = 20
found = False

for key in my_dict:
    if my_dict[key] == search_value:
        found = True
        break

if found:
    print("Value exists in the dictionary")
else:
    print("Value does not exist in the dictionary")
    
    #get the key of a minimum value in  the following  dictionary
my_dict = {"a": 10, "b": 5, "c": 30, "d": 2}
min_key = None
min_value = None

first_iteration = True
for key in my_dict:
    if first_iteration:
        min_key = key
        min_value = my_dict[key]
        first_iteration = False
    elif my_dict[key] < min_value:
        min_key = key
        min_value = my_dict[key]

print("Key with the minimum value:", min_key)

#delete a list of keys from a dictionary
my_dict = {"a": 10, "b": 20, "c": 30, "d": 40}
keys_to_remove = ["b", "d"]
new_dict = {}

for key in my_dict:
    remove = False
    for del_key in keys_to_remove:
        if key == del_key:
            remove = True
            break
    if not remove:
        new_dict[key] = my_dict[key]

print("Updated dictionary:", new_dict)
