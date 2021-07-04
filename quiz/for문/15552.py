import sys
q=int(input())
D=[]
for i in range(q) :
    C = list(sys.stdin.readline().split())
    D += C
re = len(D)//2
for k in range(re) :
    a=2*k
    b=2*k+1
    print(int(D[a])+int(D[b]))