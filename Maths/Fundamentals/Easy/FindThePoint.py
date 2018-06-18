n=int(input())
for _ in range(n):
    x1,y1,x2,y2=[int(i) for i in input().split()]
    x3=2*x2-x1
    y3=2*y2-y1 
    print(x3,y3)