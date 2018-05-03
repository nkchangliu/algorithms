from random import randint
from random import uniform

# implement the grade school multiplication

def multiplication_naive(num1, num2):
    n1 = [int(i) for i in str(num1)]
    n2 = [int(i) for i in str(num2)]
    if len(n1) < len(n2):
        n1, n2 = n2, n1
    res = 0
    for i in reversed(range(len(n2))):
        carryover = 0
        subresult = []
        for j in reversed(range(len(n1))):
            digit = (n2[i] * n1[j] + carryover) % 10
            carryover = (n2[i] * n1[j] + carryover) // 10
            subresult.insert(0, digit)
        if carryover != 0:
            subresult.insert(0, carryover)
        for _ in range(len(n2) - i - 1):
            subresult.append(0)
        subresult = [str(x) for x in subresult]
        res += int(''.join(subresult))
    return res

# implement the karatsuba's algorithm
'''
x = 5678
y = 1234
a = 56 b = 78
c = 12 d = 34
1) a* c =
2) b*d =
3) (a + b) * (c + d)
xy = 10^nac + 10^n/2(ad + bc) + bc
recursively compute ac and bd
compute (a + b)(c + d)
so only compute three recursive ones
'''
def multiplication_kara(num1, num2):
    if len(str(num1)) == 1 or len(str(num2)) == 1:
        return multiplication_naive(num1, num2)
    length = max(len(str(num1)), len(str(num2)))
    n = length // 2
    a = num1 // 10 ** n
    b = num1 % 10 ** n
    c = num2 // 10 ** n
    d = num2 % 10 ** n
    ac = multiplication_kara(a, c)
    bd = multiplication_kara(b, d)
    adbc = multiplication_kara(a + b, c + d) - ac - bd
    res = ac * 10 **(2 * n) + adbc * 10 ** n + bd
    return res
n1 = 3141592653589793238462643383279502884197169399375105820974944592
n2 = 2718281828459045235360287471352662497757247093699959574966967627
print(multiplication_naive(n1, n2))
print(multiplication_kara(n1, n2))



# use newton method to find the square root of a num
def newton_method(num, delta):
    x = num // 2 + 1
    while x * x - num > delta * delta:
        x = 1/2 * (x + num/x)
    return x


# return all the primes up until n using the Sieve of Eratosthenes method
def find_prime(n):
    if n < 2:
        return []
    prime_lst = [2]
    lst = [i for i in range(3, n+1)]

    while lst:
        new_lst = []
        for num in lst:
            if num % prime_lst[-1] != 0:
                new_lst.append(num)
        lst = new_lst
        if lst:
            prime_lst.append(lst[0])
    return prime_lst


# select the nth largest element in the lst
def quick_select(lst, n):
    pivot = lst[randint(0, len(lst)-1)]
    less_lst = [x for x in lst if x < pivot]
    same_lst = [x for x in lst if x == pivot]
    large_lst = [x for x in lst if x > pivot]
    if n <= len(large_lst):
        return quick_select(large_lst, n)
    elif n <= len(large_lst) + len(same_lst):
        return pivot
    else:
        return quick_select(less_lst, n - len(large_lst) - len(same_lst))

# use monte carlo method to calculate pi

def calculate_pi(n):
    within_circle = 0
    for i in range(n):
        x = uniform(-1, 1)
        y = uniform(-1, 1)
        if x **2 + y ** 2 <= 1:
            within_circle += 1
    return within_circle / n * 4


def reservoir_sample(lst, k):
    reserve = []
    for i in range(k):
        reserve.append(lst[i])
    for i in range(k, len(lst)):
        rand = randint(0, i)
        if rand < k:
            reserve[rand] = lst[i]
    return reserve


# euclidean meathod to find GCD
def gcd(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1
    reminder = num1 % num2
    if reminder == 0:
        return num2
    else:
        return gcd(num2, reminder)



