ll=0
n,m=[int(i) for i in input().split()] 
s={}
for i in range(1,n+1):
    s[i]=[]
for i in range(m):
    a,b=[int(i) for i in input().split()] 
    s[b].append(a)
def eventree(temp,l):
    if len(s[temp])==0:
        return (1,l)
    else:
        su=0
        for i in s[temp]:
            t1=eventree(i,l)
            su+=t1[0]
            l=t1[1]
        su+=1
        if su%2==0:
            return (0,l+1)
        else:
            return (su,l)
c=eventree(1,0)
print(c[1]-1)

            
    