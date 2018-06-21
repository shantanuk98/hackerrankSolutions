q=int(input())
for _ in range(q):
    n,m=[int(i) for i in input().split()]
    g={}
    v={}
    for i in range(1,n+1):
        g[i]=[]
        v[i]=0
    d=[0]*(n+1)
    for _ in range(m):
        a,b=[int(i) for i in input().split()]
        g[a].append(b)
        g[b].append(a)
    start=int(input())
    queue=[]
    queue.append(start)
    v[start]=1
    while(len(queue)):
        temp=queue.pop(0)
        for i in g[temp]:
            if v[i]==0:
                v[i]=1
                queue.append(i)
                d[i]=d[temp]+6
    for i in range(1,n+1):
        if i==start:continue
        if d[i]==0:print("-1",end=" ")
        else:print(d[i],end=" ")
    print(" ")
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        