from abc import ABC, abstractmethod

class BankAccount(ABC):
    """Abstract base class defining core banking operations"""
    
    @abstractmethod
    def deposit(self, amount: float) -> None:
        """Abstract method for depositing money"""
        pass
    
    @abstractmethod
    def withdraw(self, amount: float) -> None:
        """Abstract method for withdrawing money"""
        pass
    
    @abstractmethod
    def check_balance(self) -> float:
        """Abstract method for checking account balance"""
        pass

class CurrentAccount(BankAccount):
    """Concrete implementation of a current (checking) account"""
    
    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        self.account_holder = account_holder
        self._balance = initial_balance
        self._overdraft_limit = -1000.0
    
    def deposit(self, amount: float) -> None:
        if amount <= 0:
            print("\n❌ Error: Deposit amount must be positive")
            return
        self._balance += amount
        print(f"\n✅ Deposited £{amount:.2f}. New balance: £{self._balance:.2f}")
    
    def withdraw(self, amount: float) -> None:
        if self._balance - amount < self._overdraft_limit:
            print(f"\n❌ Error: Insufficient funds. Overdraft limit is £{abs(self._overdraft_limit)}")
            return
        if amount <= 0:
            print("\n❌ Error: Withdrawal amount must be positive")
            return
        self._balance -= amount
        print(f"\n✅ Withdrawn £{amount:.2f}. New balance: £{self._balance:.2f}")
    
    def check_balance(self) -> float:
        print(f"\n💰 Current balance for {self.account_holder}: £{self._balance:.2f}")
        return self._balance

def display_menu():
    print("\n=== PyBank Menu ===")
    print("1. Check Balance")
    print("2. Make Deposit")
    print("3. Make Withdrawal")
    print("4. Exit")
    print("=================")

def get_amount(operation: str) -> float:
    while True:
        try:
            amount = float(input(f"\nEnter amount to {operation}: £"))
            return amount
        except ValueError:
            print("❌ Please enter a valid number")

if __name__ == "__main__":
    print("\n🏦 Welcome to PyBank! 🏦")
    print("=" * 30)
    
    name = input("\nEnter account holder name: ")
    account = CurrentAccount(name, 1000.0)  # Start with £1000 balance
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            account.check_balance()
        elif choice == '2':
            amount = get_amount("deposit")
            account.deposit(amount)
        elif choice == '3':
            amount = get_amount("withdraw")
            account.withdraw(amount)
        elif choice == '4':
            print("\n👋 Thank you for using PyBank! Goodbye!")
            break
        else:
            print("\n❌ Invalid choice. Please try again.")
        
        input("\nPress Enter to continue...")