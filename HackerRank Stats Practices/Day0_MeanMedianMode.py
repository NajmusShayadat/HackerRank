# take input of the length of the array
length = int(input())
# take input of 10 evenly spaced array and split them
inp = input().split()
# convert into a list of integers
nums = list(map(int, inp))


# calculate mean
def mean_out(n, x):
    return sum(x) / n


# calculate median
def median_out(n, x):
    x.sort()
    # if n is even, average of the central twwo element is median
    if n % 2 == 0:
        return (x[int(n / 2)] + x[int((n / 2) - 1)]) / 2
    # if n is odd, center element is the median
    else:
        return x[(n - 1) / 2]


# calculate mode
def mode_out(x):
    max_count = 0
    mde = 0
    for num in x:
        if x.count(num) > max_count:
            mde = num
            max_count = x.count(num)
    return mde


print(mean_out(length, nums))
print(median_out(length, nums))
print(mode_out(nums))
