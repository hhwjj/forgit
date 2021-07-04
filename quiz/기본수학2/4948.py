import sys
input=sys.stdin.readline
*s,=range(246913)
#print(s[246912])
for i in s[2:]:
    s[2*i::i]=[0]*(246912//i-1)
    
while True:
    A=int(input())
    if A==0:
        break
    else:
        cnt=0
        for k in s[A+1:2*A+1]:
            if k!=0:
                cnt+=1
        print(cnt)