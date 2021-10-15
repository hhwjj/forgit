# N=int(input())
# case=[]

# for i in range(N):
#     [a,b]=list(map(int,input().split()))
#     case.append((a,b))

# case.sort()

# for i in case:
#     print("{} {}".format(i[0],i[1]))

import sys

N = int(input())

li = [sys.stdin.readline() for _ in range(N)]

li.sort(key=lambda x: ((tuple(map(int, x.split())))[1],(tuple(map(int, x.split())))[0]))

print(''.join(li))