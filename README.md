## Chapter 2 Challenge: Input / Output and Writing Functions

---

### Core Concept

All computer programs follow the same basic pattern:

1.  **Gather input**
2.  **Process input**
3.  **Produce output**

---

### The Textbook Way

```python
a = int(input("first number:"))
b = int(input("second number:"))
c = int(input("third number:"))

print(a + b + c)
```

*   `input()` gathers input from the user.
*   `print()` produces the output.

This method directly interacts with the user via the terminal.

---

### The "Function" Way

```python
def add_three(a, b, c):
    return a + b + c
```

*   `a`, `b`, and `c` are variables (parameters), but we do not use `input()` inside the function.
*   `return` produces the output, but we do not use `print()` inside the function.
*   The function gets used by a different part of the program. Inside the function, we are focusing strictly on **variables, logic, and expressions**.

---

### Exercise 

The file `main.py` contains functions with incorrect output.
Study the comments and re-write the function bodies so the program will produce the correct results.

You will also be introduced to the following ideas in professional *software development*:

*   **User Interface**
*   **Automated Testing**
*   **git**

#### User Interface

Each of the functions represents a small part of a bigger program. You can see the entire program by running the following command in the terminal:

`python main.py`

This will launch a menu in your terminal. You can:
*   **Select 1-7**: To test your specific function logic directly in the terminal.
*   **Select G**: To launch a **Web Interface (Gradio)** in your browser for a more visual experience.

#### Automated Testing

You can check if your logic is 100% correct by running `pytest` in the terminal before submitting. If all tests pass (green), your logic is sound.

#### Submit

To submit your work, execute the following commands in the terminal:

```bash
git add -A
git commit -m 'submit'
git push
```
