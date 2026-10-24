# Max Profit Building Optimization

A Python-based dynamic programming solution to determine the optimal mix of properties to build within a given time limit to maximize total earnings. 

Each property takes a specific amount of time to build, and once completed, generates a fixed rate of earnings per unit of remaining operational time.

## 📋 Problem Overview

Given a total timeframe `n`, you can build three types of properties:
*   **Theatre (T):** Takes 5 time units to build, earns \$1500/unit time.
*   **Pub (P):** Takes 4 time units to build, earns \$1000/unit time.
*   **Commercial Park (C):** Takes 10 time units to build, earns \$2000/unit time.

The goal is to find the combination (mix) of buildings that yields the **maximum possible profit** within `n` time units.

## 📁 Project Structure

```text
maxprofit/
│
├── solutions.py     # Contains the core optimization algorithm (solve_max_profit)
└── test_cases.py    # Contains the test runner script and evaluation metrics
```

## 🚀 Getting Started

### Prerequisites
*   Python 3.x installed on your machine.

### Installation & Execution

1. Navigate to your project directory using the terminal/command prompt:
   ```bash
   cd "C:\Users\Raja Rajan\OneDrive\Desktop\maxprofit"
   ```

2. Run the test script to execute the solution against the preset test cases:
   ```bash
   python test_cases.py
   ```

## 🧪 Expected Output

When running the test suite, you should see the following validation output:

```text
Test Case 1 (Time Unit: 7): Earnings = \$3000 | Mix = {'T': 0, 'P': 1, 'C': 0}
Test Case 2 (Time Unit: 8): Earnings = \$4500 | Mix = {'T': 1, 'P': 0, 'C': 0}
Test Case 3 (Time Unit: 13): Earnings = \$16500 | Mix = {'T': 2, 'P': 0, 'C': 0}

All test cases passed successfully!
```
