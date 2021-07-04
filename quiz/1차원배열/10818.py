import sys
input=sys.stdin.readline
a=input()
b=list(map(int,input().split()))
print("{} {}".format(min(b),max(b)))