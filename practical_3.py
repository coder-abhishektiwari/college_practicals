#Practical 3: Program to create, concatenate and print a string and accessing sub-string froma given string.


print("\n")

print("#Three methods to create a string-------\n")         ##Three methods to create a string-------
#method 1
method_1 = "\"Abhishek\""
print("Method 1- (double qoutes method): ", method_1)       #Method 1- (double qoutes method):  "Abhishek"

#method 2
method_2 = '\'Tiwari\''
print("Method 2- (single qoutes method): ", method_2)       #Method 2- (single qoutes method):  'Tiwari'

#method 3
method_3 = """\"""This is multi-line string
Line 2 of multiline string\""" """
print("Method 3- (multiline string method): ", method_3)    #Method 3- (multiline string method):  """This is multi-line string
                                                            #Line 2 of multiline string"""
print()

print("\n#String Operations--------- \n")                   ##String Operations---------

string_1 = "Hawlet"
string_2 = "Packered"
print("String 1: ", string_1)                               #String 1:  Hawlet
print("String 2: ", string_2)                               #String 2:  Packered
print()

#concatenation
concatenated = string_1 + " " + string_2                    
print("Concatednated String: ",concatenated)                #Concatednated String:  Hawlet Packered

#accesing substring
substring = concatenated[0:5]
print("Substring (first 5 characters): ", substring)        #Substring (first 5 characters):  Hawle

#using nagative indexing
substring_nagative = concatenated[-5:]
print("Substring negative (last 5 characters): ", substring_nagative)  #Substring negative (last 5 characters):  kered


print()