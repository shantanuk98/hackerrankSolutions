n,k=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
a.sort()
ctr=0
s=0
for i in range(n):
    if s+a[i]<=k:
        ctr+=1
        s+=a[i]
    else:break
print(ctr)
        