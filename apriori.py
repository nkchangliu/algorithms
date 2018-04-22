# first step: find those sets that have length one
K = 2

def apriori_firststep(lst):
    item_count = {}
    for l in lst:
        for item in l:
            if frozenset([item]) not in item_count:
                item_count[frozenset([item])] = 1
            else:
                item_count[frozenset([item])] += 1
    item_dict = {key: value for key, value in item_count.items() if value >= K}
    return item_dict

# find set with n elements
def apriori(lst, n):
    item_dict = apriori_firststep(lst)
    ele_to_consider = get_elements(item_dict)
    for i in range(n - 1):
        item_count = {}
        for key1 in item_dict:
            for key2 in ele_to_consider:
                if key2 not in key1:
                    new_key = set(key1)
                    new_key.add(key2)
                    s = frozenset(new_key)
                    item_count[s] = check_item(lst, s)
        item_dict = {key: value for key, value in item_count.items() if value >= K}
        ele_to_consider = get_elements(item_dict)
    return item_dict

def get_elements(item_dict):
    s = set()
    for key in item_dict:
        s.update(key)
    return s

def check_item(lst, s):
    count = 0
    for l in lst:
        if set(s).issubset(l):
            count += 1
    return count


