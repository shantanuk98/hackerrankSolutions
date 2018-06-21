n,m=[int(i) for i in input().split()]
a=[0]*n
for _ in range(m):
    b,e,v=[int(i) for i in input().split()]
    if b<=n:a[b-1]+=v
    if e<n:a[e]-=v
s=0
s1=0
for i in a:
    s+=i
    s1=max(s1,s)
print(s1)