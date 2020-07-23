from math import factorial as ft

a, b = map(float, input().split())

tot = 6
num = 3
prob = a / (a + b)
res = 0.0


# python 3.8 has math.comb (n,x) function built in.
def comb(n, x):
    return ft(n) / (ft(x) * ft(n - x))


# binomial probability formula.
def bp(x, n, p):
    return comb(n, x) * (p ** x) * ((1 - p) ** (n - x))


# for at least 3 boys it can be 3, 4 5 or 6 so it's cumulative
for i in range(num, tot + 1):
    res += bp(i, tot, prob)
print(round(res, 3))
