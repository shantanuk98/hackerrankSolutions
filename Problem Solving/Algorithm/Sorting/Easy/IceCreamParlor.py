t=int(input())
for _ in range(t):
    m=int(input())
    n=int(input()) 
    a=[int(i) for i in input().split()]
    c=0
    for j in range(n-1):
        for k in range(j+1,n):
            if a[j]+a[k]==m:
                print(min(j,k)+1,max(j,k)+1)
                c=1
                break
        if c==1:break