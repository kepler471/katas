from math import sqrt, ceil


def iterative(n, m):
    def isprime(x):
        for i in range(2, int(sqrt(x) + 1)):
            if x % i == 0:
                return False
        return True

    def rev(n):
        return int(str(n)[::-1])

    return [
        p
        for p in range(n, m + 1)
        if isprime(p) and isprime(rev(p)) and p != rev(p)
    ]


def recursive(n, m):
    def isprime(x):
        def check(i):
            return i > ceil(sqrt(x)) or (x % i != 0 and check(i + 1))

        return check(2)

    def rev(n):
        return int(str(n)[::-1])

    return [
        p for p in range(n, m + 1) if isprime(p) and isprime(rev(p)) and p != rev(p)
    ]
