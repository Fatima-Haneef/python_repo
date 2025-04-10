# python Program to Find the Area of a Triangle[The program takes three sides of a triangle and rints the area formed by all three sides.]

import math


def area_of_triangle(a, b, c):
    s = (a + b + c) / 2  
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))
print("Area of triangle:", area_of_triangle(a, b, c))


# python Program to Find Quotient and Remainder of Two Numbers[The program takes two numbers and prints the quotient and remainder.]


def quotient_remainder(a, b):
    q = a // b
    r = a % b
    return q, r


a = int(input("Enter dividend: "))
b = int(input("Enter divisor: "))
q, r = quotient_remainder(a, b)
print("Quotient:", q)
print("Remainder:", r)


# Python Program to Print an Identity Matrix [The program takes a number n and prints an identity matrix of the desired size.]


def identity_matrix(n):
    for i in range(n):
        row = ""
        for j in range(n):
            if i == j:
                row += "1 "
            else:
                row += "0 "
        print(row)


n = int(input("Enter size of identity matrix: "))
identity_matrix(n)


# Python Program to Find the LCM of Two Numbers [The program takes two numbers and prints the LCM of two numbers.]


def find_lcm(a, b):
    max_val = a if a > b else b
    while True:
        if max_val % a == 0 and max_val % b == 0:
            return max_val
        max_val += 1


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("LCM:", find_lcm(a, b))


# python Program to Find the Sum of Natural Numbers. [Write a program that takes the number of terms and calculates the sum of the first N natural numbers.]


def sum_natural(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


n = int(input("Enter number of terms: "))
print("Sum:", sum_natural(n))


# Python Program to Check If Two Numbers are Amicable Numbers or Not[The program takes two numbers and checks if they are amicable numbers.] Amicable numbers are pairs of different numbers where the sum of the proper divisors (divisors excluding the number itself) of one number equals the other number, and vice versa. The smallest example is 220 and 284.


def sum_of_divisors(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total


def are_amicable(a, b):
    return sum_of_divisors(a) == b and sum_of_divisors(b) == a


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Amicable Numbers" if are_amicable(a, b) else "Not Amicable")


# Python Program to Find All Perfect Squares in the Given Range.[ The program takes a range and creates a list of all numbers in the range which are perfect squares and the sum of the digits is less than 10.] To find perfect squares within a range, identify the smallest and largest integers whose squares fall within that range, then list the squares of those integers.
# Example:
# Range: 1 to 100
# Smallest integer: 1 (1 * 1 = 1)
# Largest integer: 10 (10 * 10 = 100)
# Perfect Squares: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100


def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total


def perfect_squares_in_range(start, end):
    squares = []
    i = 1
    while i * i <= end:
        square = i * i
        if square >= start and sum_of_digits(square) < 10:
            squares.append(square)
        i += 1
    return squares


start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
print("Perfect squares with digit-sum < 10:", perfect_squares_in_range(start, end))


# Python Program to Check Armstrong Number Armstrong Number in Python: Armstrong Number is an integer such that the sum of the cubes  of its digits is equal to the number itself. Armstrong numbers are 0, 1, 153, 370, 371, 407, etc.
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total


def perfect_squares_in_range(start, end):
    squares = []
    i = 1
    while i * i <= end:
        square = i * i
        if square >= start and sum_of_digits(square) < 10:
            squares.append(square)
        i += 1
    return squares


start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
print("Perfect squares with digit-sum < 10:", perfect_squares_in_range(start, end))


# [Write a Python Program to check if a number is an Armstrong number. If the number is an Armstrong then display “it is an Armstrong number” else display “it is not an Armstrong number”.]
def is_armstrong(n):
    original = n
    total = 0
    digits = 0
    temp = n
    while temp > 0:
        digits += 1
        temp = temp // 10
    temp = n
    while temp > 0:
        digit = temp % 10
        total += digit**digits
        temp = temp // 10
    return total == original


# Test
n = int(input("Enter a number: "))
if is_armstrong(n):
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")
