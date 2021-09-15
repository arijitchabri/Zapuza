inp = "-1-2A-3-4-6-6-9"
num_lst1 = []
num_lst2 = []
num_lst3 = []
i = 0
for i in range(0, len(inp)):
    if len(num_lst1) < 2:
        if inp[i].isdigit():
            if inp[i - 1] == "-":
                num_lst1.append(int(inp[i]) * -1)
            else:
                num_lst1.append(int(inp[i]))
    elif len(num_lst2) < 3:
        if inp[i].isdigit():
            if inp[i - 1] == "-":
                num_lst2.append(int(inp[i]) * -1)
            else:
                num_lst2.append(int(inp[i]))

print(num_lst1)
print(num_lst2)
print(num_lst3)