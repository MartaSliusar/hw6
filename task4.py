lst = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
suma = 35
i = 0
j = 0
pairs = set()

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] + lst[j] == suma:
            result1 = lst[i], lst[j]
            pairs.add(result1)
            result2 = result1[::-1]
            pairs.add(result2)
print(sorted(pairs))

