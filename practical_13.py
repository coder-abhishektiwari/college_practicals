'''Practical 13: Write a program that accepts the lengths of three sides of a triangle as inputs. 
The program output should indicate whether or not the triangle is a right triangle 
(Recall from the Pythagorean Theorem that in a right triangle, the square of one 
side equals the sum of the squares of the other two sides). '''

def is_right_traingle(a, b, c):
    sides = sorted([a,b,c])

    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    else:
        return False


#main  
a = 3
b = 5
c = 4
print()
if is_right_traingle(a,b,c):
    print(f"The traingle with sides {a ,b, c} is right triangle.")
else:
    print(f"The traingle with sides {a ,b, c} is not a right triangle.")

print()