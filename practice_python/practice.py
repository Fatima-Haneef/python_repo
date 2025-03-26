users = [
    {"name": "fatima", "skills": ["python", "react", "ai"], "experience": 2},
    {
        "name": "fatima_hanif",
        "skills": ["node.js", "express.js", "mongodb"],
        "experience": 10,
    },
    {
        "name": "fatima_Muhammad_hanif",
        "skills": ["python", "ml", "ai"],
        "experience": 20,
    },
]
senior_python_devs = []
for user in users:
    if "python" in user["skills"] and user["experience"] > 4:
        senior_python_devs.append(user["name"])
        print(
            f"{user['name']} is a senior python developer with {user['experience']} years of experience"
        )


orignal_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6}
squared_dict = {}
for key, value in orignal_dict.items():
    squared_dict[key] = value**2
    print(f"{key}'s square is {value**2}")

    names = ["Alice", "Bob", "Charlie"]
ages = [30, 25, 35]
skills = ["Python", "JavaScript", "AI"]

combined_info = []
for i in range(len(names)):
    combined_info.append({"name": names[i], "age": ages[i], "primary_skill": skills[i]})
print("Combined User Information:", combined_info)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count = 0
odd_count = 0
total_sum = 0

for num in numbers:
    total_sum += num
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Total Sum:", total_sum)
print("Even Count:", even_count)
print("Odd Count:", odd_count)


# Complex Conditional Accumulation
mixed_data = [1, "hello", 2, [3, 4], "world", 6]
numeric_sum = 0
string_list = []

for item in mixed_data:
    if isinstance(item, int):
        numeric_sum += item
    elif isinstance(item, str):
        string_list.append(item)

print("numeric_sum", numeric_sum)
print("string_list", string_list)


# 7. Nested Dictionary Traversal
complex_data = {
    "team1": {"members": ["alice", "bob"], "projects": 3},
    "team2": {"members": ["charlie", "david"], "projects": 2},
}

team_details = []
for team_name, team_info in complex_data.items():
    for member in team_info["members"]:
        team_details.append(
            {
                "team": team_name,
                "member": member,
                "project_count": team_info["projects"],
            }
        )

print("Team details", team_details)
