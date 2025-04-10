#print first 10 natural numbers using while loop
num = 1

while num <= 10:
    print(num)
    num += 1

#take input from user and print even  numbers till the input number
limit = int(input("Enter a number to get even numbers: "))
num = 2

while num <= limit:
    print(num)
    num += 2
    
#take input from user and print odd  till the input number
limit = int(input("Enter a number to get odd numbers: "))
num = 1

while num <= limit:
    print(num)
    num += 2

    
#take input from user and print prime  numbers  till the input number
limit = int(input("Enter a number to get prime numbers: "))
num = 2

while num <= limit:
    is_prime = True
    i = 2

    while i * i <= num:
        if num % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print(num)

    num += 1
    
#print multiplication table of a given number
num = int(input("Enter a number to get its multiplication table: "))
i = 1

while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1
