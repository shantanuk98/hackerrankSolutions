for _ in range(int(input())):
    s={}
    v=[0]*101
    d=[-1]*(101)
    for i in range(101):
        s[i]=list(range(max(i+1,1),min(i+7,101)))
    n=int(input())
    for i in range(n):
        a,b=[int(i) for i in input().split()]
        for j in range(max(a-6,1),min(a,101)):
            s[j].append(b)
            s[j].remove(a)
    m=int(input())
    for i in range(m):
        a,b=[int(i) for i in input().split()]
        for j in range(max(a-6,1),min(a,101)):
            s[j].append(b)
            s[j].remove(a)
    d[1]=0
    v[1]=1
    q=[]
    q.append(1)
    while(len(q)>0):
        temp=q.pop(0)
        for i in s[temp]:
            if v[i]==0:
                v[i]=1
                d[i]=d[temp]+1
                q.append(i)
    print(d[100])
    
    