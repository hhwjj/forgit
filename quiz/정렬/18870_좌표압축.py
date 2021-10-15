import sys

N = int(input())

li=list(map(int,input().split()))
li2=list(set(li))
li2.sort()


dic={li2[i]:i for i in range(len(li2))}


for i in li:
    print(dic[i],end=' ')