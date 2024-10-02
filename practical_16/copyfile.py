#Practical 16: Write a script named copyfile.py. This script should prompt the user for the names of two 
#text files. The contents of the first file should be input and written to the second file. 

def copycontent(r_file, w_file):
    with open(r_file, 'r') as file:
        content = file.read()

    with open(w_file, 'w') as file:
        file.write(content)
        print("Content succesfully copied.")


#maintext
print()
r_file = input("Enter file name (with extention) from you want to copy: ")
w_file = input("Enter file name (with extention) where you want to write: ")
copycontent(r_file, w_file)

print()