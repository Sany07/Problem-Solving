if __name__ == '__main__':
    n = int(input())
    print(max(len(length) for length in bin(n)[2:].split('0')))
