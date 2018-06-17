l,s1,s2=[int(i) for i in input().split()]
roottwo=2**0.5
q=int(input())
for _ in range(q):
    a=int(input())
    print((abs(l-a**0.5)/abs(s1-s2))*roottwo)