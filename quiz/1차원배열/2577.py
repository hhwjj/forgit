import sys
input=sys.stdin.readline
a=int(input())
b=int(input())
c=int(input())

d=str(a*b*c)
for i in range(10) :
    i=str(i)
    t=d.count(i)
    print(t)