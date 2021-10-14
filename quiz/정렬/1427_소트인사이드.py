a=input()
k=[]
for i in a:
    k.append(int(i))
k.sort(reverse=True)
f="".join(map(str,k))
print(f)