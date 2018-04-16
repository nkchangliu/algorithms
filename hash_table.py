# implementation of hash_table


class HashTable(object):

    def __init__(self, capacity = 101):
        self.lst = [[]] * capacity
        self.keys = []
        self.capacity = capacity
        self.size = 0
        self.capacity_ind = 0
        self.capacity_lst = [101, 503, 1093, 2017, 4091, 8171, 17321, 34549, 79769, 160781]

    def insert(self, key, value):
        if key not in self.keys:
            self.lst[hash(key) % self.capacity].append((key, value))
            self.size += 1
            self.keys.append(key)
        else:
            lst, i = self.get_pair(key)
            lst[i] = (key, value)
        if self.capacity / self.size < 10:
            self.capacity_ind += 1
            self.resize(self.capacity_lst[self.capacity_ind])


    def get_pair(self, key):
        lst = self.lst[hash(key) % self.capacity]
        for i in range(len(lst)):
            if lst[i][0] == key:
                return lst, i

    def get_value(self, key):
        lst, i = self.get_pair(key)
        return lst[i][1]

    def resize(self, capacity):
        lst = [[]] * capacity
        self.capacity = capacity
        for key in self.keys:
            lst[hash(key) % capacity].append((key, self.get_value(key)))
        self.lst = lst




