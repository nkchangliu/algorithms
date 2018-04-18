from disjointset import DisjointSet

def one_distance_away(s):
    one_away = set()
    for i in range(len(s)):
        if s[i] == "0":
            new_s = s[0: i] + "1" + s[i+1 : ]
        else:
            new_s = s[0: i] + "0" + s[i+1 : ]
        one_away.add(new_s)
    return one_away

def two_distance_away(s):
    two_away = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == "0":
                if s[j] == "0":
                    new_s = s[0:i] + "1" + s[i + 1 : j] + "1" + s[j+1 : ]
                else:
                    new_s = s[0:i] + "1" + s[i + 1: j] + "0" + s[j+1 :]
            else:
                if s[j] == "0":
                    new_s = s[0: i] + "0" + s[i + 1 : j] + "1" + s[j+1 : ]
                else:
                    new_s = s[0 : i] + "0" + s[i + 1 : j] + "0" + s[j+1 : ]
            two_away.add(new_s)
    return two_away


def num_cluster():
    file = open("big_distance.txt", "r")
    lst = file.readlines()
    lst = [l.strip("\n").replace(" ", "") for l in lst]
    lst = lst[1:]
    vertex = set(lst)
    ds = DisjointSet(vertex)
    for vertice in vertex:
        one_aways = one_distance_away(vertice)
        for v in one_aways:
            if v in vertex:
                ds.union(vertice, v)
        two_aways = two_distance_away(vertice)
        for v in two_aways:
            if v in vertex:
                ds.union(vertice, v)
    return len(ds.return_parents())


print(num_cluster())
