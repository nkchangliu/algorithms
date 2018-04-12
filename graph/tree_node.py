class TreeNode(object):
    def __init__(self, value, left=None, right=None, parent=None):
        self.val = value
        self.left = left
        self.right = right
        self.parent = parent

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return self.left == None and self.right == None

    def has_two_children(self):
        return self.left and self.right

    def is_left_child(self):
        if self.parent:
            return self == self.parent.left

    def is_right_child(self):
        if self.parent:
            return self == self.parent.right



