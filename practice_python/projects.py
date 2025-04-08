# import json
# import os

# TODO_FILE = "tasks.json"

# def load_tasks():
#     if os.path.exists(TODO_FILE):
#         with open(TODO_FILE, "r") as f:
#             return json.load(f)
#     return []

# def save_tasks(tasks):
#     with open(TODO_FILE, "w") as f:
#         json.dump(tasks, f)

# def add_task(tasks):
#     task = input("Enter task: ").strip()
#     tasks.append({"task": task, "completed": False})
#     save_tasks(tasks)
#     print("Task added!")

# def view_tasks(tasks):
#     if not tasks:
#         print("No tasks.")
#         return
#     for i, task in enumerate(tasks, 1):
#         status = "✓" if task["completed"] else " "
#         print(f"{i}. [{status}] {task['task']}")

# def delete_task(tasks):
#     view_tasks(tasks)
#     try:
#         task_num = int(input("Enter task number to delete: ")) - 1
#         if 0 <= task_num < len(tasks):
#             del tasks[task_num]
#             save_tasks(tasks)
#             print("Task deleted!")
#         else:
#             print("Invalid task number.")
#     except ValueError:
#         print("Invalid input.")

# def main():
#     tasks = load_tasks()
#     while True:
#         print("\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit")
#         choice = input("Choose an option: ")
#         if choice == "1":
#             add_task(tasks)
#         elif choice == "2":
#             view_tasks(tasks)
#         elif choice == "3":
#             delete_task(tasks)
#         elif choice == "4":
#             break
#         else:
#             print("Invalid choice.")

# if __name__ == "__main__":
#     main()




# import requests
# from bs4 import BeautifulSoup

# def scrape_quotes():
#     url = "http://quotes.toscrape.com"
#     try:
#         response = requests.get(url)
#         response.raise_for_status()  # Check for HTTP errors
#         soup = BeautifulSoup(response.text, "html.parser")
#         quotes = soup.find_all("div", class_="quote")
        
#         for quote in quotes:
#             text = quote.find("span", class_="text").text
#             author = quote.find("small", class_="author").text
#             print(f"{text}\n— {author}\n")
#     except requests.exceptions.RequestException as e:
#         print(f"Error: {e}")

# if __name__ == "__main__":
#     scrape_quotes()


import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (download from https://www.kaggle.com/c/titanic/data)
df = pd.read_csv("titanic.csv")

# Basic analysis
survival_rate = df.groupby('Sex')['Survived'].mean()
print("Survival Rate by Gender:\n", survival_rate)

# Plotting
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Survival by class
df.groupby('Pclass')['Survived'].mean().plot(kind='bar', ax=axes[0], title='Survival Rate by Class')

# Age distribution
df['Age'].hist(ax=axes[1], bins=20)
axes[1].set_title('Age Distribution')

plt.tight_layout()
plt.show()