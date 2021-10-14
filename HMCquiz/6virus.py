[K,P,N] = list(map(int,input().split()))

F=K*(P**N)
print(F%1000000007)