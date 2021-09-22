arr = [15, -2, 1, -9, 3, 7, -15, 23]
cur = 0
hash = {}
max_sub = 0
for i in range(len(arr)):
    cur += arr[i]
    if arr[i] == 0 and max_sub == 0:
        max_sub = 1
    elif cur == 0:
        max_sub = i + 1
    else:
        if cur in hash:
            max_sub = max(max_sub, (hash[cur] - 1))
        else:
            hash[cur] = i
print(max_sub)
