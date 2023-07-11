#!/usr/bin/python3
"""pascal triangle module"""


def pascal_triangle(n):
    """
    return pascal triangle
    :rtype: list
    """
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        triangle.append([1 for _ in range(i + 1)])
        for j in range(len(triangle[i])):
            try:
                if i < 1 or j < 1:
                    raise IndexError
                triangle[i][j] = triangle[i - 1][j] + triangle[i - 1][j - 1]
            except IndexError:
                pass
    return triangle
