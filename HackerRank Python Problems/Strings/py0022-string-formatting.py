def print_formatted(number):
    # your code goes here
    # Remove spaces in the front after conversion. e.g 0b1101 becomes 1101
    width=len(bin(number)[2:]) 
    for i in range(1,number+1):
        deci=str(i)
        octa=oct(i)[2:]
        hexa=(hex(i)[2:]).upper()
        bina=bin(i)[2:]
        print(deci.rjust(width),octa.rjust(width),hexa.rjust(width),bina.rjust(width))

n = int(input())
print_formatted(n)