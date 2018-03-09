from functools import wraps


def cache(function):
    memo = {}

    @wraps(function)
    def wrapper(*args):
        if(args in memo):
            return memo[args]
        else:
            rt = function(*args)
            memo[args] = rt
            return rt
    return wrapper


@cache
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


def dp_fib(n):
    prev, forward = 0, 1
    for i in range(n):
        prev, forward = forward, prev+forward
    return prev


print(fib(8))
print(dp_fib(8))
