for _ in range(int(input())):
    n,k=[int(i) for i in input().split()]
    a=[int(i) for i in input().split()]
    b=[int(i) for i in input().split()]
    a.sort()
    ans="YES"
    b.sort(reverse=True)
    for i in range(n):
        a[i]+=b[i]
        if a[i]<k:ans="NO"
    print(ans)