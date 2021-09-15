# Exercise 6: Given a list of numbers,
# Iterate it and print only those numbers
# which are divisible of 5
# print(*number_list, end="\n")

my_list = [*range(100)]
print(*[i for i in my_list if i % 5 == 0])
















