# gcd practice

'''
gcd(142,76)

142 = 76 * q -> #times it goes into 76 goes into 142
142 = 76 * q + r -> remainder

142 = 76 * 1 + 66

76 = 66 * 1 + 10

66 = 10 * 6 + 6

10 = 6 * 1 + 4

6 = 4 * 1 + 2

4 = 2 * 2 + 0

2 -> gcd


'''

def gcd(num, den):
    GCD = 0
    l = [num, den]
    g = max(l)
    m = min(l)
    n = g % m
    if n == 0:
        GCD = m
    while n != 0:
        GCD = n
        g = m
        m = n
        n = g % m
    return GCD





print(gcd(100, 10))
