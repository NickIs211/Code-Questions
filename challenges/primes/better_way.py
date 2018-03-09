from itertools import combinations
from functools import reduce


def get_primes(n):
    vals = [True] * (n+1)
    for i in range(2, n+1):
        if(vals[i]):
            for v in range(i*i, n+1, i):
                vals[v] = False

    return [x for x in range(2, n+1) if vals[x]]


def prime_factorization(n):
    primes = get_primes(n)
    fits = [1, n]
    index = 0
    while index < len(primes):
        if(fits[-1] % primes[index] == 0):
            last, fits[-1] = fits[-1] // primes[index], primes[index]

            if last == 1:
                break

            fits.append(last)
            index = 0
            continue
        index += 1
    return fits


def getFactors(n, prime_factors=None):
    fits = []
    if(prime_factors is not None):
        fits = prime_factors
    else:
        fits = prime_factorization(n)
    factors = {reduce(lambda x, y: x*y, set_)
               for set_ in combinations(fits, 2)}
    factors.update([1, n])
    return sorted(factors)


num = int(input("What factorization do you desire sire? "))
if(num == 0):
    print("Infinite factors sire! The fortress crumbles.")
else:
    neg = 1
    print("IT SHALL BE.")
    if(num < 0):
        neg, num = -1, abs(num)
    prime_factors = prime_factorization(num)
    factors = list(getFactors(21, prime_factors))
    prime_factors[0] *= neg
    print('{} ='.format(neg*num), ' x '.join(str(p) for p in prime_factors))

    print("Factors: ")
    for i in range(0, len(factors)//2):
        print("  ", ' x '.join([str(factors[i]), str(factors[-1-i])]))
