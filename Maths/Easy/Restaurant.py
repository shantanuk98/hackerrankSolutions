import math
t=int(input())
for _ in range(t):
    l,b=[int(i) for i in input().split()]
    print((l*b)//math.gcd(l,b)**2)