import math
A,B,V=map(int,input().split())
net=A-B
take=V-A
nettake=math.ceil(take/net)
final=int(nettake)+1
print(final)