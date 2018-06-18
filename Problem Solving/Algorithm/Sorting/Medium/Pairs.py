n,k=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
a.sort()
ctr=0
i=0
j=1
while(j<n):
    diff= a[j]-a[i]
    if diff==k:
        ctr+=1
        j+=1
    elif diff<k:j+=1
    else:i+=1
print(ctr)