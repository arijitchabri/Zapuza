def largestSubArrayFinder(arr):
    "This takes a array and return the max_sub len where the sub sum is zero"
    cur = 0
    hash: "Taking this dictionary for hashing the elements" = {}
    max_sub = 0
    for i in range(len(arr)):
        cur += arr[i]
        if arr[i] == 0 and max_sub == 0:
            """At here we found a zero and if the max_sub is zero then 
            then max_sub now become 1 as 0 is in the arr."""
            max_sub = 1
        elif cur == 0:
            """If current become zero then it means that from
            starting to this pos all elements sum is zero"""
            max_sub = i + 1
        else:
            """At here we are storing the index of cur if it is not in has
            But if it does then it means that from that location to the current the
            sub sum is zero"""
            if cur in hash:
                max_sub = max(max_sub, (hash[cur] - 1))
            else:
                hash[cur] = i
    return max_sub


arr = [15, -2, 1, -9, 3, 7, -15, 23]
print(largestSubArrayFinder(arr))
