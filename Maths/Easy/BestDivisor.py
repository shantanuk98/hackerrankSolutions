n=int(input())
f=[]
m=0
num=-1
for i in range(1,n+1):
    if n%i==0:
        s=str(i)
        su=0
        for j in s:su+=int(j)
        if su>m:
            m=su
            num=i
print(num)