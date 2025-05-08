
# Introduction to Challenge Exercises

**COMP115** is a foundational course designed to introduce students—both general learners and future computer science majors—to the core ideas of coding.

To support deeper learning, each major chapter includes a **Challenge Exercise**. These challenges are designed to introduce key computer science concepts and practices beyond the basics.

## In this challenge, you will explore:

* **Visual Studio Code**
  Learn to use the same code editor trusted by professional developers.

* **Working with Terminal**
  Learn to work with the terminal to issue operating system commands.

* **Functions**
  Organize your code by grouping related logic into reusable blocks.

* **Automated Testing**
  Understand how programmers test their code using test cases, just like in your textbook assignments.

* **Git & GitHub**
  Use version control to manage and submit your work. You'll learn how to upload and share code using GitHub.

These challenges not only build your skills but also give you a taste of the tools and practices used in real-world software development.

## Grading for Challenge Exercises

Challenge Exercises are designed for students who wish to go **above and beyond** the general course expectations.

* These exercises are **optional**, but completing them demonstrates a deeper understanding of computer science concepts.
* **Your grade will not be negatively affected** if you choose not to complete them.
* However, to be eligible for an **A or A+** in the course, you are expected to complete at least some of the Challenge Exercises.
* Without attempting them, the highest grade you can earn will be **capped at an A−**.

---

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


## The real programmers way

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

   * So the function gives back a result rather than printing directly.


# Exercise 

The file, main.py, contains functions where the output is incorrect.  Study the comments
and re-write the function body so the program will produce the correct results.

You will also be introduced to the following ideas in professional *software development*

 - User Interface
 - Automated Testing
 - git

## User Inteface

Each of the functions represents a small part of a bigger program.  You can see the entire
program by running `python main.py` in the terminal and follow the prompt to open 
the browser.  You can check each of your function by providing different inputs.

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
