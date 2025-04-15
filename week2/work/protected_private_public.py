# Bank Management System with Public, Protected, and Private Attributes

class BankAccount:
    # Public property
    account_counter = 1000  # To generate account numbers
    def __init__(self, owner, email, balance=0):
        self.owner = owner
        self.email = email
        self.account_number = BankAccount.account_counter  # Public info
        self.__balance = balance  # Private balance
        BankAccount.account_counter += 1  # Increment account number for next account

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if self._is_valid_withdrawal(amount):  # Protected method
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self.__balance  # Access private balance via method

    def display_account_info(self):
        # Public method to display basic account info
        print(f"Account Number: {self.account_number}, Owner: {self.owner}, Email: {self.email}")
        
    def _is_valid_withdrawal(self, amount):
        """ Protected method to check if the withdrawal is valid """
        return 0 < amount <= self.__balance

    def __apply_interest(self):
        """ Private method for interest calculation (cannot be accessed outside) """
        interest = self.__balance * 0.05
        self.__balance += interest
        print(f"Applied interest of {interest}. New balance: {self.__balance}")

class SavingsAccount(BankAccount):
    """ Derived class for SavingsAccount with interest handling """
    def __init__(self, owner, email, balance=0):
        super().__init__(owner, email, balance)

    def apply_interest(self):
        """ Public method to allow interest application for savings account """
        self._BankAccount__apply_interest()  # Corrected: Access private method from BankAccount

    def get_balance(self):
        return f"Your balance is: {super().get_balance()}"



class CheckingAccount(BankAccount):
    """ Derived class for CheckingAccount """
    def __init__(self, owner, email, balance=0):
        super().__init__(owner, email, balance)

    def display_account_info(self):
        """ Override method to display customized account info """
        print(f"Checking Account - Account Number: {self.account_number}, Owner: {self.owner}, Email: {self.email}")
    

# Testing the system
print("Bank Account Management System:")

# Creating accounts
savings = SavingsAccount("Fatima", "fatima@email.com", 5000)
checking = CheckingAccount("Usman", "usman@email.com", 3000)

# Public method calls
savings.display_account_info()
checking.display_account_info()

# Deposit and withdraw with validation (protected methods)
savings.deposit(2000)
savings.withdraw(1000)

# Apply interest (private method inside public access)
savings.apply_interest()

# Access private balance (through public method)
print(savings.get_balance())

# Cannot access private properties directly (throws error)
# print(savings.__balance)  # Error
