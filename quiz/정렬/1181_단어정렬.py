import sys

N = int(input())

li = [sys.stdin.readline() for _ in range(N)]
li=set(li)
li=list(li)
li.sort(key=lambda x: (len(x),x))



print(''.join(li))