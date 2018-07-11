lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

s = lst[3:7]
# lst[3:7] = []
print(s)

s.reverse()
print(s)
# lst = lst[:3] + s + lst[3:]
lst[3:7] = s
print(lst)