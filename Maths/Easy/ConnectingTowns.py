from operator import mul
t=int(input())
for _ in range(t):
    n=int(input())
    pro=1
    a=[int(i) for i in input().split()]
    for i in a:pro=(pro*i)%1234567
    print(pro)
