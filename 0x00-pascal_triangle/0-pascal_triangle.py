def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row (0-indexed).

    :param n: The number of rows of Pascal's Triangle to generate.
    :return: A list of lists containing the values of Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)

    return triangle

# Example usage
if __name__ == "__main__":
    import sys
    import json
    if len(sys.argv) > 1:
        num_rows = int(sys.argv[1])
        print(json.dumps(pascal_triangle(num_rows)))
    else:
        print("Usage: python 0-pascal_triangle.py <number_of_rows>")
