def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = [[1]]  # Initialize the triangle with the first row

    for i in range(1, n):
        row = [1]  # Start each row with a 1
        for j in range(1, i):
            # Each element is the sum of the two elements directly above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # End each row with a 1
        triangle.append(row)
    
    return triangle

# Example test cases
print(pascal_triangle(5))  # Expected: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
print(pascal_triangle(0))  # Expected: []
print(pascal_triangle(1))  # Expected: [[1]]
print(pascal_triangle(2))  # Expected: [[1], [1, 1]]
