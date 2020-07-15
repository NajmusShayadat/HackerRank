N = int(input())
arr = []
for i in range(N):
	command, *a = input().split()
	inp = list(map(int, a))
	command = str(command)
	if command == 'insert':
		arr.insert(inp[0], inp[1])
	elif command == 'append':
		arr.append(inp[0])
	elif command == 'remove':
		arr.remove(inp[0])
	elif command == 'pop':
		arr.pop()
	elif command == 'sort':
		arr.sort()
	elif command == 'reverse':
		arr.reverse()
	elif command  =='print':
		print(arr)