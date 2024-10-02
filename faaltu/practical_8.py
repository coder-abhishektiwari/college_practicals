#Practical 8: Write a python program to find largest of three numbers.

list = [23,98,56]
print("\nmy list: ", list)
max = 0  #initialized max with 0
iteration = 0
for i in range(len(list)):
    if list[i] > max:
        max = list[i]   #make list item max if the list item is greater than previous max
        iteration = iteration + 1
    else: 
        max = max       #otherwise max remains max
        iteration = iteration + 1

print(iteration, "iteration performed in which", max, "is found maximum number.")
print()