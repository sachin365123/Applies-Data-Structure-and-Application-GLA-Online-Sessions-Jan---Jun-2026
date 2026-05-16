# 20 Write a program for addition of polynomials. 

# Program for Addition of Two Polynomials

# Function to add two polynomials
def add_polynomials(poly1, poly2):

    max_len = max(len(poly1), len(poly2))

    # Make both polynomials of same length
    while len(poly1) < max_len:
        poly1.insert(0, 0)

    while len(poly2) < max_len:
        poly2.insert(0, 0)

    result = []

    # Add corresponding coefficients
    for i in range(max_len):
        result.append(poly1[i] + poly2[i])

    return result


# Input first polynomial
n1 = int(input("Enter highest degree of first polynomial: "))

poly1 = []

print("Enter coefficients of first polynomial:")
for i in range(n1 + 1):
    coeff = int(input(f"Coefficient of x^{n1-i}: "))
    poly1.append(coeff)

# Input second polynomial
n2 = int(input("\nEnter highest degree of second polynomial: "))

poly2 = []

print("Enter coefficients of second polynomial:")
for i in range(n2 + 1):
    coeff = int(input(f"Coefficient of x^{n2-i}: "))
    poly2.append(coeff)

# Add polynomials
result = add_polynomials(poly1, poly2)

# Display result
degree = len(result) - 1

print("\nResultant Polynomial:")

for i in range(len(result)):
    coeff = result[i]

    if coeff != 0:
        if degree - i > 1:
            print(f"{coeff}x^{degree-i}", end=" + ")
        elif degree - i == 1:
            print(f"{coeff}x", end=" + ")
        else:
            print(f"{coeff}", end="")

print()