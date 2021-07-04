t=int(input())
for i in range(t):
    h,w,n=map(int,input().split())
    #리스트생성
    a=[]
    #1~층수 까지 루프 // 층별로 방 리스트 생성
    for j in range(1,h+1):
        #리스트생성
        b=[]
        #1~방수 까지루프
        for k in range(1,w+1):
            #층수곱하기 100 + 방
            b.append(100*j+k*1)
        a.append(b)
        #=> a[층][방]
    cnt=0
    for c in range(w):
        for d in range(h):
            f=a[d][c]
            cnt+=1
            if cnt==n:
                print(f)   