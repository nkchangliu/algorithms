# create a segement tree that has stores the min of the lst

def segement_tree(lst):
    num = len(lst)
    res = [None] * len_needed(len(lst))
    return create_tree(lst, res, 0, len(lst) - 1, 0)


def create_tree(lst, res, low, high, pos):
    if low == high:
        res[pos] = lst[low]
    else:
        mid = (low + high) // 2
        create_tree(lst, res, low, mid, pos * 2 + 1)
        create_tree(lst, res, mid + 1, high, pos * 2 + 2)
        res[pos] = min(res[pos * 2 + 1], res[pos * 2 + 2])
    return res

def min_in_range(lst, search_low, search_high):
    segement = segement_tree(lst)
    return find_min(segement, 0, len(lst) -1, search_low, search_high, 0)


def find_min(segement, low, high, search_low, search_high, pos):
    # case 1: does not contain the range we look for
    if search_low > high or search_high < low:
        return float("inf")

    # case 2: contains the range
    elif search_low <= low and search_high >= high:
        return segement[pos]

    # case 3: partially contain the range
    else:
        mid = (low + high) // 2
        left = find_min(segement, low, mid, search_low, search_high, 2 * pos + 1)
        right = find_min(segement, mid + 1, high, search_low, search_high, 2 * pos + 2)
        return min(left, right)

def len_needed(length):
    if length == 0:
        return 0
    time = find_time(length, 0)
    if pow(2, time) == length:
        return pow(2, time) * 2 - 1
    else:
        return pow(2, time + 1) * 2 - 1

def find_time(length, n):
    if length < 2:
        return n
    else:
        return find_time(length // 2, n + 1)

