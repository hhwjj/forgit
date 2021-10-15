from itertools import combinations

N=int(input())

XY=[]
for i in range(1,N+1):
    for k in range(1,N+1):
        XY.append((i,k))
print(XY)

dic={XY.index(_) : _ for _ in XY}

for i in combinations(dic,N):
    print(i)