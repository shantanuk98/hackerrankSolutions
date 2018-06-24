n=int(input())
a=[int(i) for i in input().split()]
a.sort()
m=10**18+1
for i in range(n-1):
    if abs(a[i]-a[i+1])<m:m=abs(a[i]-a[i+1])
print(m)