n=int(input())
a=[int(i) for i in input().split()]
m=int(input())
b=[int(i) for i in input().split()]
mi=min(min(a),min(b))
for i in range(n):a[i]=a[i]-mi
for i in range(m):b[i]=b[i]-mi
c=[0]*101
for i in range(m):c[b[i]]+=1
for i in range(n):c[a[i]]-=1
for i in range(101):
    if c[i]>0:print(i+mi,end=" ")