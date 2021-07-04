def mset(n:str) :
    s1=set()
    for i in n:
        s1.add(i)
    return(s1)

def comp(n:str) :
    ns=n[0]
    for i in range(1,len(n)):
        if n[i] != n[i-1] :
            ns+=n[i]
    return ns


n1=int(input())
finalr=0
for i in range(n1):
    w1=input()
    ws=mset(w1)
    wc=comp(w1)
    #소결과
    r=0
    for k in ws:
        if wc.find(k) != wc.rfind(k) :
            r+=1
    #print("{}의 판단 0이면 그룹단어, 1이면 아님:".format(w1),r)
    if r==0 :
        #그룹단어갯수 : finalr
        finalr+=1
print(finalr)