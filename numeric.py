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