import math
prime=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]
t=int(input())
for _ in range(t):
    n=int(input())
    product=1
    counter=0
    for i in prime:
        product*=i
        if product>n:break
        counter+=1
    print(counter)
