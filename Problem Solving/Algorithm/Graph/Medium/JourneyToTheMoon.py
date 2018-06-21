import queue
n,p=[int(i) for i in input().split()]
g={}
v={}
for _ in range(p):
    i=[int(j) for j in input().split()]
    if i[0] in g:g[i[0]].append(i[1])
    else:g[i[0]]=[i[1],]
    if i[1] in g:g[i[1]].append(i[0])
    else:g[i[1]]=[i[0],]
    v[i[0]]=0
    v[i[1]]=0
l = queue.Queue(maxsize=100000)
cluster=[]
ans=1
for j in g:
    le=0
    if v[j]==0:
        l.put(j)
        v[j]=1
        le=1
        while(not l.empty()):
            start=l.get()
            for i in g[start]:
                if v[i]==0:
                    v[i]=1
                    le+=1
                    l.put(i)
        cluster.append(le)
s=sum(cluster)
for _ in range(n-s):
    cluster.append(1)
s=sum(cluster)
ans=0
for i in range(len(cluster)):
    ans+=(s-cluster[i])*cluster[i]
    s-=cluster[i]
print(ans)
