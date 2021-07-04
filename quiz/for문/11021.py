q=int(input())

D=[]
for i in range(q) :
    
    C = list(input().split())
    D += C
re = len(D)//2
for k in range(re) :
    a=2*k
    b=2*k+1
    print("Case #{}: {} + {} = {}".format(k+1,int(D[a]),int(D[b]),int(D[a])+int(D[b])))