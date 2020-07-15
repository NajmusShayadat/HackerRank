def mutate_string(string, position, character):
    new = string[:position] + c + string[position+1:]
    return new

s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)