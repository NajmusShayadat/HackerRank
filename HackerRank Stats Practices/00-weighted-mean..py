n = int(input().strip())  # not needed for python

x = list(map(int, input().strip().split(' ')))
w = list(map(int, input().strip().split(' ')))
w_sum = 0
for i in range(len(w)):
    w_sum += (x[i] * w[i])
print(round(w_sum / sum(w), 1))
