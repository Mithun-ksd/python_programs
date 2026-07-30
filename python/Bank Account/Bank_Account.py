class BankAccount:
    def __init__(self, balance=0):  # Correct constructor
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient Balance")
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance

class SavingAccount(BankAccount):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = (self.balance * self.interest_rate / 100)
        self.balance += interest

account_type = input("Enter account type (b for Bank Account and s for Saving Account): ").lower()
if account_type == 'b':
    account = BankAccount()
elif account_type == 's':
    interest_rate = float(input("Enter Interest Rate: "))  # Prompt for interest rate immediately
    account = SavingAccount(0, interest_rate)  # Initialize with 0 balance

while True:
    print("\nBank Account Menu")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Get Balance")
    print("4. Quit")
    choice = int(input("Enter your choice (1-4): "))
    if choice == 1:
        amount = float(input("Enter Amount To Deposit: "))
        account.deposit(amount)
        if isinstance(account, SavingAccount):
            account.add_interest()  # Add interest after deposit
        print("\nDeposit Successful")
    elif choice == 2:
        amount = float(input("Enter Amount To Withdraw: "))
        account.withdraw(amount)
        print("Withdraw Successful")
    elif choice == 3:
        print("Balance:", account.get_balance())
    elif choice == 4:
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid Choice")
