'''Practical 10: Write a Python program to construct the following pattern, using a nested for 
loop 
*
* 
* * 
* * * 
* * * * 
* * * 
* * 
* 
*
'''

n = 4  # The middle row count (max stars)

# First part: increasing stars
print("\n*")

for i in range(1, n + 1):
    print("* " * i)

# Second part: decreasing stars
for i in range(n - 1, 0, -1):
    print("* " * i)

print("*\n")
