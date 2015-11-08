__author__ = 'Daniel'


class AllNerestSmallerValues(object):
    def allNearestSmaller(self, A):
        P = [-1 for _ in A]
        stk = []
        for i, v in enumerate(A):
            while stk and A[stk[-1]] >= v: stk.pop()

            if stk:
                P[i] = stk[-1]
            else:
                P[i] = -1  # no preceding smaller value

            stk.append(i)

        return P

    @staticmethod
    def test():
        A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
        solution = AllNerestSmallerValues()
        P = solution.allNearestSmaller(A)
        expected = [None, 0, 0, 4, 0, 2, 2, 6, 0, 1, 1, 5, 1, 3, 3, 7]
        for i, v in enumerate(P):
            if P[i] == -1:
                assert expected[i] is None
            else:
                assert expected[i] == A[P[i]]

if __name__ == "__main__":
    AllNerestSmallerValues.test()