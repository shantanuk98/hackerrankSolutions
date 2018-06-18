import math
t=int(input())
for _ in range(t):
    n,k=[int(i) for i in input().split()]
    i=0
    j=n-1
    a=[]
    for l in range(n):
        if l%2==0:
            a.append(j)
            j-=1
        else:
            a.append(i)
            i+=1
    print(a.index(k))
    
    