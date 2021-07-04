import sys
input=sys.stdin.readline
M=int(input())
N=int(input())
#print(A)
a=[]
for i in range(M,N+1):
    d=2
    cnt=0
    #print("{}가 소수?".format(i))
    if i == 1:
        pass
        #print("i=1or2")
    elif i == 2:
        a.append(i)
        #print("i=1or2")
    else:
        if i %2==0:
            pass
        else:
            while d<i/2:
                if i%d==0:
                    cnt+=1
                d+=1

        #print("cnt:",cnt)
            if cnt == 0:
                a.append(i)
    
suma=sum(a)
if a == [] :
    print(-1)
else:
    print(suma)
    print(min(a))