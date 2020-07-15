h, w = [int(x) for x in input().split()]
c1 = '.|.'
c2 = '-'
c3 = 'WELCOME'
hlines = int(h/2)

#Top part
for i in range(hlines):
	print(((c1*(2*i+1)).center(w,c2)))

#Mid part
print((c3).center(w,c2))

#Bottom part
for i in range(hlines,0,-1):
	print((c1*(2*i-1)).center(w,c2))