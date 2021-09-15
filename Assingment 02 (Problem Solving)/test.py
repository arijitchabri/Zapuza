import re

inp = "12A446-99"
vowels = {"A", "E", "I", "O", "U", "Y"}
inpt = re.c(r'(\d*1)(\w)(\d\d\d)-(\d\d)')
res = inpt.search(inp)
lst = [i for i in res.group()]

print(lst)