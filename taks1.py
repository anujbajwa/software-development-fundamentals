
# Step 1: Account Class
class Account:
    def _init_(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(str(amount) + " deposited. New balance: " + str(self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance = self.balance - amount
            print(str(amount) + " withdrawn. New balance: " + str(self.balance))

    def display_balance(self):
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


# Step 2: Customer Class
class Customer:
    def _init_(self, name, account):
        self.name = name
        self.account = account

    def display_customer_info(self):
        print("\nCustomer Name:", self.name)
        self.account.display_balance()


# Step 3: Transaction Class
class Transaction:
    def _init_(self, account, amount, transaction_type):
        self.account = account
        self.amount = amount
        self.transaction_type = transaction_type
        self.process_transaction()

    def process_transaction(self):
        if self.transaction_type == "deposit":
            self.account.deposit(self.amount)
        elif self.transaction_type == "withdraw":
            self.account.withdraw(self.amount)
        else:
            print("Invalid transaction type")


# Step 4: Test the program

# Create account
account1 = Account(101, 100)

# Create customer
customer1 = Customer("Alice", account1)

# Display info
customer1.display_customer_info()

# Perform transactions
Transaction(account1, 50, "deposit")
Transaction(account1, 30, "withdraw")

# Final balance
customer1.display_customer_info()
 
 
 




