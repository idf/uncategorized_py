import random


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


class MergeSort(object):
    def merge_sort(self, A):
        """Inplace merge sort of array without recursive. The basic idea
        is to avoid the recursive call while using iterative solution.
        The algorithm first merge chunk of length of 2, then merge chunks
        of length 4, then 8, 16, .... , until 2^k where 2^k is large than
        the length of the array
        """
        n = len(A)
        l = 1
        while l <= n:
            for i in range(0, n, l*2):
                lo, hi = i, min(n, i+2*l)
                mid = i + l
                p, q = lo, mid
                while p < mid and q < hi:
                    if A[p] < A[q]:
                        p += 1
                    else:
                        tmp = A[q]
                        A[p+1: q+1] = A[p:q]
                        A[p] = tmp
                        p, mid, q = p+1, mid+1, q+1

            l *= 2

        return A


    @staticmethod
    def test():
        sorter = MergeSort()
        assert sorter.merge_sort([4, 3, 2, 1]) == [1, 2, 3, 4]
        assert sorter.merge_sort([4, 2, 3, 1]) == [1, 2, 3, 4]
        assert sorter.merge_sort([4, 5, 3, 2, 1]) == [1, 2, 3, 4, 5]

        for _ in range(100):
            tmp = range(100)
            random.shuffle(tmp)
            assert sorter.merge_sort(tmp) == range(100)

        return 'test pass!'


class MergeSorter2(object):
    def merge_sort(self, A):
        if len(A) <= 1:
            return

        mid = len(A)/2
        L, R = A[:mid], A[mid:]
        self.merge_sort(L)
        self.merge_sort(R)

        i, j, k = 0, 0, 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1

        if i < len(L):
            A[k:] = L[i:]
        if j < len(R):
            A[k:] = R[j:]

    @staticmethod
    def test():
        sorter = MergeSorter2()
        A = [4, 3, 2, 1]
        sorter.merge_sort(A)
        assert A == [1, 2, 3, 4]

        for _ in range(100):
            tmp = range(100)
            random.shuffle(tmp)
            sorter.merge_sort(tmp)
            assert tmp == range(100)

        return 'test pass!'


if __name__ == "__main__":
    PartialQuickSort.test()
    MergeSort.test()
    MergeSorter2.test()
