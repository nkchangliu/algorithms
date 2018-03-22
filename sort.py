# selection
# insertion
# bubble
# merge
# quick
# heap
# bucket sort
# radix sort

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

lst = [-1, 4, 2, -4, 3, 10]

print(selection_sort(lst))
print(insertion_sort(lst))
print(bubble_sort(lst))
