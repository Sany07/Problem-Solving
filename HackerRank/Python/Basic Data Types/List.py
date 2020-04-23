    n = int(input())
    list = []
    for _ in range(n):
        x = input()
        x = x.split(" ")
        command = x[0]
        if command=="insert":
                a,b=int(x[1]),int(x[2])
                list.insert(a,b)
        elif command=="remove":
                a=int(x[1])
                list.remove(a)
        elif command=="append":
                a=int(x[1])
                list.append(a)
        elif command=="sort":
                list.sort()
        elif command=="pop":
                list.pop()
        elif command=="reverse":
                list.reverse()
        elif command=="print":
                print(list)
