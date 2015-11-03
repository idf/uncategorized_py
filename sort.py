__author__ = 'Daniel'


class PartialQuickSort(object):
    def partial_qsort(self, A, i, j, m):
        if i >= j: return

        p = self.pivot(A, i, j)
        self.partial_qsort(A, i, p, m)
        if p+1 >= m: return
        self.partial_qsort(A, p+1, j, m)

    def pivot(self, A, i, j):
        p = i
        closed = p
        for ptr in xrange(i, j):
            if A[ptr] < A[p]:
                closed += 1
                A[ptr], A[closed] = A[closed], A[ptr]

        A[closed], A[p] = A[p], A[closed]
        return closed

    @staticmethod
    def test():
        A = [4, 5, 3, 2, 1, 6, 7]
        sorter = PartialQuickSort()
        m = 3
        sorter.partial_qsort(A, 0, len(A), m)
        try:
            assert A[:m] == range(1, m+1)
        except AssertionError as e:
            print A[:m]
            raise e

if __name__ == "__main__":
    PartialQuickSort.test()
