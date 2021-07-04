import sys
input=sys.stdin.readline
*s,=range(10001)
for i in s[2:]:
    s[2*i::i]=[0]*(10000//i-1)
s=set(s)

n=int(input())

for i in range(n):
    A=int(input())
    k=int(A/2)
    while 1:
        if k in s:
            #print("1차통과")
            if A-k in s:
                #print("2차통과")
                break
            else:
                #print("{}에 1추가".format(k))
                k+=1
        else:
            #print("{}에 1추가".format(k))
            k+=1
    print(A-k,k)