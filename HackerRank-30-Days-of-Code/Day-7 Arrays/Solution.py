import math
import os
import random
import re
import sys



n = int(input())

arr = list(map(int, input().rstrip().split()))

for i in arr[::-1]:
    print(i , end=' ')