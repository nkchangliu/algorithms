ENDS_HERE = '__ENDS_HERE'

class Trie(object):

    def __init__(self):
        self._trie = {}


    def insert(self, text):
        trie = self._trie
        for char in text:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        trie[END_HERE] = True

    def element(self, prefix):
        dic = self._trie
        for char in prefix:
            if char in dic:
                dic = dic[char]
            else:
                return []
        return self._element(dic)

    def _element(self, dic):
        res = []
        for key, value in dic:
            if key == ENDS_HERE:
                sub_res = [""]
            else:
                sub_res = [key + s for s in self._element(value)]
            res.extend(sub_res)
        return res



