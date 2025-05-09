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

This method directly interacts with the user but has some limitations.


## The Professional Way

```python
def sum(a, b, c):
    return a + b + c

# This is where we actually invoke the function to execute
print(sum(1, 2, 3))
```

* `a`, `b`, and `c` are inputs to the function.
* `return` produces the output.
* We execute the function from the terminal, by typing the command `python main.py`



## Why Use Functions?

* The **textbook way** only allows **one program per file**.
* With functions, we can have many units of computation per file.


## Converting Textbook Code to a Function

1. **Give your function a name**:

   ```python
   def my_function(...):
   ```

2. **Replace input() with parameters**:

   * Move the inputs into the function arguments.

3. **Indent the logic**:

   * Write the processing steps inside the function body.

4. **Replace `print()` with `return`**:

   * This allows the function to return a result that can be used elsewhere, rather than printing directly.


# Exercise 

The file `main.py` contains functions with incorrect output.
Study the comments and re-write the function body so the program will produce the correct results.

You will also be introduced to the following ideas in professional *software development*

 - User Interface
 - Automated Testing
 - git

## User Interface

Each of the functions represents a small part of a bigger program.  You can see the entire
program by running `python main.py` in the terminal and follow the prompt to open 
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
