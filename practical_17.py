# Program 17: Write a program that inputs a text file. The program should print all of the unique 
# words in the file in alphabetical order. 
print()
def print_order(text_file):
    with open(text_file, 'r') as file:
        content = file.read()
        print("File content: \n", content)
        seen = set()
        for char in content:
            if char.isalpha():
                seen.add(char)

        sorted_seen = sorted(seen)

        print("\nOrdered alphabets: ")
        for char in sorted_seen:
            print(char, end=" ")


print_order('text.txt')

print("\n")