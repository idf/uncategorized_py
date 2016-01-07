from collections import deque
__author__ = 'Daniel'


class MaxProductSolution(object):
    def solve(self, A):
        """
        O(n)
        """
        q = deque([A[0]])
        maxa = 0
        for e in A[1:]:
            while q and q[0] < e:
                maxa = max(maxa, q[0]*e)
                q.popleft()

            q.append(e)

        return maxa


if __name__ == "__main__":
    assert MaxProductSolution().solve([1, 6, 2, 3, 6, 4, 9, 5, 10]) == 90