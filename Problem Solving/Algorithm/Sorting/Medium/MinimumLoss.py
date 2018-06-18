n=int(input())
a=[int(i) for i in input().split()]
for i in range(n):
    a[i]=[a[i],i]
a.sort(reverse=True)
#print(a)
mindif=10**16+1
for i in range(n-1):
    if a[i][0]-a[i+1][0]<mindif and a[i][1]<a[i+1][1]:mindif=a[i][0]-a[i+1][0]
print(mindif)