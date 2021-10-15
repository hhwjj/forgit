from itertools import permutations

[N,M]=list(map(int,input().split()))

li = [_ for _ in range(1,N+1)]
print(li)

for i in permutations(li,M):
    k=list(map(str,i))
    print(" ".join(k))
