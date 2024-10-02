#Practical 8: Write a python program to find largest of three numbers.

def find_max(a, b, c):
    if (a>=b) & (a>=c):
        return a
    elif (b>=a) & (b>=c):
        return b
    else:
        return c


#main program
a = 200
b = 300
c = 150
print()
print("Values: ",a,b,c)
print(f"{find_max(a,b,c)} is largest")
print()
