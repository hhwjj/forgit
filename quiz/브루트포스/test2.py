k1=set(range(0,10))
k2=set(range(0,100))
s=set(range(0,1000))
s1=set()
s2=set()
for i in k2:s.add(str(i).zfill(3))
for i in k1:s.add(str(i).zfill(2))
for i in k2:s2.add(str(i).zfill(2))
s=set(map(str,s))
s2=set(map(str,s2))


f=set()
for i in s:
    f.add(int(i+"666"))
    for j in range(0,3):
        f.add(int(str(j)+"666"+i))
for k in s:
    for j in k2:f.add(int(str(j)+"666"+k))

f=list(f)
f.sort()
print(len(f))
while 1:
    n=int(input())
    print(f[n-1])