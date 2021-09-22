mat = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 60

mat = [j for i in mat for j in i]

low = 0
high = len(mat) - 1
mid = high // 2


def BinarySearch(low, high):
    mid = (low + high) // 2
    if low > high:
        return False
    elif mat[mid] > target:
        high = mid - 1
        return BinarySearch(low, high)
    elif mat[mid] < target:
        low = mid + 1
        return BinarySearch(low, high)
    else:
        return True


res = BinarySearch(low, high)
print(res)
