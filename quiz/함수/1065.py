import sys
input=sys.stdin.readline().rstrip

def arith(n:str):
    scnt=0
    b=set()
    c=len(n)-1
    for k in range(c) :
        c=int(n[k+1])-int(n[k])
        b.add(c)
    if len(b) ==1:
        scnt+=1
    return scnt


on=int(input())
cnt=0
for i in range(on):
    #print(i,"번째를 돌립니다.",len(str(i+1)))
    d=len(str(i+1))
    if d <= 2:
        cnt+=1
        #print("1,2 자리 {}수의 cnt:".format(i),cnt)

    else:
        cnt += arith(str(i+1))
        #print("3자리 이상 {}수의 cnt:".format(i),cnt)
print(cnt)