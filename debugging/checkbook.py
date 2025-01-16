class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit a specified amount into the checkbook balance.

        Parameters:
        amount (float): The amount to deposit.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the checkbook balance.

        Parameters:
        amount (float): The amount to withdraw.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """Print the current balance of the checkbook."""
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()

        if action == 'exit':
            break
        elif action == 'deposit':
            while True:
                try:
                    amount = float(input("Enter the amount to deposit: $"))
                    if amount <= 0:
                        print("Amount must be greater than zero. Please try again.")
                        continue
                    cb.deposit(amount)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number for the deposit amount.")
        elif action == 'withdraw':
            while True:
                try:
                    amount = float(input("Enter the amount to withdraw: $"))
                    if amount <= 0:
                        print("Amount must be greater than zero. Please try again.")
                        continue
                    cb.withdraw(amount)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number for the withdrawal amount.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
