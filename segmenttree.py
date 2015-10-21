"""
Segment Tree
"""
from operator import itemgetter

__author__ = 'Daniel'


class Node(object):
    def __init__(self, start, end, cnt):
        self.start = start
        self.end = end
        self.cnt = cnt

        self.left = None
        self.right = None

    def __repr__(self):
        return repr("[%d,%d)" % (self.start, self.end))


class SegmentTree(object):
    """empty space"""
    def __init__(self):
        self.root = None

    def build(self, start, end):
        """a node can have right ONLY if has left"""
        if start >= end:
            return

        root = Node(start, end, end-start)
        root.left = self.build(start, (end+start)/2)
        if root.left: root.right = self.build((start+end)/2, end)
        return root

    def find_delete(self, root, val):
        """
        :return: index
        """
        root.cnt -= 1
        if not root.left:
            return root.start
        elif root.left.cnt >= val:
            return self.find_delete(root.left, val)
        else:
            return self.find_delete(root.right, val-root.left.cnt)


class Solution(object):
    def reconstructFromInversion(self, A):
        st = SegmentTree()
        n = len(A)
        st.root = st.build(0, n)
        A = sorted(A, key=lambda x: x[0])
        ret = [0]*n
        for a in A:
            idx = st.find_delete(st.root, a[1]+1)
            ret[idx] = a[0]

        return ret

if __name__ == "__main__":
    A = [(5, 0), (2, 1), (3, 1), (4, 1,), (1, 4)]
    assert Solution().reconstructFromInversion(A) == [5, 2, 3, 4, 1]