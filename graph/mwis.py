# using DP to solve maximum weight independent set problem

def solve_mwis(lst):
    res = []
    res.append(lst[0])
    res.append(max(lst[0], lst[1]))
    for x in lst[2:]:
        not_include_x = res[-1]
        include_x = res[-2] + x
        res.append(max(not_include_x, include_x))
    return res[-1], recover_solution(res)

def recover_solution(res):
    lst = []
    i = len(res) - 1
    while i > 0:
        if res[i] > res[i-1]:
            lst.append(i)
            i -= 2
        else:
            i -= 1
    if i == 0:
        lst.append(0)
    return lst



def test():
    file = open("mwis.txt", "r")
    lst = file.readlines()
    lst = [int(i) for i in lst[1:]]
    print(solve_mwis(lst))

test()
