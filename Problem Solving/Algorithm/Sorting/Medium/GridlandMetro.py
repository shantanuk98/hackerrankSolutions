n,m,k=[int(i) for i in input().split()]
a=[]
for i in range(k):
    s=[int(i) for i in input().split()]
    for i in range(len(a)):
        if s[0]==a[i][0]:
            a[i].append(s[1:3])
            break
    else:
        a.append([s[0],])
        a[-1].append(s[1:3])
tot=0
for i in range(len(a)):
        b=a[i][1:len(a[i])]
        b.sort()
        c=[[0,0]]
        #print(b)
        for j in range(len(b)-1):
            if b[j+1][0]<=b[j][1]:
                b[j+1][0]=min(b[j][0],b[j+1][0])
                b[j+1][1]=max(b[j][1],b[j+1][1])
                b[j][0]=b[j][1]=0
        for j in range(len(b)):
            if b[j][1]==0:pass
            else:
                tot+=b[j][1]-b[j][0]+1
        #print(b)
print(n*m-tot)