import sys

N = int(input())

li = [sys.stdin.readline() for _ in range(N)]

li.sort(key=lambda x: ((tuple(map(int, x.split())))[1],(tuple(map(int, x.split())))[0]))

print(''.join(li))