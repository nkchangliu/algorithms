from random import randint

def random_shuffle(lst):
    for i in reversed(range(0, len(lst))):
        rand_ind = randint(0, i + 1)
        lst[rand_ind], lst[i] = lst[i], lst[rand_ind]
    return lst


