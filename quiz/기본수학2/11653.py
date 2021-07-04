N=int(input())
#n=N
def divide(k:int):
    global r
    r=k
    for i in range(2,k+1):
        if r==1:
            #print("종료")
            break
        elif r%i==0:
            r=int(k/i)
            print(i)
            #print("{}로 나눈 값:".format(i),r)
            divide(r)
    return r
divide(N)
#print("끝")