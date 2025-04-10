# Python Program to Check if a String is a Pangram or Not [The program takes a string and checks if it is a pangram or not.]
def is_pangram(s):
    s = s.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in s:
            return False
    return True


text = input("Enter a string: ")
print("Pangram" if is_pangram(text) else "Not a Pangram")


# Python Program to Replace Every Blank Space with Hyphen in a String[The program takes a string and replaces every blank space with a hyphen.]
def replace_spaces_with_hyphen(s):
    result = ""
    for char in s:
        if char == " ":
            result += "-"
        else:
            result += char
    return result


text = input("Enter a string: ")
print(replace_spaces_with_hyphen(text))


# This is a Python Program to display which letters are in the two strings but not in both.
def uncommon_letters(s1, s2):
    result = ""
    for char in s1:
        if char not in s2 and char not in result:
            result += char
    for char in s2:
        if char not in s1 and char not in result:
            result += char
    return result


s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print("Uncommon letters:", uncommon_letters(s1, s2))


# Python Program to Find the Larger String without using Built-in Functions[The program takes in two strings and display the larger string without using built-in function.]
def larger_string(s1, s2):
    len1 = 0
    for _ in s1:
        len1 += 1
    len2 = 0
    for _ in s2:
        len2 += 1
    return s1 if len1 > len2 else s2


s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print("Larger string is:", larger_string(s1, s2))


# Python Program to Count Number of Uppercase and Lowercase Letters in a String[The program takes a string and counts the number of lowercase letters and uppercase letters in the string.]
def count_case(s):
    upper = lower = 0
    for char in s:
        if "A" <= char <= "Z":
            upper += 1
        elif "a" <= char <= "z":
            lower += 1
    return upper, lower


s = input("Enter a string: ")
u, l = count_case(s)
print("Uppercase letters:", u)
print("Lowercase letters:", l)


# Python Program to Check if Two Strings are Anagram. [An anagram in Python is a pair of strings that have the same characters, but in a different order. It involves rearranging the letters of one string to form the other.]
def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    for char in s1:
        if s1.count(char) != s2.count(char):
            return False
    return True


s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print("Anagrams" if are_anagrams(s1, s2) else "Not Anagrams")


# Python Program to Check if the Substring is Present in the Given String. [The program takes a string and checks if a substring is present in the given string.]
def is_substring(string, substring):
    for i in range(len(string) - len(substring) + 1):
        match = True
        for j in range(len(substring)):
            if string[i + j] != substring[j]:
                match = False
                break
        if match:
            return True
    return False


string = input("Enter the main string: ")
substring = input("Enter the substring: ")
print("Substring Found" if is_substring(string, substring) else "Not Found")


# Python Program to Print All Permutations of a String in Lexicographic Order without Recursion. The problem is the display all permutations of a string in lexicographic or dictionary order.
def next_permutation(s):
    s = list(s)
    n = len(s)

    i = n - 2
    while i >= 0 and s[i] >= s[i + 1]:
        i -= 1

    if i == -1:
        return False, "".join(s)

    j = n - 1
    while s[j] <= s[i]:
        j -= 1

    s[i], s[j] = s[j], s[i]

    s[i + 1 :] = reversed(s[i + 1 :])

    return True, "".join(s)


def lexicographic_permutations(string):

    string = "".join(sorted(string))
    print(string)

    has_next = True
    while has_next:
        has_next, string = next_permutation(string)
        if has_next:
            print(string)


input_string = "ABC"
lexicographic_permutations(input_string)


# Python Program to Calculate the Length of a String Without using Library Functions.[ The program takes a string and calculates the length of the string without using library functions.
def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count


s = input("Enter a string: ")
print("Length:", string_length(s))


# Python Program to Create a New String Made up of First and Last 2 Characters. The program takes a string and forms a new string made of the first 2 characters and last 2 characters from a given string.
def first_last_2_chars(s):
    if len(s) < 2:
        return "Empty String"
    return s[:2] + s[-2:]


s = input("Enter a string: ")
print("New string:", first_last_2_chars(s))
