
#Homework 3: Data Types, Functions, Conditionals, and Loops



""" ### Problem 1: Power of a Number:
Write a function to compute the value of x raised to the power y (x^y) 
without using the built-in pow or ** operator.
"""

def power(input, power):
   output = 1 #defining the output to be 1 to initialize the function, also makes sure input**0 = 1
   for i in range(power):
     output = output*input
   return output

#doesn't work for non-integer or negative exponents, perhaps could add some extra logic/cases for that later down the line


"""### Problem 2: Minimum and Maximum
Write a function that takes a list of numbers as input and returns the 
minimum and maximum values in the list as a tuple.
"""

def minandmax(list1):
   list1.sort()
   min = list1[0] #after sorting the min and max will clearly be the first and last items
   max = list1[-1]
   return (min, max)

#I'm not sure if using list1.sort() is cheating here (did you want us to iterate through the list and find the min and max?), but it works

"""### Problem 3: Check Leap Year
Write a function that takes a year as input and returns True if it's a 
leap year, and False otherwise. A leap year is divisible by 4 but not divisible 
by 100 unless it is also divisible by 400.
"""

def leapYear(year):
   if year % 4 == 0 and (not(year % 100 == 0) or year % 400 == 0):
      #maybe it is a little unclear to put it all in one line, but it is false as long as the year is divisible by 100
      #but if it is also divisible by 400, the 100 condition doesn't matter (hence the or statement)
      return True
   else:
      return False

"""### Problem 4: Calculate BMI (Body Mass Index):
Write a function that takes a person's weight (in kilograms) and height 
(in meters) as input and returns their BMI.
"""

def calculate_bmi(weight, height):
    return weight / (height**2)

"""### Problem 5: Rotating Digits
Implement a function called rotate_digits that takes an integer n as input and 
rotates its digits to the right by one position. For example, given the input 12345, 
the function should return 51234. You may *not* convert the input to a string but 
you can use properties of a string in your answer.

**Hint:** Use modulus (%) and floor division (//). For example, 12345 % 10 = 5 and 
12345 // 10 = 1234
"""

def rotate_digits(digits):
   leading_digit = digits % 10
   remaining_numbers = digits // 10
   digitsLength = int(len(str(remaining_numbers))) #This also might be cheating, but I'm not coverting the input to a string (just the remaining part to get the amount of zeros on the leading digit)
   return leading_digit*(10**digitsLength) + remaining_numbers

### For questions #6-10, write the solution with a for-loop and a while-loop.
# If it is not possible to write it with a for-loop or while-loop, detail why.

"""Problem 6: Maximum
Given a list of numbers, find the maximum number. Use a for-loop and a while-loop.
"""

list1 = [1, 3, 5, 7, 4, 6]

def findMax_for(list1):
   max = list1[0]
   for i in range(len(list1)):
      if list1[i] > max:
         max = list1[i]
   return max

def findMax_while(list1):
   max = list1[0]
   i = 0
   while i < len(list1):
      if list1[i] > max:
         max = list1[i]
      i += 1
   return max

"""Problem 7: Minimum
Given a list of numbers, find the minimum number. Use a for-loop and a while-loop.
"""

list1 = [1, 3, 5, 7, 4, 6]

def findMin_for(list1):
   min = list1[0]
   for i in range(len(list1)):
      if list1[i] < min:
         min = list1[i]
   return min

def findMin_while(list1):
   min = list1[0]
   i = 0
   while i < len(list1):
      if list1[i] < min:
         min = list1[i]
      i += 1
   return min

"""Problem 8: The Product
Given a list of numbers, calculate the product of all the numbers.
"""

def product(numList):
   totalProduct = numList[0] #starts with the first element
   for i in range(len(numList)):
      totalProduct *= numList[i] #multiplies all the following elements
   return totalProduct

def product_while(numList):
   i = 1
   totalProduct = numList[0]
   while i < len(numList):
      totalProduct *= numList[i]
      i += 1
   return totalProduct

"""Problem 9: Vowels
Given a string, count the number of vowels in it using a for loop.

"""

string1 = "pneumonoultramicroscopicsilicovolcanoconiosis"

def countVowels(str):
   vowelCount = 0
   for i in range(len(str)):
      if str[i] == "a" or str[i] == "e" or str[i] == "i" or str[i] == "o" or str[i] == "u": #is there a better way to write all of these conditions?
         vowelCount += 1
   return vowelCount

"""Problem 10: Sum of Digits (Digital Root):
Given an integer, return the sum of its digits (also known as the digital 
root) For example, if the input is 12345, the output should be 15 
(1 + 2 + 3 + 4 + 5).

**Hint:** Refer to #5!

"""

# For this question, it is harder to do it as a for-loop as there is no 
# way of keeping track of all the digits.
# So, only a while-loop solution is necessary.

def sumDigits(num):
   i = 0
   sum = 0
   number = num #had to make another variable since we're changing the value of num, for some reason without this change the while loop would break without getting the last number
   while i <= int(len(str(num))):
      nthDigit = number % 10
      sum += nthDigit
      number = (number - nthDigit)//10
      i +=1
   return sum