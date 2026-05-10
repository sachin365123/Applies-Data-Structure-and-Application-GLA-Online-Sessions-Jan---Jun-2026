# Write a program to demonstrate various operations (length, copy, append, 
# compare) on strings. 

# Python program to demonstrate various string operations

# Input strings
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Length operation
print("\nLength of first string:", len(str1))
print("Length of second string:", len(str2))

# Copy operation
copy_str = str1[:]
print("\nCopied string:", copy_str)

# Append operation (Concatenation)
append_str = str1 + str2
print("\nAppended string:", append_str)

# Compare operation
if str1 == str2:
    print("\nBoth strings are equal")
else:
    print("\nBoth strings are not equal")