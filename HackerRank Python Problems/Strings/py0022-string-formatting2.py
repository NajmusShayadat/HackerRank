def print_formatted(number):
    # your code goes here
    # Remove spaces in the front after conversion. e.g 0b1101 becomes 1101
    w = 1 + len(bin(number)[2:]) 
    for i in range(1,number+1):
        de = str(i)
        oc = oct(i)[2:]
        he = (hex(i)[2:]).upper()
        bi = bin(i)[2:]
        print(f"{de:>{w-1}}{oc:>{w}}{he:>{w}}{bi:>{w}}")

n = int(input())
print_formatted(n)