# Exercise 1:
# Given two integer numbers return
# their product. If the product is greater than
# 1000, then return their sum.
def foo(num1, num2, limit):
    return num1 + num2  if (num1 * num2 > limit) else num1 * num2


num1 = 12
num2 = 2000
limit = 1000

print("Result = ", foo(num1, num2, limit))
