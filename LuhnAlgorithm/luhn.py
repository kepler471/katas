def validate(n):
    d = lambda k: [int(x) for x in str(n)[k::-2]]
    return sum(d(-1) + [9 if i == 9 else 2 * i % 9 for i in d(-2)]) % 10 == 0