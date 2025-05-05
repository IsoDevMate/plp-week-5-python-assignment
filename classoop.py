class BankAccount:
    """A simple bank account class to demonstrate OOP concepts"""

    # Class variable (shared by all instances)
    bank_name = "Python National Bank"

    def __init__(self, account_holder, balance=0):
        """Constructor method to initialize a new bank account

        Args:
            account_holder (str): Name of the account holder
            balance (float, optional): Initial balance. Defaults to 0.
        """
        # Instance variables (unique to each instance)
        self.account_holder = account_holder
        self.balance = balance
        self.account_number = id(self)  # Using the object's ID as a simple account number

    def deposit(self, amount):
        """Deposit money into the account

        Args:
            amount (float): Amount to deposit

        Returns:
            float: New balance
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Error: Deposit amount must be positive")
        return self.balance

    def withdraw(self, amount):
        """Withdraw money from the account

        Args:
            amount (float): Amount to withdraw

        Returns:
            float: New balance
        """
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
            else:
                print("Error: Insufficient funds")
        else:
            print("Error: Withdrawal amount must be positive")
        return self.balance

    def get_balance(self):
        """Get the current balance

        Returns:
            float: Current balance
        """
        return self.balance

    def display_info(self):
        """Display account information"""
        print(f"Bank: {BankAccount.bank_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ${self.balance:.2f}")

    @classmethod
    def change_bank_name(cls, new_name):
        """Class method to change the bank name

        Args:
            new_name (str): New bank name
        """
        cls.bank_name = new_name
        print(f"Bank name changed to: {cls.bank_name}")


# Example usage
def main():
    # Create two bank account objects
    alice_account = BankAccount("Alice Smith", 1000)
    bob_account = BankAccount("Bob Johnson")

    print("===== Initial Account Information =====")
    alice_account.display_info()
    print("\n")
    bob_account.display_info()

    print("\n===== Performing Transactions =====")
    alice_account.deposit(500)
    alice_account.withdraw(200)

    bob_account.deposit(100)
    bob_account.withdraw(50)
    bob_account.withdraw(100)  # This will fail (insufficient funds)

    print("\n===== Updated Account Information =====")
    alice_account.display_info()
    print("\n")
    bob_account.display_info()

    print("\n===== Changing Bank Name =====")
    BankAccount.change_bank_name("Python International Bank")

    print("\n===== Final Account Information =====")
    alice_account.display_info()
    print("\n")
    bob_account.display_info()


if __name__ == "__main__":
    main()