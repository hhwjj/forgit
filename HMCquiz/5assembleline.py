from sys import stdin


N = int(stdin.readline())

if N>1:
    a=[]
    b=[]
    am=[]
    bm=[]


    for i in range(N-1):
        tmp=list(map(int,stdin.readline().split()))
        a.append(tmp[0])
        b.append(tmp[1])
        am.append(tmp[2])
        bm.append(tmp[3])


    tmp=list(map(int,input().split()))

    a.append(tmp[0])
    b.append(tmp[1])

    na=len(a)
    sa=[a[0]]*na
    sb=[b[0]]*na

    print(sa)
    print(sb)
    for i in range(1,na):
        sa[i]=min(sa[i-1],sb[i-1]+bm[i-1])+a[i]
        sb[i]=min(sb[i-1],sa[i-1]+am[i-1])+b[i]
    
    print(sa)
    print(sb)
    
    print(min(sa[na-1],sb[na-1]))

else:
    [a,b]=list(map(int,input().split()))    
    print(min(a,b))