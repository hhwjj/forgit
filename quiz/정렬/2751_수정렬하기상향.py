import sys
input=sys.stdin.readline
n=int(input())
s=list()
for i in range(n):
    k=int(input())
    s.append(k)
s.sort()
for j in s:print(j)