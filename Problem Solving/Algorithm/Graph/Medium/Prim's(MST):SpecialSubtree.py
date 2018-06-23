import heapq
n,m=[int(i) for i in input().split()] 
s={}
v={}
d={}
for i in range(1,n+1):
    s[i]=[]
    v[i]=0
for i in range(m):
    a,b,w=[int(i) for i in input().split()] 
    s[a].append((w,b))
    s[b].append((w,a))
start=int(input())
q=[]
q.append((0,start))
heapq.heapify(q)
su=0
while(len(q)>0):
    temp=heapq.heappop(q)
    if v[temp[1]]==0:
        v[temp[1]]=1
        su+=temp[0]
        for i in s[temp[1]]:
            heapq.heappush(q,i)
print(su)
            
    