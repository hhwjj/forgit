T=int(input())
for y in range(T):
    k=int(input()) #층
    n=int(input()) #호
    a=[]
    b=[]
    for i in range(n+1):
        b.append(i+1)
    a.append(b)
    for i in range(1,k+1):
        b=[1]
        a.append(b)
        c=0
        for x in range(1,n+1):
            c=a[i-1][x]+a[i][x-1]
            b.append(c)
    print(a[k][n-1])