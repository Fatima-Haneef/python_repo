# a = 2
# b = "abc"
# c = 2.5
# print(a + c)

print("hello world")
print("My name is FATIMA MUHAMMAD HANIF")
print("My name is FATIMA MUHAMMAD HANIF")
print("My name is FATIMA MUHAMMAD HANIF")


name = input("Your Name")
print ("Hello " + name)




#Type Inference in Python

# Specific Data Type
strVar = str("Hello World - Richard")
print(type(strVar))

strVar2="Hello World - Richard"
print(type(strVar2))


#---------------------- int

intVar = int(50)
print(type(intVar))

intVar2=50
print(type(intVar2))


#---------------------- float

floatVar = float(50.3)
print(type(floatVar))

floatVar2=50.3
print(type(floatVar2))

#---------------------


#---------------------- float = with an "e" to indicate the power of 10

floatEVar = float(35e3)
print(type(floatEVar))

floatEVar2=35e3
print(type(floatEVar2))

#---------------------

#---------------------- Complex = numbers are written with a "j" as the imaginary part
ComplexVar = complex(3+5j)
print(type(ComplexVar))

ComplexVar2=3+5j
print(type(ComplexVar2))



print(bool(1))  # True because 1 is a truthy value
print(bool("Hello"))  # True because non-empty strings are truthy
print(bool(0))  # False because 0 is a falsy value


print(5 > 2)  # True because 5 is greater than 2
print(5 == 2)  # False because 5 is not equal to 2



print(True and True)  # True
print(False or True)  # True




#arithmatic operations
a = 7
b = 2

# addition
print ('Sum: ', a + b)  

# subtraction
print ('Subtraction: ', a - b)   

# multiplication
print ('Multiplication: ', a * b)  

# division
print ('Division: ', a / b) 

# floor division
print ('Floor Division: ', a // b)

# modulo
print ('Modulo: ', a % b)  

# a to the power b
print ('Power: ', a ** b) 


# cycle 2

a = -21
b = 10
# Addition
print ("a + b : ", a + b)
# Subtraction
print ("a - b : ", a - b)
# Multiplication
print ("a * b : ", a * b)
# Division
print ("a / b : ", a / b)
# Modulus
print ("a % b : ", a % b)
# Exponent
print ("a ** b : ", a ** b)
# Floor Division
print ("a // b : ", a // b)#Rule: Floor division always rounds down (towards negative infinity).



# logical operators
# logical AND
print(True and True)     # True
print(True and False)    # False

# logical OR
print(True or False)     # True

# logical NOT
print(not True)          # False

# operator
a = 5
b = 6

print((a > 2) and (b >= 6))    # True



username = "fatima"
password = "pass123"

if username == "fatima" and password == "pass123":
    print("Login successful!")
else:
    print("Invalid credentials!")

#assignment operator

# Assignment Operator
a = 10
# Addition Assignment
a += 5
print ("a += 5 : ", a)
# Subtraction Assignment
a -= 5
print ("a -= 5 : ", a)
# Multiplication Assignment
a *= 5
print ("a *= 5 : ", a)
# Division Assignment
a /= 5
print ("a /= 5 : ",a)
# Remainder Assignment
a %= 3
print ("a %= 3 : ", a)
# Exponent Assignment
a **= 2
print ("a **= 2 : ", a)
# Floor Division Assignment
a //= 3
print ("a //= 3 : ", a)

