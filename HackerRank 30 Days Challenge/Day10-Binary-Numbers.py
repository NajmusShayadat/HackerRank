# Day 10: Binary Numbers

n = int(input())
a = bin(n)[2:].split('0')
print(max(list(map(lambda s: len(s), a))))
