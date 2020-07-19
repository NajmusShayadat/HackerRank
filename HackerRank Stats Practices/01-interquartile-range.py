# Enter your code here. Read input from STDIN. Print output to STDOUT
p = int(input())  # this is not needed for python
arr = list(map(int, input().strip().split(' ')))
freq = list(map(int, input().strip().split(' ')))


def median(x, n):
    # if n is even, average of the central two element is median
    if n % 2 == 0:
        return (x[int(n / 2)] + x[int((n / 2) - 1)]) / 2

    # if n is odd, center element is the median
    else:
        return x[int((n - 1) / 2)]


def big_array(a, f):
    big = []

    for i in range(len(a)):

        # pick the i indexed frequency and add that many a[i]
        for j in range(f[i]):
            big.append(a[i])

    return big


s = big_array(arr, freq)
s.sort()

s_len = len(s)
q_len = int(s_len / 2)

q1 = median(s[:q_len], q_len)
q3 = median(s[-q_len:], q_len)
print(round(float(q3 - q1), 1))
