import re

n = int(input())

pat = r'\w+[.\w]*@\w+[.\w]+\w+'
sep = ';'
s = ''
for i in range(n):
    s += input() + '\n'
res = re.findall(pat, s)
# out = list(set(res))
# out.sort()
print(sep.join(sorted(set(res))))
