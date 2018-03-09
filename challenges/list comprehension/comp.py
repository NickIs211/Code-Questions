gen = (n**2 for n in range(10))

print(' x '.join(str(x) for x in gen))

li = [(n, m) for n in range(10) for m in range(10)]
print(li)
