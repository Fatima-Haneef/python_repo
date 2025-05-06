# users = [
#     {"name": "fatima", "skills": ["python", "react", "ai"], "experience": 2},
#     {
#         "name": "fatima_hanif",
#         "skills": ["node.js", "express.js", "mongodb"],
#         "experience": 10,
#     },
#     {
#         "name": "fatima_Muhammad_hanif",
#         "skills": ["python", "ml", "ai"],
#         "experience": 20,
#     },
# ]
# senior_python_devs = []
# for user in users:
#     if "python" in user["skills"] and user["experience"] > 4:
#         senior_python_devs.append(user["name"])
#         print(
#             f"{user['name']} is a senior python developer with {user['experience']} years of experience"
#         )


# orignal_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6}
# squared_dict = {}
# for key, value in orignal_dict.items():
#     squared_dict[key] = value**2
#     print(f"{key}'s square is {value**2}")

#     names = ["Alice", "Bob", "Charlie"]
# ages = [30, 25, 35]
# skills = ["Python", "JavaScript", "AI"]

# combined_info = []
# for i in range(len(names)):
#     combined_info.append({"name": names[i], "age": ages[i], "primary_skill": skills[i]})
# print("Combined User Information:", combined_info)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_count = 0
# odd_count = 0
# total_sum = 0

# for num in numbers:
#     total_sum += num
#     if num % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1

# print("Total Sum:", total_sum)
# print("Even Count:", even_count)
# print("Odd Count:", odd_count)


# # Complex Conditional Accumulation
# mixed_data = [1, "hello", 2, [3, 4], "world", 6]
# numeric_sum = 0
# string_list = []

# for item in mixed_data:
#     if isinstance(item, int):
#         numeric_sum += item
#     elif isinstance(item, str):
#         string_list.append(item)

# print("numeric_sum", numeric_sum)
# print("string_list", string_list)


# # 7. Nested Dictionary Traversal
# complex_data = {
#     "team1": {"members": ["alice", "bob"], "projects": 3},
#     "team2": {"members": ["charlie", "david"], "projects": 2},
# }

# team_details = []
# for team_name, team_info in complex_data.items():
#     for member in team_info["members"]:
#         team_details.append(
#             {
#                 "team": team_name,
#                 "member": member,
#                 "project_count": team_info["projects"],
#             }
#         )

# print("Team details", team_details)


# # advaced examples
# start, end = 10, 50
# primes = []

# for num in range(start, end + 1):
#     is_prime = True
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         primes.append(num)

# print("Prime numbers:", primes)


# list1 = [1, 2, 3, 4]
# list2 = [10, 20, 30, 40]
# list3 = ["a", "b", "c", "d"]

# for x, y, z in zip(list1, list2, list3):
#     print(f"{x} - {y} - {z}")


# for i in range(0, 100, 7):  # Step of 7
#     print(i, end=" ")
# print()


# data = ["apple", "banana", "cherry"]

# for index, value in enumerate(data, start=1):
#     print(f"{index}: {value}")


# data = ["apple", "banana", "cherry"]

# for index, value in enumerate(data, start=1):
#     print(f"{index}: {value}")


# num = 1
# while True:
#     print(num, end=" ")
#     num *= 2  # Doubles each iteration
#     if num > 1000:
#         break
# print()


# matrix = [[j for j in range(1, 6)] for i in range(3)]
# for row in matrix:
#     print(row)


# numbers = list(range(1, 21))
# even_numbers = [num for num in numbers if num % 2 == 0]
# odd_numbers = [num for num in numbers if num % 2 != 0]

# print("Even:", even_numbers)
# print("Odd:", odd_numbers)


# for i in reversed(range(1, 11)):
#     print(i, end=" ")
# print()


# data = [
#     {"name": "A", "score": 90},
#     {"name": "B", "score": 45},
#     {"name": "C", "score": 78},
#     {"name": "D", "score": 85},
# ]

# passed_students = [d["name"] for d in data if d["score"] >= 50]
# print("Passed:", passed_students)


# stats = {"wins": 12, "losses": 5, "draws": 3}

# for key, value in stats.items():
#     if value > 5:
#         print(f"{key}: {value}")


# numbers = [2, 4, 6, 8, 10]
# result = list(map(lambda x: x * 7, numbers))
# print(result)


# words = ["sky", "tree", "azzzzzz","brrr", "cloud", "myth", "sun"]
# vowel_words = list(filter(lambda word: any(char in 'aeiouAEIOU' for char in word), words))
# print(vowel_words)

# from functools import reduce
# numbers = [2,2,1,1,2,20]
# # Multiply all numbers using reduce
# product = reduce(lambda x, y: x * y, numbers)
# print(product)


# class my_class:
  
#     agent_code = "A001"
#     serial_number = 1234567890
    
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         print(f" Client  {self.name} is created her age is {self.age}")
#     def __del__(self):
#         print(f"Person deleted with name: {self.name} and age: {self.age}")
        
# result = my_class("fatima",20)
# print(my_class.agent_code)
# print(my_class.serial_number)
# del result
 
