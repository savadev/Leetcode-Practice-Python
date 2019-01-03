'''
既然题目保证了每次ping的t值都比之前的要更大，那么我们完全可以用队列来模拟实现整个过程，所求的数量即为队列的长度。
inputs = ["RecentCounter","ping","ping","ping","ping"],
inputs = [[],[1],[100],[3001],[3002]]

Output: [null,1,2,3,3]
'''
import collections


class RecentCounter:

    def __init__(self):
        self.q = collections.deque()
        # queue, first in and first out
        print('init q = ')
        print(self.q)

    def ping(self, t):
        self.q.append(t)

        while self.q[0] < t - 3000:
            self.q.popleft()
        print(self.q)
        return len(self.q)


# call 一次class 只会调用init一次
obj = RecentCounter()

obj.ping(1)
obj.ping(100)

