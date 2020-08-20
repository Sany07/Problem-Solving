

if __name__ == '__main__':
    arr = []

    my_hourglasses = list()

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    m = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            try:
                m.append(sum([arr[i][j],arr[i][j+1],arr[i][j+2],arr[i+1][j+1],arr[i+2][j],arr[i+2][j+1],arr[i+2][j+2]]))
            except IndexError as e:
                continue

    print(max(m))