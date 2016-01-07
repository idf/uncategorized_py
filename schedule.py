from collections import defaultdict

__author__ = 'Daniel'


class Val(object):
    def __init__(self):
        self.cnt = 0
        self.start = 0


class TaskScheduleSolution(object):
    def solve(self, A, intvl):
        m = defaultdict(Val)
        for e in A:
            m[e].cnt += 1

        t = 0  # time sequence
        for _ in A:
            maxa = None
            for k, v in m.items():
                if not maxa or m[maxa].cnt <= v.cnt:
                    if m[maxa].cnt == v.cnt and m[maxa].start > v.start:
                        maxa = k
                    elif m[maxa].cnt < v.cnt:
                        maxa = k

            # finish one task
            t = max(t, m[maxa].start)+1
            m[maxa].cnt -= 1
            if m[maxa] <= 0:
                del m[maxa]

            m[maxa].start = t+intvl

        return t


if __name__ == "__main__":
    assert TaskScheduleSolution().solve([1, 1, 2, 1], 2) == 7
    assert TaskScheduleSolution().solve([1, 2, 3, 1, 2, 3], 3) == 7
