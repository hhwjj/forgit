iter=int(input())
n=0
Sn=0
while Sn<iter :
    n+=1
    Sn=n*(n+1)/2
#짝수일때
k=int(Sn)-iter
r1=""
if n%2==0 :
    r1="{}/{}".format((n-k),(k+1))
#홀수일때
else :
    r1="{}/{}".format((k+1),(n-k))
print(r1)