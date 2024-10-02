#practical 6: Write a program to demonstrate working with tuples in python.
print()
print("#Creating new tupple")
tupple = (1,2,3,4)
print("My tupple: ", tupple)   #(1, 2, 3, 4)
print()

print("#accessing element from tupple")
print("value at index 3 is ", tupple[3])   #4
print()

#tupple slicing
print("Slicing tupple [3:6]: ", tupple[1:3])   #(2, 3)
print()

#unpacking
a,b,c,d = tupple
print("unpacked_tupple : ", a,b,c,d)    #1 2 3 4

#Concatenation
concatenated_tupple = tupple + ('a','b','c','d')
print("Concatenated tupple: ", concatenated_tupple)  #(1, 2, 3, 4, 'a', 'b', 'c', 'd')
print()

#check element is exist in tupple or not using Membership operator
print("let's check 4 in exist in my concatenated_tupple ")
if (4 in concatenated_tupple):
    print("Yes 4 is found in concatednated_tupple")            #true condition
else:
    print("No 4 is not found")                                 #false condition



print()