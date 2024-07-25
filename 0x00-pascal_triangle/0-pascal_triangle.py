def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row (0-indexed).

    :param n: The number of rows of Pascal's Triangle to generate.
    :return: A list of lists containing the values of Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    
    return triangle

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        num_rows = int(sys.argv[1])
        print(pascal_triangle(num_rows))
    else:
        print("Usage: python 0-pascal_triangle.py <number_of_rows>")
