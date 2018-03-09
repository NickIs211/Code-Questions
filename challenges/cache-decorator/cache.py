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


print(fib(35))
