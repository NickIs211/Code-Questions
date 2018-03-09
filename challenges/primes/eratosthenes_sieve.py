import math

n = int(input("Prime numbers from 0 to ...? "))
vals = [True for i in range(n+2)]
for i in range(2, int(math.sqrt(n)) + 2):
    if vals[i]:
        for j in range(i*i, n+1, i):
            vals[j] = False
print([x for x in range(2, n+1) if vals[x]])
