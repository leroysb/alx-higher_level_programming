#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)

print("------")
print("------")

try:
    print(matrix_divided(matrix, "School"))
except Exception as e:
    print(e)

print("------")
print("------")

try:
    print(matrix_divided(matrix, 0))
except Exception as e:
    print(e)

print("------")
print("------")

try:
    print(matrix_divided(10, 2))
except Exception as e:
    print(e)

print("------")
print("------")


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8]
]

try:
    print(matrix_divided(matrix, 1))
except Exception as e:
    print(e)

print(matrix)


print("------")
print("------")


matrix = [
    [1, 2, 3],
    ["This", "is", "Python"]
]

try:
    print(matrix_divided(matrix, 1))
except Exception as e:
    print(e)

print(matrix)
