import heapq
n,m=[int(i) for i in input().split()]
g={}
v={}
for i in range(1,n+1):
    g[i]=[]
    v[i]=0
s=0
for _ in range(m):
    a,b,c=[int(i) for i in input().split()]
    g[a].append((c,b))
    g[b].append((c,a))
    v[a]=0
    v[b]=0
q=[]
heapq.heapify(q)
heapq.heappush(q,(0,1))
ctr=0
ans=0
temp=0
while(ctr<n and len(q)>0):
    temp=heapq.heappop(q)
    if v[temp[1]]==0:
        v[temp[1]]=1
        ans+=temp[0]
        ctr+=1
        for i in g[temp[1]]:
            if v[i[1]]==0:heapq.heappush(q,i)
print(ans)
    
    
    