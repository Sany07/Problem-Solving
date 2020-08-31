
from itertools import permutations

w, n= input().split(" ")
permutations = list(permutations(w, int(n)))
permutations.sort()
[print("".join(i)) for i in permutations]