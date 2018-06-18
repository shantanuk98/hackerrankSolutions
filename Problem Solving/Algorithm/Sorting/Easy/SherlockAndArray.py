t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(i) for i in input().split()]
    s=sum(a)
    ans="NO"
    ctr=0
    for i in range(n):
        if s-ctr-a[i]==ctr:
            ans="YES"
            break 
        ctr+=a[i]
    print(ans)