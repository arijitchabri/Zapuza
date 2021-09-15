#Exercise 8: Reverse a given number and return true if
# it is the same as the original number

num = int(input("Give me a number :- "))
num_rev = 0
temp = num
while num > 0:
    num, mod = divmod(num, 10)
    num_rev = num_rev*10 +mod
if num_rev == temp:
    print("True")
else:
    print("False")
























