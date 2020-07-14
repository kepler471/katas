from itertools import permutations, combinations_with_replacement, chain
import time
import random


def apply_ops(ops, nums):
    i, j, k = ops
    a, b, c, d = [float(n) for n in nums]
    A, B, C, D = nums
    opmap = {'+': float.__add__,
             '-': float.__sub__,
             '*': float.__mul__,
             '/': float.__truediv__}
    strf = (A, i, B, j, C, k, D)

    try:
        if opmap[j](opmap[i](a, b), opmap[k](c, d)) == 24:
            return "({}{}{}){}({}{}{})".format(*strf)
    except ZeroDivisionError:
        pass
    try:
        if opmap[k](opmap[j](opmap[i](a, b), c), d) == 24:
            return "(({}{}{}){}{}){}{}".format(*strf)
    except ZeroDivisionError:
        pass
    try:
        if opmap[k](opmap[i](a, opmap[j](b, c)), d) == 24:
            return "({}{}({}{}{})){}{}".format(*strf)
    except ZeroDivisionError:
        pass
    try:
        if opmap[i](a, opmap[k](opmap[j](b, c), d)) == 24:
            return "{}{}(({}{}{}){}{})".format(*strf)
    except ZeroDivisionError:
        pass
    try:
        if opmap[i](a, opmap[j](b, opmap[k](c, d))) == 24:
            return "{}{}({}{}({}{}{}))".format(*strf)
    except ZeroDivisionError:
        pass


def permute_ops(ops='+-*/'):
    y = [permutations(x) for x in combinations_with_replacement(ops, 3)]
    return chain.from_iterable(y)


op_perms = set(permute_ops())


def equal_to_24(*case):
    case_perms = permutations(case)
    for case_i in case_perms:
        for op in op_perms:
            result = apply_ops(op, case_i)
            if result:
                return result
    return "It's not possible!"


random.seed(42)
if __name__ == "__main__":
    # Set up test tuples:
    #   17,160 as the complete set of permutations for 4 playing cards
    #   5,000 random ints
    z = permutations(range(1, 14), 4)
    zl = list(z)
    rl = [(random.randint(1, 100),
           random.randint(1, 100),
           random.randint(1, 100),
           random.randint(1, 100))
          for ri in range(5000)]

    results_52 = {}
    start = time.time()
    for zi in zl:
        results_52[zi] = equal_to_24(*zi)

    results_rand = {}
    for ri in rl:
        results_rand[ri] = equal_to_24(*ri)

    performance = time.time() - start
    print(performance)
