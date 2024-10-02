# Creating strings using different methods
print()
# 1. Single quotes
str1 = 'Hello'
print("String using single quotes:", str1)  # Output: String using single quotes: Hello

# 2. Double quotes
str2 = "World"
print("String using double quotes:", str2)  # Output: String using double quotes: World

# 3. Multi-line string using triple quotes
str3 = """This is a 
multi-line string"""
print("String using triple quotes:", str3)  
# Output: 
# String using triple quotes: This is a 
# multi-line string

# Concatenating strings
concat_str = str1 + " " + str2
print("\nConcatenated string:", concat_str)  # Output: Concatenated string: Hello World

# Accessing sub-string (positive indexing)
sub_str_pos = concat_str[0:5]
print("Sub-string from the concatenated string (positive indexing):", sub_str_pos)  
# Output: Sub-string from the concatenated string (positive indexing): Hello

# Accessing sub-string (negative indexing)
sub_str_neg = concat_str[-5:]
print("Sub-string from the concatenated string (negative indexing):", sub_str_neg)  
# Output: Sub-string from the concatenated string (negative indexing): World
print()