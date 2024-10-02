#Practical 11: Write a Python script that prints prime numbers less than 20. 
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Print prime numbers less than 20
print()
print("Prime numbers less than 20 are:")
for number in range(2, 20):
    if is_prime(number):
        print(number, end=" ")

print("\n")