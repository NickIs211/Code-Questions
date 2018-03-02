import math
from functools import reduce
from itertools import compress
from sys import exit
n = 1
negative = 1
while(True):
    try:
        n = int(input("Prime factorization of what number? "))
        break
    except ValueError:
        print("That is not a number! Try again.")

if(n == 0):
    print("Zero has infinite factors!")
    exit(0)
if(n < 0):
    negative = -1
n = abs(n)
vals = [True for i in range(n+2)]

for i in range(2, int(math.sqrt(n)) + 2):
    if vals[i]:
        for j in range(i*i,n+1,i):
            vals[j] = False
primes = [x for x in range(2,n+1) if vals[x]]
if n in primes or n == 1:
    print(str(n) + ": " + ' x '.join([str(1),str(n)]))
    print("Factors:")
    print((1,n))
else:
    i = 0
    res = [n]
    while res[len(res)-1] not in primes:
        for prime in primes:
            if(res[len(res)-1] % prime == 0):
                res.insert(len(res)-1,prime)
                res[len(res)-1] = int(res[len(res)-1]/prime)
                break
    factors = {1}
    for i in range(1, n):
        l = list(bin(i)[2:].zfill(len(res)))
        factors.add(reduce((lambda x,y: x*y), compress(res, map(int,l))))
    final = list((factors))
    final.sort()
    print(final)
    res[0]*=negative
    print(str(n*negative) + ": " + ' x '.join(list(map(str,res))))
    print("Factors:")
    print(final)
    for i in range(0, int(len(final)/2) if(len(final) % 2 == 0) else int(len((final))/2 + 1)):
        print((final[i],final[int(len(final))-1-i]))