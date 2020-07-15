# Day 8: Dictionaries and Maps
n = int(input())
p = [input() for i in range(n)]

phonebook = dict(map(lambda s : s.split(), p))
while True:
    try:
        qry = input()
        if qry in phonebook:
            print(f'{qry}={phonebook[qry]}')
        else:
            print("Not found")
    except EOFError:
        break
