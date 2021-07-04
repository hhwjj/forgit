#while True:
N=int(input())
a=[]
net=0
cnt5=0
for k in range(N//5+1): #k:5킬로 봉지수
    gcnt=0
    cnt3=0
    net=N-5*k
    if net%3 ==0:
        cnt3=net//3
        a.append(k+cnt3)
    else:
        a.append(1700)
if min(a) == 1700:
    print(-1)
else:
    print(min(a))