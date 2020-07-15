import textwrap

def wrap(string, max_width):
    a = textwrap.fill(string, max_width)
    return a

string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)