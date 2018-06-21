import queue
q=int(input())
for _ in range(q):
    n,m,c_lib,c_road=[int(i) for i in input().split()]
    g={}
    v={}
    """we do not allocate space for all cities just for those which have a road to or from them"""
    for _ in range(m):
        i=[int(j) for j in input().split()]
        if i[0] in g:g[i[0]].append(i[1])
        else:g[i[0]]=[i[1],]
        if i[1] in g:g[i[1]].append(i[0])
        else:g[i[1]]=[i[0],]
        v[i[0]]=0
        v[i[1]]=0
    tmp=0
    l = queue.Queue(maxsize=100000)
    ans=0
    """if cost of building library c_lib is less than or equall to cost of building roads
       we do not build any roads and just build libraries in each city"""
    """else we iterate through all the cities which have a road beggining from them 
        if it has been visited we do not enter it 
        otherwise we put its location in queue and start our search from here
        it help us weed out cities which are part of city cluster that have been previously visited
        so we do not start a search from city cluster that have been previously visited
        the number of time we start the search is equall to no nof city clusters
        """
    if c_lib<=c_road:ans=c_lib*n
    else:
        tmp=n-len(v)
        for j in g:
            le=0
            if v[j]==0:
                l.put(j)
                v[j]=1
                le=1
                """in the while loop we iterate through the last popped city
                whenever we put a city on queue we mark it visited on increase the count of city in cluster
                we also check if city is visted or not before putting it in the queue
                WE DO NOT check visited after popping a city we push a city only when it is not visited
                so no need to check after popping as only unvisited cities gets pushed
                this increases efficienmcy 
                """
                while(not l.empty()):
                    start=l.get()
                    for i in g[start]:
                        if v[i]==0:
                            v[i]=1
                            le+=1
                            l.put(i)
                ans+=min((le-1)*c_road+c_lib,c_lib*le)
    print(ans+tmp*c_lib)
        
