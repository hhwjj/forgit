N=int(input())
A=list(map(int,input().split()))
#print(A)
a=[]
for i in A:
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
        while d<i:
            if i%d==0:
                cnt+=1
            d+=1

        #print("cnt:",cnt)
        if cnt == 0:
            a.append(i)
#print(a)
print(len(a))