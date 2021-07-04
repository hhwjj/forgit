s1=[]
s2=[]
for i in range(3):
    x,y=map(int,input().split())
    s1.append(x)
    s2.append(y)
for i in s1:
    if s1.count(i)==1:
        for k in s2:
            if s2.count(k)==1:
                print(i,k)