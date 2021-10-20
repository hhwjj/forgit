[K,P,N] = list(map(int,input().split()))

P=(P**10)%1000000007

r1=P
r2=1
R=0
A1=N

def md(l,m):
    i=1
    r=l
    while i<m:
        r=r*l%1000000007
        i+=1
    return r


if A1>10000:
    while A1>10000:
        A2=A1%10000
        A1=A1//10000
        if A2!=0:
            r2=r2*md(r1,A2)%1000000007
        r1=md(r1,10000)
    r1=md(r1,A1)
    R=r1*r2%1000000007
    print(R*K%1000000007)

else:
    print(K*(P**N)%1000000007)