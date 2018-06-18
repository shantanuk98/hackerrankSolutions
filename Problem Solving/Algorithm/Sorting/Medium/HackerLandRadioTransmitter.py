n,k=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
a.sort()
i=nt=0
while(i<n):
    nt+=1
    loc=a[i]+k
    while(i<n and a[i]<=loc):i+=1
    loc=a[i-1]+k
    while(i<n and a[i]<=loc):i+=1
print(nt)