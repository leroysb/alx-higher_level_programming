#!/usr/bin/python3
for i in range(10):
    for j in range(i,10):
        if i == j:
            continue
        if i == 8 and j == 9:
            continue
        print("{0}{1}".format(i,j), end = ", ")
print("{}".format(89))
