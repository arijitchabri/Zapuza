"At here we are rotation a matrix 90 degree, clockwise, inplace"
arr = [
    [7, 8, 9],
    [1, 2, 3],
    [4, 5, 6]
]

n = len(arr)
for i in range(n//2):
    "Going throug loop for lenth half"
    for j in range(i, n - i - 1):
        temp = arr[j][n - i - 1]
        arr[j][n - i - 1] = arr[i][j]
        arr[n - i - 1][n - j - 1], temp = temp, arr[n - i - 1][n - j - 1]
        arr[n - j - 1][i], temp = temp, arr[n - j - 1][i]
        arr[i][j] = temp


print([i for i in arr], end="\n")