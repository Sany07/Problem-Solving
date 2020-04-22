count = int(input())

for i in range(0, count):
    data = input()
    even, odd = data[::2], data[1::2]
    print(even + " " + odd)
