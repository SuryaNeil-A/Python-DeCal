
# Let's start with an empty list:

"""fruitList = []"""

#Next, let's add the following fruits to the list: 'apple', 'banana', and 'kiwi'.

"""fruitList.append("apple")
fruitList.append("banana")
fruitList.append("kiwi")

print(fruitList)"""

#Print the second element in the list (which index would that be?)

"""print(fruitList[1])"""

#Now add another 'banana' to the end of the list, and replace the first one with 'cherry'.
#See if you can do this without actually typing out 'banana' in your code.

"""fruitList.append(fruitList[1])
fruitList[1] = "cherry"
print(fruitList)"""

#Sort the list in alphabetical order (see built in methods)
"""
fruitList.sort()
print(fruitList)"""

#Print the length of fruits

"""print(len(fruitList))"""




#SECOND DEMO

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Slice the list to include only the integers from 2 to 9 (inclusive) and print its length.

"""nums = nums[1:9]

print(len(nums))"""

#Now create a new list with all of the odd numbers in nums in decreasing order

numsOddReverse = nums[8::-2]

print(numsOddReverse)

# Creating two sample lists with different types of elements

numsOdd = nums[::2]
numsEven = nums[1::2]

# Concatenating lists using the '+' operator

numsSum = numsOdd + numsEven

# Printing the concatenated list

print(numsSum)

# Creating another sample list

fruits = ["apple", "banana", "cherry"]

vegetables = ["broccoli", "cucumber", "carrot"]

# Concatenating lists using the 'extend()' method

fruits.extend(vegetables)

# Printing the updated list1 after concatenation using 'extend()'

print(fruits)