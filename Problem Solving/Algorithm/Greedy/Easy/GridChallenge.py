t=int(input())
for _ in range(t):
    n=int(input())
    a=[]
    for i in range(n):
        a.append(sorted(input()))
    ans="YES"
    for i in range(n):
        b=[]
        for j in range(n):
            b.append(a[j][i])
        if b!=sorted(b):
            ans="NO"
            break
    print(ans)