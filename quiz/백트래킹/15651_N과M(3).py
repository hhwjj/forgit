from itertools import product
[N,M]=list(map(int,input().split()))

li = [_ for _ in range(1,N+1)]


for i in product(li,repeat=M):
    k=list(map(str,i))
    print(" ".join(k))
