from math import factorial as ft

reject, sample = map(int, input().split())
prob = reject / 100
res = []


# python 3.8 has math.comb (n,x) function built in.
def comb(n, x):
    # return the combination of nCx
    return ft(n) / (ft(x) * ft(n - x))


def bp(x, n, p):
    # return the binomial probability of a (x, n, p)
    return comb(n, x) * (p ** x) * ((1 - p) ** (n - x))


for i in range(sample + 1):
    res.append(bp(i, sample, prob))

print(f"{round(sum(res[:3]), 3)}\n{round(sum(res[2:]), 3)}")
