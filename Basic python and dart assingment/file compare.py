import sys
# f = open(sys.argv[1], "r")
# f2 = open(sys.argv[2], "r")
f = open("file1.txt", "r")
f2 = open("file2.txt", "r")

lis1 = [i.replace("\n", "") for i in f]
lis2 = [i.replace("\n", "") for i in f2]
lis1 = [i.strip() for i in lis1 if i]
lis2 = [i.strip() for i in lis2 if i]
print(lis1)
for i in lis1:
    if i not in lis2:
        print(i, "-")
for i in lis2:
    if i not in lis1:
        print(i, "+")
