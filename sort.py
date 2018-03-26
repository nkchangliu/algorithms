# selection
# insertion
# bubble
# merge
# quick
# heap
# bucket sort
# radix sort
# sort a stack using another stack
import math
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
    p = randint(0, len(lst) - 1)
    piv = lst[p]
    return quick_sort([x for x in lst if x < piv]) + \
            [x for x in lst if x == piv] + quick_sort([x for x in lst if x > piv])

def heap_sort(lst):
    lst = build_heap(lst)
    end = len(lst) - 1
    while end > 0:
        lst[0], lst[end] = lst[end], lst[0]
        lst = perc_down(lst, 0, end)
        end -= 1
    return lst


def build_heap(lst):
    for i in reversed(range(0, len(lst)//2)):
        lst = perc_down(lst, i, len(lst))
    return lst

def perc_down(lst, i, end):
    left = 2 * i + 1
    right = 2 * i + 2
    while left < end and right < end:
        max_child, min_child = compare_child(lst, left, right)
        if lst[i] >= lst[max_child]:
            return lst
        if lst[i] < lst[max_child]:
            lst[i], lst[max_child] = lst[max_child], lst[i]
            i = max_child
        elif lst[i] < lst[min_child]:
            lst[i], lst[min_child] = lst[min_child], lst[i]
            i = min_child
        left = 2 * i + 1
        right = 2 * i + 2
    while left < end:
        if lst[i] < lst[left]:
            lst[left], lst[i] = lst[i], lst[left]
            i = left
            left = 2 * i + 1
        return lst
    return lst

def compare_child(lst, left, right):
    if lst[left] > lst[right]:
        return left, right
    return right, left

def bucket_sort(lst, num_bucket = 10):
    buckets = [[] for i in range(num_bucket)]
    maxi, mini = max(lst), min(lst)
    step = math.ceil((maxi - mini) / num_bucket)
    for num in lst:
        buckets[(num - mini) // step].append(num)
    for bucket in buckets:
        insertion_sort(bucket)
    result = []
    for bucket in buckets:
        result += bucket
    return result

def radix_sort(lst):
    max_digit =len(str(max(lst)))
    buckets = [[] for i in range(10)]
    for num in lst:
        buckets[num % 10].append(num)
    for i in range(1, max_digit):
        buckets = radix_sort_helper(buckets, i)
    result = []
    for bucket in buckets:
        result += bucket
    return result

def radix_sort_helper(buckets, i):
    new_buckets = [[] for i in range(10)]
    for bucket in buckets:
        for num in bucket:
            new_buckets[(num // 10 ** i) % 10].append(num)
    return new_buckets


def stack_sort(lst):
    new_l = []
    while lst:
        value = lst.pop()
        if not new_l or value >= new_l[-1]:
            new_l.append(value)
        else:
            while new_l:
                lst.append(new_l.pop())
            new_l.append(value)
    return new_l

lst = [-1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, -4, 5, -5, 7, 3, 10, 25, 87, 32, 45,57, 61]
print(selection_sort(lst))
print(insertion_sort(lst))
print(bubble_sort(lst))
print(merge_sort(lst))
print(quick_sort(lst))
print(heap_sort(lst))
print(bucket_sort(lst))
print(stack_sort(lst))
radix_lst = [randint(0, 999) for i in range(100)]
print(radix_lst)
print(radix_sort(radix_lst))
