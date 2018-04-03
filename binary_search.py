# binary search value on a lst
def binary_search(lst, start, end, value):
    if start == end:
        if lst[start] == value:
            return start
        return -1
    mid = (start + end) // 2
    if value == lst[mid]:
        return mid
    elif value < lst[mid]:
        return binary_search(lst, start, mid - 1, value)
    else:
        return binary_search(lst, mid + 1, end, value)

def binary_search_iterative(lst, value):
    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == value:
            return mid
        elif lst[mid] > value:
            end = mid - 1
        else:
            start = mid + 1
    return -1

print(binary_search_iterative([3, 5, 6, 10, 18, 20], 6))
print(binary_search_iterative([3, 5, 6, 10, 18, 20], 7))


# given a sorted list of distant integer, return true if exists i where lst[i] = i
def find_index(lst):
    start, end = 0, len(lst) - 1
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == mid:
            return True
        elif lst[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
    return False

print(find_index([-8, -5, -3, 3, 4, 5, 7, 9]))
print(find_index([-8, -5, -3, 2, 5, 6, 7, 9]))


# find max of an unimodal array
def find_max(lst, start, end):
    if start == end:
        return lst[start]
    if start + 1 == end:
        if lst[start] > lst[end]:
            return lst[start]
        else:
            return lst[end]
    mid = (start + end) // 2
    if lst[mid] >= lst[mid - 1] and lst[mid] >= lst[mid + 1]:
        return lst[mid]
    elif lst[mid] > lst[mid - 1] and lst[mid] < lst[mid + 1]:
        return find_max(lst, mid + 1, end)
    else:
        return find_max(lst, start, mid - 1)

print(find_max([2, 5, 6, 8, 14, 12, 8, 5, 4], 0, 9))

# given a sorted array being rotated many times, find x in the array
def binary_search_rotate(lst, x):
    l = 0
    u = len(lst) - 1
    while(l < u):
        m = (l + u) // 2
        if x == lst[m]:
            return m
        elif lst[l] < lst[u]:
            if x > lst[m]:
                l = m + 1
            elif x > lst[m]:
                u = m - 1
            else:
                l = m + 1
        elif x < lst[m]:
            u = m - 1
        elif x < lst[u]:
            l = m + 1
        else: u = m - 1
    return -1


# given a list of string with empty "", find str s
def find_str_bi(lst, s):
    l = 0
    u = len(lst) - 1
    while l < u:
        m = (l + u) // 2
        while m < len(lst) and lst[m] == "":
            m += 1
        while m > 0 and lst[m] == "":
            m -= 1
        if lst[m] == "":
            return -1
        else:
            if s == lst[m]:
                return m
            elif s < lst[m]:
                u = m - 1
            else:
                l = m + 1
