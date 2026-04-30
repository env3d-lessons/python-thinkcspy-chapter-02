# Chapter 2 Challenge: Input / Output and Writing Functions

## Core Concept

All computer programs follow the same basic pattern:

1. **Gather input**
2. **Process input**
3. **Produce output**


## The Textbook Way

```python
a = int(input("first number:"))
b = int(input("second number:"))
c = int(input("third number:"))

print(a + b + c)
```

* `input()` gathers input from the user.
* `print()` produces the output.

This method directly interacts with the user.


## The "Function" Way

```python
def sum(a, b, c):
    return a + b + c
```

* `a`, `b`, and `c` are variables, but we do not use input()
* `return` produces the output, but we do not use print()
* The function gets used by a different part of the program, but within the function we are still dealing with the same concepts: variables and expressions.


# Exercise 

The file `main.py` contains functions with incorrect output.
Study the comments and re-write the function body so the program will produce the correct results.

You will also be introduced to the following ideas in professional *software development*

 - User Interface
 - Automated Testing
 - git

## User Interface

Each of the functions represents a small part of a bigger program.  You can see the entire
program by running `gradio main.py` in the terminal and follow the prompt to open 
the browser.  You can check each of your functions by providing different inputs.

## Automated Testing

You can check if you have gotten everything correct by running `pytest` in the terminal
before submitting.

## Submit

To submit, execute the following commands in the terminal:

```bash
git add -A
git commit -m 'submit'
git push
```
