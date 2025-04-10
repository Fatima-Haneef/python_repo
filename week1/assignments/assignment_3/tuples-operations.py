# Python Program to Create a List of Tuples with the First Element as the Number and Second
# Element as the Square of the Number. The program takes a range and creates a list of tuples
# within that range with the first element as the number and the second element as the square of
# the number


start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

square_tuples = [(x, x**2) for x in range(start, end + 1)]

print("List of tuples (number, square):")
print(square_tuples)


# Python Program to Remove All Tuples in a List Outside the Given Range. The program removes
# all tuples in a list of tuples with the USN outside the given range.
# Problem Solution
# 1. Take in the lower and upper roll number from the user.
# 2. Then append the prefixes of the USN’s to the roll numbers.
# 3. Using list comprehension, find out which USN’s lie in the given range.
# 4. Print the list containing the tuples.
# 5. Exit.
# In the context of a university, a USN, or University Student Number, is a unique identifier
# assigned to each student, acting as a primary identifier for their academic records and
# interactions with the institution.


# Step 1: Sample list of tuples (USN, Name)
students = [
    ("CS100", "Ali"),
    ("CS101", "Ayesha"),
    ("CS102", "Zain"),
    ("CS105", "Fatima"),
    ("CS110", "Usman"),
    ("CS115", "Sara"),
]

# Step 2: Take roll number range input
lower = int(input("Enter lower roll number (e.g., 101): "))
upper = int(input("Enter upper roll number (e.g., 110): "))

# Step 3: Filter list using list comprehension
filtered_students = [
    (usn, name) for usn, name in students if lower <= int(usn[2:]) <= upper
]

# Step 4: Print result
print("Filtered student list (within roll number range):")
print(filtered_students)
