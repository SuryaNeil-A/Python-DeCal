"""
HW 4: Debugging and Lists

Q1 Debugging

Throughout this homework, whenever you encounter an error, we would like you to 
explain in a comment what it was and how you fixed it. You can write all these errors 
at any place in the file.



Q2 List Slicing and Striding:

Part 1: Create a variable (name it anything you want but make it descriptive!) that 
is assigned to a list with the numbers 0 to 50. You should not have to write each 
number manually.
"""

numberList = []

for i in range(51):
    numberList.append(i)

"""
Part 2: Create a function that takes in a list and squares each element in the list.
"""

def squareList(list1):
    for i in range(len(list1)):
        list1[i] = (list1[i])**2
    return list1

"""
Part 3: You are given two lists: listA and listB. listA contains the integers 1 through 
10 while listB contains the integers 20 through 30. Return a single, new list containing
only the odd integers of both lists in sorted order.
"""

listA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listB = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

def totalOddList(list1, list2):
    totals = list1 + list2
    odd_totals = []
    for i in range(len(totals)):
        if totals[i] % 2 != 0:
            odd_totals.append(totals[i])
    return odd_totals

#somehow I had a lot of trouble with this problem, kept getting an index out of range error because I was removing items from the totals list (I didn't have odd_totals created)
#so the length of my list kept changing with each iteration of the for loop until it was out of the range...felt quite silly after I figured that out

"""
Q3 2D Lists
Using nested for loops, create and print a 5x5 2D list with the odd numbers from 1 to 25.
"""

#the odd numbers from 1 to 25 do not make a 5x5 matrix...
#[[1,3,5,7,9],[11,13,15,17,19],[21,23,25]]
#just going to do numbers 1 to 25 instead since I imagine that was intended

#[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

# Q3 PART 1 CODE HERE
list_2D = []
#Hint: Outer loop will manage row indices, inner loop will manage column indices (or vice 
# versa).

row_start = 1
for i in range(5):
    row_end = row_start + 5
    row = []
    for k in range(row_start,row_end):
        row.append(k)
    row_start = row_end
    list_2D.append(row)

print(list_2D)

#had some errors getting the row start and row end properly but it worked out pretty quickly

"""
Now with your completed list_2D, replace all multiples of 3 with '?' character and print
the resulting 2D list.
"""

# Q3 PART 2 CODE HERE

def goodbyeThree(list1):
    for i in range(len(list1)):
        row_k = list1[i]
        for k in range(len(row_k)):
            if row_k[k] % 3 == 0:
                row_k[k] = "?"
        list1[i] = row_k
    return list1

print(goodbyeThree(list_2D))

"""
Q4 More List Practice

Write a function that takes in a list and returns a copy of that list with duplicate 
values removed.
"""

def remove_duplicates(list1):
    duplicatesOut = []
    for i in range(len(list1)):
        if list1[i] not in duplicatesOut:
            duplicatesOut.append(list1[i])
    return duplicatesOut


#It may be helpful to create an array to test your function.

test1 = [40, 10, 80, 50, 20, 60, 30]
test2 = [10,20,30,30,30,30,30,40,10,20,80,69,420]
test3 = [1,1,1,1,1,1,1,1,1,1,1,10]

print(remove_duplicates(test1))
print(remove_duplicates(test2))
print(remove_duplicates(test3))