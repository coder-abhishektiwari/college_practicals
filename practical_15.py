#Practical 15: Write a python program to define a module and import a specific function in that 
#module to another program. 

from practical_15_module import find_max

list = [23,56,23,76,45,54,65,76,45]
print()
print(list)
print(f"maximum number for list is {find_max(list)}")
print()
