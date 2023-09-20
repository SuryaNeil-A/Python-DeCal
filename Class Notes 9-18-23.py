#If Statements

"""value = int(input("Enter a number:"))

if value == 10:
    print(value, "is equal to 10.")
elif value > 10:
    print(value, "is greater than 10.")
else:
    print(value, "is less than than 10.")"""

#For Loops

"""for i in range(0,26):
    print(i)"""

"""for i in range(25,-1,-3):
    print(i)"""

i = 25
while i >= 0:
    print(i)
    i -= 1

def power(input, power):
    input = int(input("enter input:"))
    power = int(input("enter power:"))
    for i in range(0,power + 1):
        output *= input
    print(output)
