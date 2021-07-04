f=[]
for i in range(100):
    k=str(i)+"666"
    l="666"+str(i)

    if k!=l:
        f.append(int(l))
        f.append(int(k))
    else:
        f.append(int(k))
f.sort()



n=int(input())
print(f[n-1])