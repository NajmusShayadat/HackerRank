# Find std deviation

n = int(input().strip())  # not needed for python
arr = list(map(int, input().strip().split(' ')))


def sq_dis(a, mu):
    tot = 0
    for x in a:
        tot += (x - mu) ** 2
    return tot


mean = (sum(arr) / n)
sigma = (sq_dis(arr, mean) / n) ** 0.5
print(round(sigma, 1))
