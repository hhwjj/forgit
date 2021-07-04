#A: 고정비용
#B: 가변비용
#C: 판매가

A,B,C=map(int,input().split())
net=C-B
if net>0:
    print(A//net+1)
else:
    print(-1)