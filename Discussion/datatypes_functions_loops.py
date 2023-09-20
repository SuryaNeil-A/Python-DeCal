# -*- coding: utf-8 -*-
"""datatypes_functions_loops.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PIizne-6qpr8q7Hygx5aKN56IxN5LhGl

## Comprehension Problems

### Problem 1: Data Types (15 Points)
Instructions: Fill in the blanks. (Ex. a = 5, so the data type of a is an int). If you're not sure, you can use the type() function to output the type of the variable.
"""

variable1 = "Surprised Pikachu is the best meme." # Data type of variable1: string

variable2 = 5 # Data type of variable2: integer

variable3 = 1.29 # Data type of variable3: float

def g():
    print("beep beep")
    return True

variable4 = g # Data type of variable4: variable

variable5 = g() # Data type of variable5: function

variable6 = [1,2,3] # Data type of variable6: list

variable7 = (1,3,5) # Data type of variable7: 

variable8 = {"brand": "Ford", "model": "Mustang", "year": 1964} # Data type of variable8: 

"""### Problem 2: Using /, //, % (5 points)

Observe what happens in each of these scenarios. Recall the differences between normal, floor, and modulo division and describe those differences in the markdown cell below.
"""

5/2 # normal division

4//3 # floor division

459 % 4 # modulo division

"""Describe the operators above"""

# Normal division does normal division, including decimals. 
# Floor division does the same but takes the floor of the output (always rounds down)
# Modulo division returns the remainder after division (e.g. 5 % 2 = 1)

"""### Problem 3: Hanging by a String (3 points)

In the following problem use string indexing to turn the words below into a new word that is part of the original word or a modified version of it. Example: Strongest $\rightarrow$ Strong
"""

word_1 = "Fastest"
print(word_1[3:])
word_2 = "Outside" #two options are acceptable here, try both if you want!
print(word_2[0:3])
word_3 = "racecar"
print(word_3[0:4])

"""### Problem 4: Palindromes (2 points)

Use string indexing to reverse the palindrome, then use the `print()` function to print the string out to verify that it is in fact a palindrome.
"""

palindrome_1 = "tattarrattat"
##CODE HERE##
palindrome_2 = "madam"
##CODE HERE##

"""## Application Problems

### Problem 1 (5 points)

Take your favorite equation (or find one on the internet) and turn it into a function (like we did with the volume of a sphere).
"""

## INSERT CODE ##

"""### Problem 2 (5 points)

Write a function last_digit(num) which returns the last digit of a number as a string. Tip: To convert an int or a float to a string, use the str() function. If you want to convert a string to an int or a float, use int() or float() respectively.
"""

def last_digit(num):
    """ Returns last digit of a number as a string.

    >>> last_digit(2019):
    9
    >>> last_digit(40023948):
    8
    """
    return ## INSERT CODE ##

"""### Problem 3 (10 points)

For this problem, it would be helpful to know some functions that are already built-in to Python. In particular, min() and max(). Run the following code (and try it yourself) to see what they do, and then complete the function two_of_three. This one is a bit tricky so dont feel bad if you're stuck for a while!
"""

min(3, 4, 5), min(-5, 9, -20)

max(3, 4, 5), max(-5, 9, -20)

def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return ## INSERT CODE ##

"""## Coding Hygiene

As programmers we do need to practice good coding. What does that entail you might ask?

As good programmers we should abide by the following rules of thumb:

1. Use semi descriptive variables. DO NOT represent every variable as a single letter. This leads to ambiguity and makes it very difficult to understand/read your code when you come back to it, it also makes it difficult on us when we grade your homework. Examples: use temp instead of t, radius instead of r, etc...

2. Leave comments as frequently as needed to make it easy to understand for people reading, especially in your functions. We recommend a docstring under the name of your functions describing what it does. Docstring is a comment using triple quotes of the form ('''________''')

3. Stay consistent with your line spacing, try to make it as comprehensible as possible. Cramped up code with no spacing inbetween is not very pleasing to the eye and can get overwhelming

### Pretty Me Up (5 points)

Fix the given code so that it adheres to the coding hygiene guidelines above
"""

def v(r):
    return 4/3 * 3.14 * r**3