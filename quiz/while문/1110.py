a=input().zfill(2)
c=a
i=0
b=-1
while a!=b:
    b=int(c[0])+int(c[1])
    b=str(b).zfill(2)
    c=c[1]+b[1]
    b=c
    i+=1
print(i)