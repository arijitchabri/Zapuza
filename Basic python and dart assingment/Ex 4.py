# Exercise 4: Given a string and an integer number n,
# remove characters from a string starting from zero up to n
# and return a new string
def string_cutting(string, start_point):
    return string[start_point:]


new_str = "We are team black"
num = 4
print(string_cutting(new_str, num))
