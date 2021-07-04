M,N=list(map(int,input().split()))
*s,=range(N+1)
#print(s)
for i in s[2:]:
    s[2*i::i]=[0]*(N//i-1)
    #print(s)
for k in s[2:]:
    if M<=k and k!=0:
        print(k)