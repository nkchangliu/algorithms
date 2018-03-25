# selection
# insertion
# bubble
# merge
# quick
# heap
# bucket sort
# radix sort
from random import randint

def selection_sort(lst):
    for i in range(len(lst)):
       minimum, m = min( (lst[i], i) for i in range(i, len(lst)))
       lst[i], lst[m]  = lst[m], lst[i]
    return lst


def insertion_sort(lst):
    for i in range(len(lst)):
        while i > 0 and lst[i - 1] > lst[i]:
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            i -= 1
    return lst

def bubble_sort(lst):
    sort = False
    while not sorted:
        sort = True
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i + 1], lst[i] = lst[i], lst[i + 1]
                sort = False
    return lst

def merge_sort(lst):
    return merge(lst, 0, len(lst) - 1)

def merge(lst, start, end):
    if start == end:
        return lst[start:end + 1]
    mid = int((start + end) / 2)
    lst1 = merge(lst, start, mid)
    lst2 = merge(lst, mid + 1, end)
    result = []
    i = 0
    j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            result.append(lst1[i])
            i += 1
        else:
            result.append(lst2[j])
            j += 1
    while i < len(lst1):
        result.append(lst1[i])
        i += 1
    while j < len(lst2):
        result.append(lst2[j])
        j += 1
    return result

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = randint(0, len(lst) - 1)
    small = []
    large = []
    for i in range(len(lst)):
        if i != pivot and lst[i] < lst[pivot]:
            small.append(lst[i])
        elif i != pivot and lst[i] >= lst[pivot]:
            large.append(lst[i])
    small = quick_sort(small)
    large = quick_sort(large)
    small += lst[pivot : pivot + 1]
    small += large
    return small

lst = [-1, 4, 2, -4, 3, 10]
print(selection_sort(lst))
print(insertion_sort(lst))
print(bubble_sort(lst))
print(merge_sort(lst))
print(quick_sort(lst))

