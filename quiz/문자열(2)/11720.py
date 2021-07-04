import sys
input=sys.stdin.readline

#투입숫자갯수
a=int(input())

#투입숫자일렬항
b=str(input())

#합계산
c=0
for i in range(a):
    c+=int(b[i])
print(c)