"""
Binary Indexed Tree
"""
__author__ = 'Daniel'


class BIT(object):
    def __init__(self, n):
        """BIT uses index starting from 1"""
        self.N = [0 for _ in xrange(n+1)]

    def lowbit(self, x):
        return x & -x

    def set(self, i, val):
        while i < len(self.N):
            self.N[i] += val
            i += self.lowbit(i)

    def pre_sum(self, i):
        ret = 0
        while i > 0:
            ret += self.N[i]
            i -= self.lowbit(i)

        return ret

    @staticmethod
    def test():
        A = [1, 2, 3, 4, 5]
        n = len(A)
        bit = BIT(n)
        for i in xrange(n):
            bit.set(i+1, A[i])

        for i in xrange(n):
            print bit.pre_sum(i+1)


if __name__ == "__main__":
    BIT.test()

