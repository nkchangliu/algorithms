# maintain the median of a list using log(n) time

# implement using two heaps, one min heap and one max heap

from pq import PriorityQueue

class Median(object):

    def __init__(self, lst = []):
        self.minHeap = PriorityQueue()
        self.maxHeap = MaxHeap()
        self.size = len(lst)
        if lst:
            lst = sorted(lst)
            mid = len(lst) // 2
            self.minHeap = PriorityQueue(lst[mid: ])
            self.maxHeap = MaxHeap(lst[0 : mid])

    def get_median(self):
        if self.size == 0:
            raise IndexError("empty heap")
        if self.size == 1 or self.size % 2 != 0:
            return self.minHeap.get_min()[0]
        else:
            return self.maxHeap.get_max()[0]


    def insert(self, prio, ele):
        if self.size == 0:
            self.minHeap.insert(prio, ele)
        elif self.size == 1:
            self.minHeap.insert(prio, ele)
            prio, ele = self.minHeap.delete_min()
            self.maxHeap.insert(prio, ele)
        else:
            min_in_minHeap = self.minHeap.get_min()[0]
            max_in_maxHeap = self.maxHeap.get_max()[1]
            if prio >= min_in_minHeap:
                self.minHeap.insert(prio, ele)
            else:
                self.maxHeap.insert(prio, ele)

        if not self.is_balanced():
            self.balance()
        self.size += 1

    def is_balanced(self):
        return self.minHeap.size() <= self.maxHeap.size() + 1 and \
                self.minHeap.size() >= self.maxHeap.size()

    def balance(self):
        while not self.is_balanced():
            if self.minHeap.size() >= self.maxHeap.size() + 1:
                prio, ele = self.minHeap.delete_min()
                self.maxHeap.insert(prio, ele)
            else:
                prio, ele = self.maxHeap.delete_max()
                self.minHeap.insert(prio, ele)




# use the minHeap build in pq as a max heap
class MaxHeap(object):
    def __init__(self, lst = []):
        lst = [(-prio, ele) for (prio, ele) in lst]
        self.maxHeap = PriorityQueue(lst)

    def insert(self, priority, ele):
        self.maxHeap.insert(-priority, ele)

    def delete_max(self):
        prio, ele = self.maxHeap.delete_min()
        return -prio, ele

    def get_max(self):
        prio, ele = self.maxHeap.get_min()
        return -prio, ele

    def size(self):
        return self.maxHeap.size()


