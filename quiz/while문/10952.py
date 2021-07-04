import sys
input = sys.stdin.readline
d=1
c=[]
while True :
    b=list(input().split())
    d=int(b[0])+int(b[1])
    if d ==0:
        break
    c+=b
re = int(len(c)/2)

for k in range(re) :
    print(int(c[2*k])+int(c[2*k+1]))
#다른사람 답
#    while(1):
#    a,b=map(int,input().split())
#    if a==0 and b==0:
#        break
#    print(a+b)