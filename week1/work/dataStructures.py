



# #touple project

# # Student Management System using Tuples

# # List to store student records (each record is a tuple)
# students = [
#     (101, "Alice", 20, "A"),
#     (102, "Bob", 21, "B"),
#     (103, "Charlie", 19, "A"),
#     (104, "David", 22, "C")
# ]

# # Function to display all students
# def display_students():
#     print("\n--- Student Records ---")
#     for student in students:
#         print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}")
#     print("----------------------\n")

# # Function to search for a student by ID
# def search_student(student_id):
#     for student in students:
#         if student[0] == student_id:
#             print("\nStudent Found!")
#             print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}")
#             return
#     print("\nStudent not found!")

# # Function to add a new student
# def add_student():
#     student_id = int(input("Enter Student ID: "))
#     name = input("Enter Name: ")
#     age = int(input("Enter Age: "))
#     grade = input("Enter Grade: ")

#     # Creating a tuple for the new student
#     new_student = (student_id, name, age, grade)

#     # Tuples are immutable, so we use list to store new students
#     global students
#     students = students + [new_student]  # Adding a new tuple to the list

#     print("\nStudent added successfully!")

# # Main menu
# while True:
#     print("\nStudent Management System")
#     print("1. Display All Students")
#     print("2. Search Student by ID")
#     print("3. Add New Student")
#     print("4. Exit")
    
#     choice = input("Enter your choice: ")

#     if choice == "1":
#         display_students()
#     elif choice == "2":
#         student_id = int(input("Enter Student ID to search: "))
#         search_student(student_id)
#     elif choice == "3":
#         add_student()
#     elif choice == "4":
#         print("\nExiting... Have a nice day!")
#         break
#     else:
#         print("\nInvalid choice! Please try again.")


# Note : In case of list, we use square
# brackets []. Here we use round brackets ()



t = (10, 20, 30) 

print(t)
print(type(t))


print (" Next  run")
# Next  run


tt = (1, 2, 3, 4, 5)

# tuples are indexed
print(tt[1])
print(tt[4])

# tuples contain duplicate elements
tt = (1, 2, 3, 4, 2, 3)
print(tt)


print (" Next  run")
# Next  run


t = (10, 5, 20)

print("Value in t[0] = ", t[0])
print("Value in t[1] = ", t[1])
print("Value in t[2] = ", t[2])


print (" Next  run")
# Next  run

t = (10, 5, 20)

print("Value in t[-1] = ", t[-1])
print("Value in t[-2] = ", t[-2])
print("Value in t[-3] = ", t[-3])


# Define a tuple
t = (1, 2, 3, 4, 5)

# Traverse through each item in the tuple
for x in t:
    print(x, end=" ")



print (" Next  run")
# Next  run


    # Code for concatenating 2 tuples
t1 = (0, 1, 2, 3)
t2 = ('python', 'geek')

# Concatenating above two
print(t1 + t2)



print (" Next  run")
# Next  run


# Code for creating nested tuples
t1 = (0, 1, 2, 3)
t2 = ('python', 'geek')

t3 = (t1, t2)
print(t3)


print (" Next  run")
# Next  run


# Code to create a tuple with repetition
tx = ('python',)*3
print(tx)


print (" Next  run")
# Next  run