
import numpy as np
import matplotlib.pyplot as plt

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

"""array_1 = np.array([1,2,3])
array_2 = np.array([2,4,6])

sum = 0
for i in range(1,101):
    sum += i
print(sum)

sum2 = np.sum(np.arange(1,101))
print(sum2)

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])"""

#Plotting 10/16/23

"""x = np.linspace(0,2*np.pi, 100)
y = np.sin(x)

plt.figure()
plt.scatter(x,y, marker='*',color='green')

plt.title('Graph of sin(x)')
plt.xlabel('x values')
plt.ylabel('y values')

plt.show()"""

#another one

"""x = np.linspace(0, 2*np.pi)
y = x**2

plt.figure(figsize=(12,8))

plt.plot(x,y,color='m',linewidth=2,marker='h')

plt.title("Graph of y = x^2")
plt.xlabel("x-values")
plt.ylabel("y values")

plt.show()"""

#now subplots

"""inputs = np.linspace(-2*np.pi,2*np.pi,1000)
f = np.cos(inputs)
g = np.tan(inputs)
h = inputs**3
j = np.abs(inputs)

fig, axs = plt.subplots(2,2)

plt.suptitle("functions wow")
axs[0, 0].plot(inputs,f)
axs[0,1].plot(inputs,g)
axs[1,0].plot(inputs,h)
axs[1,1].plot(inputs,j)

plt.show()"""

