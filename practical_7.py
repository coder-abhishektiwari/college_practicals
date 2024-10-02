#Practical 7: Write a program to demonstrate working with Dictionaries in python.
#creating key value pair 
print("\nMy Dictionary")
student = {
    'Name':'abhishek', 
    'Branch':'BTech CSE', 
    'Roll No.':'2207775'
    }
print(student,'\n')

#Accessing values by key
print("Value of Name: ", student['Name']) #Value of Name:  abhishek
print()

#add or update keys
student['Department'] = 'UIET'
print("New key aded: ", student)
#{'Name': 'abhishek', 'Branch': 'BTech CSE', 'Roll No.': '2207775', 'Department': 'UIET'}
student['Roll No.'] = '2207778'
print("Roll No. changed: ", student)
#{'Name': 'abhishek', 'Branch': 'BTech CSE', 'Roll No.': '2207778', 'Department': 'UIET'}
print()

#removing key:value pair using del
del student['Roll No.']
print("Dictionary after deleting Roll No. using del: ", student)

#removing key:value pair using pop
student.pop('Branch')
print("Dictionary after deleting Branch using pop: ", student)
print()

#printing all keys
print("all keys: ")
for keys in student:
    print(student[keys])

print()
#printing all values
print("all values: ")
for values in student.values():
    print(values)

print()
#iterating key:value pairs
print("Looping through key:value pair")
for keys, values in student.items():
    print(keys,values)

print()

#checking if a key is exist

print("let's check a key 'Roll No.' exist in student ")
if ('Roll No.' in student[keys]):
    print("Yeh! key found")            #true condition
else:
    print("Oh no key does'nt exist")      #false condition

print()