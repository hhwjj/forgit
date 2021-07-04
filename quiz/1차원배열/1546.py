import sys
input=sys.stdin.readline
n=int(input())
b=list(map(int,input().split()))
c=0
for i in range(n):
    c+=b[i]/max(b)*100
print(round(c/n,6))