import sys
input=sys.stdin.readline
b=[]
cnt=0
for i in range(10):
    a=int(input())%42
    if b.count(a) == 0:
        cnt +=1
    b.append(a)
print(cnt)