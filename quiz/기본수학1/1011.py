N=int(input())
for i in range(N):
    x,y=map(int,input().split())
    d=y-x
    a=1
    b=1
    cnt=0
    sa=0
    sb=0
    if d<=3:
        print(d)
    else:
        while (sa+sb)<d:
            sa=a*(a+1)/2
            sb=b*(b+1)/2
            if a==b:
                a+=1
                cnt+=1
            else :
                b+=1
                cnt+=1
            #print("a:",a,"b:",b,"작동횟수:",cnt+1)
        print(cnt+1)
    