p = int(input())  # this is not needed for python
arr = list(map(int, input().strip().split(' ')))


def median(x, n):
    # if n is even, average of the central two element is median
    if n % 2 == 0:
        return (x[int(n / 2)] + x[int((n / 2) - 1)]) / 2

    # if n is odd, center element is the median
    else:
        return x[int((n - 1) / 2)]


arr.sort()
l2 = len(arr)
l1 = int(l2 / 2)

q1 = median(arr[:l1], l1)
q2 = median(arr, l2)
q3 = median(arr[-l1:], l1)
print(int(q1))
print(int(q2))
print(int(q3))