import math
n=int(input())
for i in range(n):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    #son=(r2**2-r1**2+x1**2+y1**2-x2**2-y2**2)/2
    d2=(x2-x1)**2+(y2-y1)**2
    d1=math.sqrt(d2)

    if d1 !=0 and d1>(r1+r2):
        print(0)
    elif d1 == 0 and abs(r1-r2)!=0:
        print(0)
    elif d1 != 0 and d1==(r1+r2):
        print(1)
    elif d1 != 0 and d1==abs(r1-r2):
        print(1)
    elif d1==0 and (r1-r2)==0:
        print(-1)
    else:
        print(2)