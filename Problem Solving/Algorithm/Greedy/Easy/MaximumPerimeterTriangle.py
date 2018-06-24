n=int(input())
a=[int(i) for i in input().split()]
a.sort(reverse=True)
ans=0
for i in range(n-2):
    if a[i]<a[i+1]+a[i+2]:
        ans=[a[i],a[i+1],a[i+2]]
        break
if ans==0:print(-1)
else:print(' '.join(str(i) for i in sorted(ans)))

 