# Problem 8.35
class Stack(object):
# Initializes a list to be used.
    def __init__(self):
        self.list = []

# Similar to __str__ but instead when s is inseted it will just print the list
    def __repr__(self):
        return str(self.list)

# Overloaded operator to use len() function on the list.
    def __len__(self):
        return len(self.list)
    
# Take an item as input and push it on top of the stack
    def push(self, item):
        self.list.append(item)

# Remove and return the item at the top of the stack
    def pop(self):
        print(self.list.pop())

# Return True if the stack is empty, False otherwise
    def isEmpty(self):
        if not self.container:
            print(True)
        else:
            print(False)


# Problem 8.40
class BankAccount(object):
# Initializes the account and if an ammount is less than 0 then it raises and exception
    def __init__(self, account = 0):
        if self.account < 0:
            raise ValueError("Illegal balance")
        self.account = account

# Subtracts the amount wanted from the bank account and checks if the amount withdrawn is more than the cash in the account.
    def withdraw(self, amount):
        if amount > self.account:
            raise ValueError("Overdraft")
        self.account -= amount

# Adds the amount of money that is wanted to the account. Raises an error if a negative number is deposited. 
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Negative Deposit")
        self.account += amount

# Prints out the balance when the function is called on.
    def balance(self):
        print(self.account)
        
    


