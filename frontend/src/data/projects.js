export const projectsManifest = {
  "cli-banking-app": {
    id: "cli-banking-app",
    title: "Build a CLI Banking App",
    description: "Learn object-oriented programming by building a command-line banking application with multiple files.",
    difficulty: "Intermediate",
    xp: 500,
    language: "python",
    entrypoint: "main.py",
    files: {
      "main.py": "from bank import BankAccount\n\ndef main():\n    print('Welcome to PyBank!')\n    account = BankAccount('Alice', 100)\n    account.deposit(50)\n    account.withdraw(20)\n    print(f'Final Balance: ${account.get_balance()}')\n\nif __name__ == '__main__':\n    main()\n",
      "bank.py": "class BankAccount:\n    def __init__(self, owner, balance=0):\n        self.owner = owner\n        self.balance = balance\n\n    def deposit(self, amount):\n        if amount > 0:\n            self.balance += amount\n            print(f'Deposited ${amount}.')\n\n    def withdraw(self, amount):\n        if 0 < amount <= self.balance:\n            self.balance -= amount\n            print(f'Withdrew ${amount}.')\n        else:\n            print('Insufficient funds.')\n\n    def get_balance(self):\n        return self.balance\n",
      "README.md": "# CLI Banking App\n\nIn this guided project, you will write a complete Python application spread across two files:\n\n1. **`bank.py`**: Contains the `BankAccount` class.\n2. **`main.py`**: The entrypoint that imports the class and runs the app.\n\nTry running the project now to see how it works!"
    }
  }
};
