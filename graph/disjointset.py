class DisjointSet(object):

    def __init__(self, s):
        self.rank = {}
        self.parent = {}
        for ele in s:
            self.parent[ele] = ele
            self.rank[ele] = 0


    def find(self, ele):
        if self.parent[ele] != ele:
            self.parent[ele] = self.find(self.parent[ele])

        return self.parent[ele]

    def union(self, ele1, ele2):
        parent1 = self.find(ele1)
        parent2 = self.find(ele2)
        if self.rank[parent1] < self.rank[parent2]:
            self.parent[parent1] = parent2
        elif self.rank[parent1] > self.rank[parent2]:
            self.parent[parent2] = parent1
        else:
            self.parent[parent2] = parent1
            self.rank[parent1] += 1

    def return_parents(self):
        parents = set()
        for ele in self.parent:
            if ele == self.parent[ele]:
                parents.add(ele)

        return parents

    def return_sets(self):
        sets = {}
        for parent in self.return_parents():
            sets[parent] = set()

        for ele in self.parent:
            parent = self.find(ele)
            sets[parent].add(ele)

        return sets


