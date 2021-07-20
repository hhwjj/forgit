import sys

s=[0]*10001
n=int(input())
for i in range(n):
    b=int(sys.stdin.readline())
    s[b]=s[b]+1
for k in range(0,10001):
    if s[k]>0:
        for l in range(s[k]):
            print(k)

import sys 
N = int(input()) 
check_list = [0] * 10001 
for i in range(N): 
    input_num = int(sys.stdin.readline()) 
    check_list[input_num] = check_list[input_num] + 1 
for i in range(10001): 
    if check_list[i] != 0: 
        for j in range(check_list[i]): print(i)

