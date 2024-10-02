#Task 5: Write a program to create, append, and remove lists in python.
print()
#list creation
print("#Creating a list--------- ")
list = [1,2,3,4]
print("My list: ",list)   #My list:  [1, 2, 3, 4]

print()

#append list
print("Append 5 on list")
list.append(5)  
print(list)          #Append 5 on list

print()

#extend list
print("Extend list with [6,7,8]")
list.extend([6,7,8])
print(list)         #[1, 2, 3, 4, 5, 6, 7, 8]

print()

#pop from list
print("#Popping an element---------")
print("last element popped", list.pop())     
print(list)         #[1, 2, 3, 4, 5, 6, 7]
print("element at index 2 popped: ", list.pop(2))  
print(list)         #[1, 2, 4, 5, 6, 7]

print()

#insert element to list
print("#inserting an element---------")
print("23 inserted at 4th index")
list.insert(4,23)
print(list)        #[1, 2, 4, 5, 23, 6, 7]

print()

#deleting element form list
print("#Deleting an element---------")
del list[4]
print("deleted from 4th index ")
print(list)       #[1, 2, 4, 5, 6, 7]


print()