n=int(input())
a=[int(i) for i in input().split()]
a.sort(reverse=True)
ans=0
for i in range(n):ans+=2**i*a[i]
print(ans)