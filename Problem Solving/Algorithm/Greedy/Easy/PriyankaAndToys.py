n=int(input())
a=[int(i) for i in input().split()]
a.sort()
ctr=1
key=a[0]
for i in range(1,n):
    if a[i]>key+4:
        key=a[i]
        ctr+=1
print(ctr)
        