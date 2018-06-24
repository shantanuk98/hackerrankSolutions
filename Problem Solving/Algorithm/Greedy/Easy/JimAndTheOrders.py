a=[]
for i in range(int(input())):
    x,y=[int(i) for i in input().split()]
    a.append((x+y,i))    
a.sort()
for i in a:print(i[1]+1,end=" ")