# You are given an array A of N integers.
# You want to choose some integers from the array
# subject to the condition that the number of distinct
# integers chosen should not exceed K.
# Your task is to maximize the sum of chosen numbers.
# You are given T test cases.



from collections import Counter

for _ in range(int(input())):
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    freq = Counter(lst)
    arr = []
    for i in freq.keys():
        if i * freq[i] >= 0:
            arr.append(i * freq[i])
        else:
            continue
    arr.sort()
    print(sum(arr[-k:]))
