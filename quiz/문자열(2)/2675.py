from functools import singledispatch
import sys
input=sys.stdin.readline

N=int(input())

for i in range(N):
    S=input()
    Slist=list(S.split())
    #print(Slist)
    r=int(Slist[0])
    w1=str(Slist[1])
    re1=""
    for k in w1:
        re1 += k*r
    print(re1)