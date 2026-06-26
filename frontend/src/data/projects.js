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
  },
  "interactive-todo-list": {
    id: "interactive-todo-list",
    title: "Interactive To-Do List",
    description: "Build an interactive Javascript to-do list using arrays and modular functions.",
    difficulty: "Beginner",
    xp: 250,
    language: "javascript",
    entrypoint: "main.js",
    files: {
      "main.js": "const { addTask, completeTask, viewTasks } = require('./todo.js');\n\naddTask('Learn Javascript');\naddTask('Build a project');\ncompleteTask(0);\n\nconsole.log('Current Tasks:');\nconsole.log(viewTasks());\n",
      "todo.js": "let tasks = [];\n\nfunction addTask(name) {\n    tasks.push({ name: name, completed: false });\n}\n\nfunction completeTask(index) {\n    if (tasks[index]) {\n        tasks[index].completed = true;\n    }\n}\n\nfunction viewTasks() {\n    return tasks;\n}\n\nmodule.exports = { addTask, completeTask, viewTasks };\n",
      "README.md": "# Interactive To-Do List\n\nIn this Guided Project, you will learn how to write modular JavaScript by separating your logic from your entrypoint."
    }
  },
  "data-analysis-pipeline": {
    id: "data-analysis-pipeline",
    title: "Data Analysis Pipeline",
    description: "Analyze sales data using Python, filtering and aggregating results across multiple scripts.",
    difficulty: "Advanced",
    xp: 750,
    language: "python",
    entrypoint: "main.py",
    files: {
      "main.py": "from analyzer import calculate_total_sales\n\nsales_data = [\n    {'item': 'Laptop', 'price': 1000},\n    {'item': 'Mouse', 'price': 50},\n    {'item': 'Keyboard', 'price': 100}\n]\n\ntotal = calculate_total_sales(sales_data)\nprint(f'Total Sales Revenue: ${total}')\n",
      "analyzer.py": "def calculate_total_sales(data):\n    total = 0\n    for entry in data:\n        total += entry.get('price', 0)\n    return total\n",
      "README.md": "# Data Analysis Pipeline\n\nLearn how data engineers modularize their scripts for cleaner, more testable analysis pipelines."
    }
  }
};
