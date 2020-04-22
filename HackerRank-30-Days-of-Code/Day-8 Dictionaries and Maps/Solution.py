count = int(input())
phoneBook = {}

for i in range(count):
    name , phoneNumber  = input().split()
    phoneBook[name] = int(phoneNumber)

for i in range(count):
    try:
        searchName = input()
        if searchName in phoneBook:
            print(f'{ searchName }={phoneBook[searchName]}')
        else:
            print('Not found')
    except:
        break
