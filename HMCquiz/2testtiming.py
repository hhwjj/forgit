[N,M]=list(map(int,input().split()))
#set N,M
a=[]
for i in range(N):
    b=list(map(int,input().split()))
    a.append(b)

a[0]=[9]*M

a[N-1]=[9]*M

for k in range(N):
    a[k][0]=9
    a[k][M-1]=9

# for i in range(N):
#        print(a[i])

def make9(t):
    for i in range(1,N-1):
        for k in range(1,M-1):
            if t[i][k]==0:
                j=t[i+1][k]+t[i][k+1]+t[i-1][k]+t[i][k-1]
                if j>=9:
                    t[i][k]=9
    for i in range(1,N-1):
        for k in range(M-1,1,-1):
            if t[i][k]==0:
                j=t[i+1][k]+t[i][k+1]+t[i-1][k]+t[i][k-1]
                if j>=9:
                    t[i][k]=9
    for i in range(N-1,1,-1):
        for k in range(M-1,1,-1):
            if t[i][k]==0:
                j=t[i+1][k]+t[i][k+1]+t[i-1][k]+t[i][k-1]
                if j>=9:
                    t[i][k]=9
    for i in range(N-1,1,-1):
        for k in range(1,M-1):
            if t[i][k]==0:
                j=t[i+1][k]+t[i][k+1]+t[i-1][k]+t[i][k-1]
                if j>=9:
                    t[i][k]=9

    return t

def makec(t):
    for i in range(1,N-1):
        for k in range(1,M-1):
            if t[i][k]==1:
                j=t[i+1][k]+t[i][k+1]+t[i-1][k]+t[i][k-1]
                if j>=18:
                    t[i][k]=0
    for i in range(N-1,1,-1):
        for k in range(M-1,1,-1):
            if t[i][k]==0:
                j=t[i+1][k]+t[i][k+1]+t[i-1][k]+t[i][k-1]
                if j>=18:
                    t[i][k]=0
    return t

cnt=0
for i in range(N):
    print(a[i])

print("루프시작")

while 1 :
    for i in range(10):
        a=make9(a)
    

    print("9씌우기, 반복 : {}".format(cnt))
    for i in range(N):
        print(a[i])
    re=0
    for i in range(len(a)):
        re+=sum(a[i])
    print(re)
    if re == 9*M*N:
        break
    cnt+=1
    a=makec(a)
    print("녹은것들은 0, 흐른시간: {}".format(cnt))
    for i in range(N):
        print(a[i])


print(cnt)