import re

n = int(input())
s = ''
for i in range(n):
    s += input() + '\n'

t = int(input())

for i in range(t):
    word = input().strip()
    pat = rf'\b{word}\b'
    words = re.findall(pat, s)
    print(len(words))
