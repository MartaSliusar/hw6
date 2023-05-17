lst = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
dct = {}
for k, v in lst:
    dct.setdefault(k, []).append(v)
print(dct)

