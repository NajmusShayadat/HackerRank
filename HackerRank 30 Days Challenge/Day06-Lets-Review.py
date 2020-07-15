def even(inp):
    # Create two variable for string output
    ev = ""
    od = ""
    # iterate through the input and assign the even and odd indexed characters to the respective variables
    for i in range(len(inp)):
        if i % 2 == 0:
            ev += inp[i]
        else:
            od += inp[i]
    # print the output
    print(f'{ev} {od}')


# take an int input T and iterate the loop T times for string input
T = int(input())
if 1 < T <= 10:
    for turn in range(T):
        S = input()

        if 2 <= len(S) <= 10000:
            even(S)