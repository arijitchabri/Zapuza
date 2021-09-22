arr1 = [3, 9, 10, 18, 23]
arr2 = [5, 12, 15, 20, 21, 25]
arr3 = []
n = len(arr1)
m = len(arr2)
j = 0
k = 0
while j < n and k < m:
    if arr1[j] > arr2[k]:
        arr3.append(arr2[k])
        k += 1
    else:
        arr3.append(arr1[j])
        j += 1
if arr1[j : ]:
    arr3.append(*arr1[j : ])
if arr2[k:]:
        arr3.append(*arr2[k:])

print(arr3)