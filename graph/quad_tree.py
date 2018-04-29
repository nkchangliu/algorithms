
class QuadTree(object):

    def __init__(self, root = None):
        self.root = root

    def add(self, x, y):
        if not self.find(x, y):
            self.root = add_node(self.root, x, y)

    def find(self, x, y):
        return find_node(self.root, x, y)

    def find_in_region(self, x0, y0, x1, y1):
        return find_in_region(self.root, x0, y0, x1, y1)


def find_in_region(root, x0, y0, x1, y1):
    if root == None:
        return []
    # look at four region:
    if root.x >= x0 and root.y >= y0 and root.x <= x1 and root.y <= y1:
        return [(root.x, root.y)] + find_in_region(root.ne, x0, y0, x1, y1) + find_in_region(root.se, x0, y0, x1, y1) + \
                find_in_region(root.sw, x0, y0, x1, y1) + find_in_region(root.nw, x0, y0, x1, y1)
    # look at two region:
    if root.x > x0 and root.x <= x1 and root.y < y0:
        return find_in_region(root.ne, x0, y0, x1, y1) + find_in_region(root.nw, x0, y0, x1, y1)
    elif root.x > x0 and root.x <= x1 and root.y > y1:
        return find_in_region(root.se, x0, y0, x1, y1) + find_in_region(root.sw, x0, y0, x1, y1)
    elif root.y > y0 and root.y <= y1 and root.x > x1:
        return find_in_region(root.nw, x0, y0, x1, y1) + find_in_region(root.sw, x0, y0, x1, y1)
    elif root.y > y0 and root.y <= y1 and root.x <= x0:
        return find_in_region(root.ne, x0, y0, x1, y1) + find_in_region(root.se, x0, y0, x1, y1)
    # look at one region:
    if root.x < x0 and root.y < y0:
        return find_in_region(root.ne, x0, y0, x1, y1)
    elif root.x > x1 and root.y > y1:
        return find_in_region(root.sw, x0, y0, x1, y1)
    elif root.x < x0 and root.y > y1:
        return find_in_region(root.se, x0, y0, x1, y1)
    else:
        return find_in_region(root.ne, x0, y0, x1, y1)



    # look at one region:

def find_node(root, x, y):
    if not root:
        return None
    elif root.x == x and root.y == y:
        return root
    elif root.x <= x and root.y <= y:
        return find_node(root.ne, x, y)
    elif root.x <= x and root.y >y:
        return find_node(root.se, x, y)
    elif root.x > x and root.y > y:
        return find_node(root.sw, x, y)
    else:
        return find_node(root.nw, x, y)



def add_node(root, x, y):
    if not root:
        root = Node(x, y)
    elif root.x <= x and root.y <= y:
        root.ne = add_node(root.ne, x, y)
    elif root.x <= x and root.y > y:
        root.se = add_node(root.se, x, y)
    elif root.x > x and root.y > y:
        root.sw = add_node(root.sw, x, y)
    else:
        root.nw = add_node(root.nw, x, y)
    return root


class Node(object):
    def __init__(self, x, y, ne = None, se = None, sw = None, nw = None):
        self.x = x
        self.y = y
        self.ne = ne
        self.se = se
        self.sw = sw
        self.nw = nw

