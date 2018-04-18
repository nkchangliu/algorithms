# implementation of min Heap (Priority Queue)

class PriorityQueue(object):

    def __init__(self, lst = None):
        self.lst = []
        self.location = {}
        if lst:
            self.heaptify(lst)

    def size(self):
        return len(self.lst)

    def heaptify(self, lst):
        self.lst = lst
        for ind, pair in enumerate(lst):
            self.location[pair[1]] = ind
        for i in reversed(range(0, len(self.lst) // 2)):
                self.percolate_down(i)


    def insert(self, priority, ele):
        if ele in self.location:
            self.update(priority, ele)
        else:
            self.lst.append((priority, ele))
            self.location[ele] = len(self.lst) - 1
            self.percolate_up(self.location[ele])

    def is_empty(self):
        return not self.lst

    def update(self, priority, ele):
        ind = self.location[ele]
        old_prio = self.lst[ind][0]
        self.lst[ind] = (priority, ele)
        if old_prio > priority:
            self.percolate_up(ind)
        else:
            self.percolate_down(ind)

    def delete_min(self):
        if self.is_empty():
            raise IndexError("empty heap")
        # swap the last one with the front
        self.swap(0, -1)
        # pop the last one
        prio, ele = self.lst.pop()
        self.location.pop(ele)
        self.percolate_down(0)
        return prio, ele

    def get_min(self):
        if self.is_empty():
            raise IndexError("empty heap")
        return self.lst[0]

    def percolate_down(self, ind):
        length = len(self.lst)
        while True:
            left = ind * 2 + 1
            right = ind * 2 + 2

            if left >= length and right >= length:
                break
            elif right >= length:
                minchild = left
            else:
                if self.lst[left][0] <= self.lst[right][0]:
                    minchild = left
                else:
                    minchild = right

            if self.lst[minchild][0] < self.lst[ind][0]:
                self.swap(minchild, ind)
                ind = minchild
            else:
                break

    def percolate_up(self, ind):
        length = len(self.lst)
        parent = (ind - 1) //2
        while ind > 0 and self.lst[parent][0] > self.lst[ind][0]:
            self.swap(ind, parent)
            ind = parent
            parent = (ind - 1) // 2

    def swap(self, ind1, ind2):
        self.lst[ind1], self.lst[ind2] = self.lst[ind2], self.lst[ind1]
        ele1, ele2 = self.lst[ind1][1], self.lst[ind2][1]
        self.location[ele1], self.location[ele2] = ind1, ind2



