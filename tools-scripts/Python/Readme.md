# 🐍 Python Scripts

Beginner Python scripts written as part of learning
programming fundamentals applied to cybersecurity.

---

## Scripts

### 1. hayzed.py — Python Fundamentals Practice
Basic Python concepts including string manipulation,
lists, dictionaries, tuples, loops, and f-strings.

**Concepts Covered:**
- String indexing and methods (upper, lower)
- F-strings and concatenation
- Arithmetic operations
- Lists — insert, remove, iteration
- Dictionaries — CRUD operations, iteration
- Tuples — indexing and iteration

---

### 2. password_checker.py — Password Validation Loop
A simple password checker using a while loop that
grants or denies access based on user input.

**Concepts Covered:**
- While loops
- User input handling
- Conditional statements (if/else)
- Access control logic

```python
while password != "correct_password":
    password = input("What is your password?")
    if password == "correct_password":
        print("Access approved")
    else:
        print("Access denied, please try again")
```
----

### 3. guess_the_game.py — Number Guessing Game
A number guessing game using random number generation
with limited attempts.

**Concepts Covered:**
-	Importing modules (random)
-	Random number generation
-	While loops with counters
-	Conditional branching
- User input validation

 ```python
import random
secret = random.randint(1, 20)
attempts = 5
```

