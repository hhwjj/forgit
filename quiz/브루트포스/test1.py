k=set()
for i in range(665,5000000) :
    if '666' in str(i) : k.add(i)
    if len(k)==10000:break
k=list(k)
k.sort()
print(k[9999])

n=int(input())
print(k[n-1])