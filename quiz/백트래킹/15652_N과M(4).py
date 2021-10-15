from itertools import combinations_with_replacement
[N,M]=list(map(int,input().split()))

li = [_ for _ in range(1,N+1)]


for i in combinations_with_replacement(li,M):
    k=list(map(str,i))
    print(" ".join(k))
