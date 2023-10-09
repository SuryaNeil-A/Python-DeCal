
import numpy as np

#If Statements 9/18/23

"""value = int(input("Enter a number:"))

if value == 10:
    print(value, "is equal to 10.")
elif value > 10:
    print(value, "is greater than 10.")
else:
    print(value, "is less than than 10.")"""

#For Loops 9/18/23

"""for i in range(0,26):
    print(i)"""

"""for i in range(25,-1,-3):
    print(i)"""

"""import math

i = 25
while i >= 0:
    print(i)
    i -= 1

def power(input, power):
    output = input*input
    for i in range(2,power):
        output *= input
    output

def findMin(x,y):
    if x < y:
        return x
    elif x > y:
        return y
    else:
        return print(str(x) + " is equal to " + str(y))
    
def quadraticFormula(a,b,c):
    rootPlus = (-b+math.sqrt(b**2-4*a*c))/(2*a)
    rootMinus = (-b-math.sqrt(b**2-4*a*c))/(2*a)
    return rootPlus, rootMinus"""

#Lists 9/25/23

#Numpy Arrays 10/4/23

array_1 = np.array([1,2,3])
array_2 = np.array([2,4,6])

sum = 0
for i in range(1,101):
    sum += i
print(sum)

sum2 = np.sum(np.arange(1,101))
print(sum2)

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])