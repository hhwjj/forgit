list_a=list(input().split())
N=int(list_a[0])
X=int(list_a[1])
list_b=list(input().split())
c=""
for i in range(N):
    b=int(list_b[i])
    if b<X :
        c+=str(b)+" "
print(c)