[K,P,N] = list(map(int,input().split()))

P=(P**10)%1000000007
r=P
print(P)
for i in range(N-1):
    r=r*P%(1000000007)
print('찐r:',r)
print(r*K%1000000007)