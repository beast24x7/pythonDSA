#tuples are immutable

t = (1,2,3)

print(type(t))

print(len(t))

t = (2,2,[9,8,7])
print(t)

print(t[2])
print(t[-1])

print(t.count(2))

print(t.index(2))
# t[0] = 3 doesn't work, immutable

