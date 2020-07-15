# nested list

# !/bin/python3

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    max_val = []
    for r in range(4):
        for c in range(4):
            glass = arr[r + 1][c + 1]
            for i in range(c, c + 3):
                glass += (arr[r][i] + arr[r + 2][i])
            max_val.append(glass)
    print(max(max_val))
