s = input()

t = type(s)
for method in [t.isalnum, t.isalpha, t.isdigit, t.islower, t.isupper]:
    print(any(method(c) for c in s))