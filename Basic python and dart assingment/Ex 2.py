# Exercise 2: Given a range of the first 10 numbers,
# Iterate from the start number to the end number,
# and In each iteration print the sum of the current
# number and previous number.

nl = [*range(0, 11)]
print(nl)
[print(nl[i] + nl[i - 1]) for i in range(1, len(nl))]

