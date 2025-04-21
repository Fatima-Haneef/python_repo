from abc import ABC, abstractmethod
from dataclasses import dataclass
print("\n\n This is a OOP assignment's solution Q1")
#Question 1:
# Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person’s age.

class person:
    def __init__(self, name,country,date_of_birth ):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth
    def getdate_of_birth(self):
        print("Date of Birth of the person: ", self.date_of_birth)
        return self.date_of_birth
    
d1 = person("DJ", "USA", "1990-01-01")
d1.getdate_of_birth()

print("\n\n This is oops assignment's solution Q2")
#Question 2:
#Write a Python program to create a calculator class. Include methods for basic arithmetic operations.Create a class calculator with methods of adding, subtracting, multiply, and divide.
class calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        if self.num2 !=0:
            return self.num1 / self.num2
        else:
            return "Cannot divide by zero"
        
calc = calculator(10, 5)
print("Addition: ", calc.add())
print("Subtraction: ", calc.subtract())
print("Multiplication: ", calc.multiply())
print("Division: ", calc.divide())

print("\n\n This is oops assignment's solution Q3")
#Questions 3:
#First create a abstract class, ICaculator, all abstract methods of operations, then do inheritance, to implement a calculator functions in derived class.
class ICalculator(ABC):
    @abstractmethod
    def add(self, a, b):
        pass

    @abstractmethod
    def subtract(self, a, b):
        pass

    @abstractmethod
    def multiply(self, a, b):
        pass

    @abstractmethod
    def divide(self, a, b):
        pass
    
class Calculator(ICalculator):
        def add(self, a, b):
            return a + b

        def subtract(self, a, b):
            return a - b

        def multiply(self, a, b):
            return a * b

        def divide(self, a, b):
            if b != 0:
                return a / b
            else:
                return "Cannot divide by zero"
            
addition = Calculator()
print("inherited-calculator-addition: ",addition.add(4,6))
subtraction = Calculator()
print("inherited-calculator-subtraction: ",subtraction.subtract(8,7))
multiplication = Calculator()
print("inherited-calculator-multiplication: ",multiplication.multiply(5,6))
division = Calculator()
print("inherited-calculator-division: ",division.divide(10,2))

print("\n\n This is oops assignment's solution Q4")
#Question 4:
#Write a Python program to create a Data class for customer with following fields
#"Record ID","First Name","Last Name","Email","Phone Number","Contact owner","Primary Associated Company ID","Last Activity Date","Lead Status","Marketing contact status","Create Date","Associated Company"Also, create 5 objects of this data class.

@dataclass
class CustomerData:
    Record_ID: int
    First_Name: str
    Last_Name: str
    Email: str
    Phone_Number: str
    Contact_Owner: str
    Primary_Associated_CompanyID: int
    Last_Activity_Date: str
    Lead_Status: str
    Marketing_Contact_Status: str
    Create_Date: str
    Associated_Company: str

    def display(self):
        return (
            f"Record ID: {self.Record_ID}, First Name: {self.First_Name}, "
            f"Last Name: {self.Last_Name}, Email: {self.Email}, Phone Number: {self.Phone_Number}, "
            f"Contact Owner: {self.Contact_Owner}, Primary Associated Company ID: {self.Primary_Associated_CompanyID}, "
            f"Last Activity Date: {self.Last_Activity_Date}, Lead Status: {self.Lead_Status}, "
            f"Marketing Contact Status: {self.Marketing_Contact_Status}, Create Date: {self.Create_Date}, "
            f"Associated Company: {self.Associated_Company}"
        )

customer_data_display = CustomerData(
    Record_ID=1,
    First_Name="Fatima",
    Last_Name="Hanif",
    Email="fatima@example.com",
    Phone_Number="123-456-7890",
    Contact_Owner="Ahmad Basit",
    Primary_Associated_CompanyID=1001,
    Last_Activity_Date="2025-04-10",
    Lead_Status="New",
    Marketing_Contact_Status="Subscribed",
    Create_Date="2025-03-20",
    Associated_Company="Hanif Interiors"
)

print(customer_data_display.display())
    
print("\n\n This is oops assignment's solution Q5")
#Question 5:
#Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.
# Example:
# class Stack:
#  def __init__(self):
#  self.items = []

class stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
        print(f"Pushed {item} to stack.")
        
    def pop(self):
        if not self.is_empty():
            item = self.items.pop()
            print(f"Popped {item} from stack.")
            return item
        else:
            print("Stack is empty. Cannot pop.")
            return None
        
    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty. Cannot peek.")
            return None
    def size(self):
        return len(self.items)
        
stack1 = stack()
stack1.push(10)
stack1.push(20)
stack1.push(30)
print("peak-of-stack" ,stack1.peek())
stack1.pop()
stack1.pop()
print("stack-size",stack1.size())

print("\n\n This is oops assignment's solution Q6")
#Question 6:
# Write a Python program to create a class representing a queue data structure. Include methods for 
# enqueueing and dequeueing elements.
# class Queue:
#  def __init__(self):
#  self.items = []

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        
        self.items.append(item)

    def dequeue(self):
        
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Queue is empty!"

    def peek(self):
        
        if not self.is_empty():
            return self.items[0]
        else:
            return "Queue is empty!"

    def size(self):
        return len(self.items)

    def display(self):
        return self.items



q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Queue:", q.display())
print("Dequeued:", q.dequeue())
print("After Dequeue:", q.display())
print("Front element:", q.peek())
print("Is Queue empty?", q.is_empty())
print("Queue size:", q.size())

print("/n/n This is oops assignment's solution Q7")
#Question 7:
# Employee Class with Salary, Department, and Overtime Calculation
# Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and 
# emp_department and methods like calculate_emp_salary, emp_assign_department, and
# print_employee_details.
# Sample Employee Data:
# "ADAMS", "E7876", 50000, "ACCOUNTING"
# "JONES", "E7499", 45000, "RESEARCH"
# "MARTIN", "E7900", 50000, "SALES"
# "SMITH", "E7698", 55000, "OPERATIONS"
# Use 'assign_department' method to change the department of an employee.
# Use 'print_employee_details' method to print the details of an employee.
# Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked, which is the 
# number of hours worked by the employee. If the number of hours worked is more than 50, the 
# method computes overtime and adds it to the salary. Overtime is calculated as following formula:
# overtime = hours_worked - 50
# Overtime amount = (overtime * (salary / 50))
# Be creative in defining the class.

class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def calculate_emp_salary(self, hours_worked):
        if hours_worked > 50:
            overtime_hours = hours_worked - 50
            overtime_rate = self.emp_salary / 50
            overtime_pay = overtime_hours * overtime_rate
            total_salary = self.emp_salary + overtime_pay
            print(f"[{self.emp_name}] Overtime pay of {overtime_pay} added.")
        else:
            total_salary = self.emp_salary
            print(f"[{self.emp_name}] No overtime.")
        
        print(f"[{self.emp_name}] Total Salary after overtime (if any): {total_salary}")
        return total_salary

    def emp_assign_department(self, new_department):
        print(f"[{self.emp_name}] Department changed from {self.emp_department} to {new_department}.")
        self.emp_department = new_department

    def print_employee_details(self):
        print("--------------------------------------------------")
        print(f"Employee ID        : {self.emp_id}")
        print(f"Employee Name      : {self.emp_name}")
        print(f"Employee Salary    : {self.emp_salary}")
        print(f"Employee Department: {self.emp_department}")
        print("--------------------------------------------------")


emp1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
emp2 = Employee("JONES", "E7499", 45000, "RESEARCH")
emp3 = Employee("MARTIN", "E7900", 50000, "SALES")
emp4 = Employee("SMITH", "E7698", 55000, "OPERATIONS")

emp1.print_employee_details()
emp1.emp_assign_department("FINANCE")
emp1.calculate_emp_salary(55)
emp1.print_employee_details()

emp2.print_employee_details()
emp2.calculate_emp_salary(48)

emp3.print_employee_details()
emp3.emp_assign_department("MARKETING")
emp3.calculate_emp_salary(60)

emp4.print_employee_details()
emp4.calculate_emp_salary(50)
    
        
        
# Questions 8.
# Restaurant Class with Menu, Table Reservation, and Order Management
# Write a Python class Restaurant with attributes like menu_items, book_table, and customer_orders, 
# and methods like add_item_to_menu, book_tables, and customer_order.
# Perform the following tasks now:
# Now add items to the menu.
# Make table reservations.
# Take customer orders.
# Print the menu.
# Print table reservations.
# Print customer orders.
# Note: Use dictionaries and lists to store the data.
class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.table_reservations = []
        self.customer_orders = []

    def add_item_to_menu(self, item_name, price):
        self.menu_items[item_name] = price

    def book_tables(self, table_number, customer_name):
        reservation = {'table_number': table_number, 'customer_name': customer_name}
        self.table_reservations.append(reservation)

    def customer_order(self, customer_name, items):
        order = {'customer_name': customer_name, 'items': items}
        self.customer_orders.append(order)

    def print_menu(self):
        print("--- MENU ---")
        for item, price in self.menu_items.items():
            print(f"{item}: Rs {price}")

    def print_table_reservations(self):
        print("--- TABLE RESERVATIONS ---")
        for res in self.table_reservations:
            print(f"Table {res['table_number']} reserved for {res['customer_name']}")

    def print_customer_orders(self):
        print("--- CUSTOMER ORDERS ---")
        for order in self.customer_orders:
            print(f"{order['customer_name']} ordered: {', '.join(order['items'])}")


# Create a restaurant object
my_restaurant = Restaurant()

# Add items to menu
my_restaurant.add_item_to_menu("Burger", 350)
my_restaurant.add_item_to_menu("Pizza", 800)
my_restaurant.add_item_to_menu("Fries", 200)
my_restaurant.add_item_to_menu("Cold Drink", 120)

# Make table reservations
my_restaurant.book_tables(1, "Ali")
my_restaurant.book_tables(2, "Fatima")

# Take customer orders
my_restaurant.customer_order("Ali", ["Burger", "Cold Drink"])
my_restaurant.customer_order("Fatima", ["Pizza", "Fries"])

# Print everything
my_restaurant.print_menu()
my_restaurant.print_table_reservations()
my_restaurant.print_customer_orders()

# Question 9.
# BankAccount Class with Deposit, Withdrawal, and Transaction History
# Write a Python class BankAccount with attributes like account_number, balance, date_of_opening 
# and customer_name, and methods like deposit, withdraw, and check_balance.

class BankAccount:
    def __init__(self, account_number, customer_name, date_of_opening, balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.date_of_opening = date_of_opening
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: Rs {amount}")
        else:
            self.transaction_history.append("Failed deposit: Amount must be positive")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawn: Rs {amount}")
        else:
            self.transaction_history.append("Failed withdrawal: Insufficient funds")

    def check_balance(self):
        print(f"Account Balance: Rs {self.balance}")

    def print_transaction_history(self):
        print("--- Transaction History ---")
        for transaction in self.transaction_history:
            print(transaction)


# Sample usage
account1 = BankAccount("ACC12345", "Fatima Hanif", "2025-04-19", 10000)

account1.deposit(5000)
account1.withdraw(3000)
account1.withdraw(15000)  # Should fail due to insufficient funds
account1.check_balance()
account1.print_transaction_history()


