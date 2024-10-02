#Practical 12: Write a python program to find factorial of a number using Recursion. 

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

#main      
number = 5
print()
print(f"factorial of {number} is {factorial(number)}")
print()