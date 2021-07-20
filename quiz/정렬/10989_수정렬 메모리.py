import sys
input=sys.stdin.readline

f=list(range(0,10001))
s=""
n=int(input())
for i in range(n):
    b=input()
    s=s+b+" "
for k in f:
    a=str(k)