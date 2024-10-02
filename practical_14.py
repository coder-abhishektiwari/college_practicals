# Practical 14: Write a python program to define a module to find Fibonacci Numbers and import the 
# module to another program. 
import practical_14_module as f

print()
num = 10
print(f"fibonacci sequece for {num} is: ")
for i in range(num):
    print(f.fibonacci(i), end=" ")

print("\n")