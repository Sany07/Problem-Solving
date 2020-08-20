S = input().strip()


try:
    conInt = int(S)
    print(conInt)

except ValueError:
    print('Bad String')
