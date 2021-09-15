#Exercise 5: Given a list of numbers,
#return True if first and last number of a list is same
#Given list is  [10, 20, 30, 40, 10] result is True
def equality(nfl):
    if len(nfl):
        return True if nfl[-1] == nfl[0] else False
    print("You can't give an empty list")
    return False


nl = [10, 20, 30, 40, 100]
print(equality(nl))
