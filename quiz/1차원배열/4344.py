#첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
#둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

import sys
input=sys.stdin.readline
NOC=int(input()) #Number Of Case
case=list(map(int,input().split()))
print(case)
def sumfunc(k) :
    sum=0
    for i in k:
        sum += i
    sum = sum-k[0]
average = sumfunc(case)/case[0]
print(round(average,3))