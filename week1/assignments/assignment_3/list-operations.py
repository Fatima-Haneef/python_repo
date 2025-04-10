# This is a Python Program to find the largest number in a list. The program takes a list and prints the largest number in the list.


def find_largest(lst):
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num


lst = list(map(int, input("Enter numbers separated by space: ").split()))
print("Largest number:", find_largest(lst))


# The program takes a list and prints the largest number in the list. The program takes a list and prints the second largest number in the list.
def second_largest(lst):
    first = second = float("-inf")
    for num in lst:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second


lst = list(map(int, input("Enter numbers separated by space: ").split()))
print("Second largest number:", second_largest(lst))


# Python Program to Print Largest Even and Largest Odd Number in a List. The program takes in a list and prints the largest even and largest off number in it.
def find_largest_even_odd(lst):
    largest_even = float("-inf")
    largest_odd = float("-inf")
    for num in lst:
        if num % 2 == 0 and num > largest_even:
            largest_even = num
        elif num % 2 != 0 and num > largest_odd:
            largest_odd = num
    return largest_even, largest_odd


lst = list(map(int, input("Enter numbers separated by space: ").split()))
even, odd = find_largest_even_odd(lst)
print("Largest Even:", even)
print("Largest Odd:", odd)


# Python Program to Find Average of a List. The program takes the elements of the list one by one and displays the average of the elements of the list.
def average(lst):
    total = 0
    for num in lst:
        total += num
    return total / len(lst)


lst = list(map(int, input("Enter numbers separated by space: ").split()))
print("Average:", average(lst))


# Python Program to Count Occurrences of Element in List. The program takes a number and searches the number of times the particular number occurs in a list.
def count_occurrences(lst, target):
    count = 0
    for num in lst:
        if num == target:
            count += 1
    return count


lst = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter number to count: "))
print(f"{target} occurs {count_occurrences(lst, target)} times")


# Python Program to Remove Duplicates from a List. The program takes a lists and removes the duplicate items from the list.
def remove_duplicates(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique


lst = list(map(int, input("Enter numbers separated by space: ").split()))
print("List after removing duplicates:", remove_duplicates(lst))


# Python Program to Find the Number Occurring Odd Number of Times in a List. A list is given in which all elements except one element occurs an even number of times. The problem is to find the element that occurs an odd number of times.
def find_odd_occurrence(lst):
    for num in lst:
        count = 0
        for item in lst:
            if item == num:
                count += 1
        if count % 2 != 0:
            return num


lst = list(map(int, input("Enter numbers separated by space: ").split()))
print("Number occurring odd number of times:", find_odd_occurrence(lst))


# Python Program to Find the Union of Two Lists. The program takes two lists and finds the unions of the two lists.
def union_lists(list1, list2):
    union = list1[:]
    for item in list2:
        if item not in union:
            union.append(item)
    return union


list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))
print("Union of lists:", union_lists(list1, list2))

# Python Program to Print Largest Even and Largest Odd Number in a List. The program takes in a list and prints the largest even and largest off number in it.


lst = list(map(int, input("Enter numbers separated by space: ").split()))
largest_even = float("-inf")
largest_odd = float("-inf")

for num in lst:
    if num % 2 == 0 and num > largest_even:
        largest_even = num
    elif num % 2 != 0 and num > largest_odd:
        largest_odd = num

print("Largest Even:", largest_even)
print("Largest Odd:", largest_odd)


# Python Program to Find the Number Occurring Odd Number of Times in a List. A list is given in which all elements except one element occurs an even number of times. The problem is to find the element that occurs an odd number of times.


lst = list(map(int, input("Enter list items: ").split()))

for num in lst:
    count = 0
    for i in lst:
        if i == num:
            count += 1
    if count % 2 != 0:
        print("Number occurring odd number of times:", num)
        break

# Python Program to Find the Union of Two Lists. The program takes two lists and finds the unions of the two lists.

list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

union = list1[:]
for item in list2:
    if item not in union:
        union.append(item)

print("Union of two lists:", union)
