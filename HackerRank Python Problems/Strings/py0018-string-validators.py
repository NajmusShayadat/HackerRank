s = input()
alnum = []
alpha = []
digi = []
low = []
upp = []
for i in range(len(s)):
	alnum.append(s[i].isalnum())
	alpha.append(s[i].isalpha())
	digi.append(s[i].isdigit())
	low.append(s[i].islower())
	upp.append(s[i].isupper())
print(any(alnum))
print(any(alpha))
print(any(digi))
print(any(low))
print(any(upp))