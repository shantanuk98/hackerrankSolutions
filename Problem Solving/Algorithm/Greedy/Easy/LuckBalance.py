n,k=[int(i) for i in input().split()]
a=[]
c=0
for i in range(n):
    l,t=[int(i) for i in input().split()]
    if t==0:c+=l
    else:a.append(l)
a.sort(reverse=True)
if k>=len(a):c+=sum(a)
else:c=c+sum(a[0:k])-sum(a[k:])
print(c)
