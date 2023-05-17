dct = {}
lst = list("w3resource")

for el in lst:
    dct.setdefault(el, 0)
    dct[el] += 1
print(dct)
