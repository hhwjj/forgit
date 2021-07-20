s1=list(range(0,10000))
s2=set()
for k in s1:s2.add(str(k).zfill(4))

temp=set()


for i in s2:
    j=0
    while j<=len(i):
        str1=i[:j]+"666"+i[j:]
        temp.add(int(str1))
        j+=1
temp=list(temp)
temp.sort()

while 1:
    n=int(input())
    print(temp[n-1])