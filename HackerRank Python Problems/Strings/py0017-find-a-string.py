def count_substring(s, ss):
    c = 0
    for i in range((len(s)-len(ss)+1)):
        if s[i:(i + len(ss))] == ss:
            c += 1
    return c

string = input().strip()
sub_string = input().strip()

count = count_substring(string, sub_string)
print(count)