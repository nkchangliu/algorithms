from tree_node import TreeNode

class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, val):
        node = TreeNode(val)
        self.root = insert_helper(self.root, node)

    def in_order(self):
        return in_order_helper(self.root)

    def find(self, val):
        return find_helper(self.root, val)

    def find_min(self):
        return find_min_helper(self.root)

    def find_max(self):
        return find_max_helper(self.root)

    def predecessor(self, val):
        node = self.find(val)
        if not node:
            return None
        if node.left:
            return find_max_helper(node.left)
        else:
            curr = node
            while curr and curr.parent:
                if curr.parent.val < node.val:
                    return curr.parent
                curr = curr.parent
            return None

    def successor(self, val):
        node = self.find(val)
        if not node:
            return None
        if node.right:
            return find_min_helper(node.right)
        else:
            curr = node
            while curr and curr.parent:
                if curr.parent.val > node.val:
                    return curr.parent
                curr = curr.parent
            return None

    def delete(self, val):
        node = self.find(val)
        if not node:
            return None
        if node.is_leaf():
            delete_leaf(self.root, node)
        elif not node.has_two_children():
            delete_has_one_child(self.root, node)
        else:
            predecessor = self.predecessor(val)
            predecessor.val, node.val = node.val, predecessor.val
            if predecessor.is_leaf():
                delete_leaf(self.root, predecessor)
            else:
                delete_has_one_child(self.root, predecessor)


def delete_leaf(root, node):
    if node.is_left_child():
        node.parent.left = None
    elif node.is_right_child():
        node.parent.right = None
    else:
        root = None

def delete_has_one_child(root, node):
    if node.is_left_child():
        if node.left:
            node.parent.left = node.left
            node.left.parent = node.parent
        else:
            node.parent.left = node.right
            node.right.parent = node.parent
    elif node.is_right_child():
        if node.left:
            node.parent.right = node.left
            node.left.parent = node.parent
        else:
            node.parent.right = node.right
            node.right.parent = node.parent
    else:
        if node.left:
            root = node.left
        else:
            root = node.right

def find_min_helper(root):
    if not root or not root.left:
        return root
    return find_min_helper(root.left)

def find_max_helper(root):
    if not root or not root.right:
        return root
    return find_max_helper(root.right)

def find_helper(root, val):
    if not root or root.val == val:
        return root
    if root.val >= val:
        return find_helper(root.left, val)
    else:
        return find_helper(root.right, val)

def in_order_helper(root):
    if not root:
        return ""
    return in_order_helper(root.left) + str(root.val) + in_order_helper(root.right)

def insert_helper(root, node):
    if not root:
        root = node
    elif node.val >= root.val:
        root.right = insert_helper(root.right, node)
        root.right.parent = root
    else:
        root.left = insert_helper(root.left, node)
        root.left.parent = root
    return root



