# 11 Write a program to demonstrate various operations (reverse, extracting a substring 
# from left, extracting a substring from right, extracting a substring from middle) on 
# strings. 

# Python program to demonstrate various string operations

# Input string
text = input("Enter a string: ")

# Reverse string
reverse_text = text[::-1]
print("\nReversed string:", reverse_text)

# Extract substring from left
left_sub = text[:3]
print("Substring from left:", left_sub)



# Extract substring from right
right_sub = text[-3:]
print("Substring from right:", right_sub)


# Extract substring from middle
start = len(text) // 2 - 1
middle_sub = text[start:start + 3]
print("Substring from middle:", middle_sub)