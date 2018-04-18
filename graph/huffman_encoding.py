from tree_node import TreeNode
from pq import PriorityQueue
from collections import Counter

def get_huffman_tree(s):
    frequency_lst = Counter(s)
    pq = PriorityQueue()
    for char, freq in frequency_lst.items():
        pq.insert(freq, TreeNode(char))

    while pq.size() > 1:
        freq1, node1 = pq.delete_min()
        freq2, node2 = pq.delete_min()

        internal_node = TreeNode(node1.val + node2.val, node1, node2)
        pq.insert(freq1 + freq2, internal_node)

    _, root = pq.delete_min()
    return get_code(root)

def get_code(root, prefix=''):
    if root == None:
        return {}
    elif root.is_leaf():
        return {root.val: prefix}

    left = get_code(root.left, prefix + '0')
    right = get_code(root.right, prefix + '1')
    return {**left, **right}

def encode(string):
    res = ''
    code_dict = get_huffman_tree(string)
    for s in string:
         res += code_dict[s]
    return res



