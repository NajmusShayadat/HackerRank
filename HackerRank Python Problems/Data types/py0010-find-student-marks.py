n = int(input())
student_marks = {}
for i in range(n):
	name, *line = input().split()
	scores = list(map(float, line))
	student_marks[name] = scores
query_name = str(input())
sum = 0.0
for i in range(len(scores)):
	sum += student_marks[query_name][i]
avg = sum/len(scores)
print(format(avg, '.2f'))