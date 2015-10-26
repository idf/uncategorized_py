# -*- coding: utf-8 -*-
"""
author: 邵成
http://www.zhihu.com/question/36857981/answer/69520229
"""
__author__ = 'Daniel'


def fact(n):
    """factorization"""
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


id = lambda x: x  # identity


def factCPS(n):
    """Continuation Passing Style. Eliminate general recursion using tail call"""
    def f(n, k):
        if n == 0:
            return k(1)
        else:
            return f(n - 1, lambda x: k(n * x))

    return f(n, id)


def factNoRec(n):
    """for-loop for tail call"""
    def factory(n, k):
        """factory to make it closure; since scoping in Python is evil"""
        return lambda x: k(n * x)

    k = id
    while True:
        if n == 0:
            return k(1)
        else:
            k = factory(n, k)
            n -= 1


def factHolyCrap(n):
    k = ()
    while True:
        if n == 0:
            x = 1
            while k:
                x = k[0] * x
                k = k[1]
            return id(x)
        else:
            k = (n, k)
            n -= 1


if __name__ == '__main__':
    print([f(5) for f in [fact, factCPS, factNoRec, factHolyCrap]])