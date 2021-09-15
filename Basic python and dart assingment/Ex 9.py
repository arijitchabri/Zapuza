list1 = [*range(40)]
list2 = [*range(41, 81)]
list3 = [i for i in list1 if i % 2 == 0]
list3 = list3 + [j for j in list2 if j % 2 != 0]
print(list3)