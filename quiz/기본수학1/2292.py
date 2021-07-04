Room=int(input())
n=0
Sn=0
while Sn<Room :
    n+=1
    Sn=3*n*(n-1)+1
    
print(n)