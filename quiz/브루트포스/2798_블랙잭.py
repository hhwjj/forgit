from itertools import combinations

N,M=map(int,input().split())
numbers=list(map(int,input().split()))


a=list(combinations(numbers,3))

r2=0
for i in a:
    r1=0
    for k in i : 
        r1=r1+k
    if r1<=M and r1>r2:
        r2=r1
print(r2)

#[N,M],c=eval('map(int,input().split()),'*2);from itertools import*;print(max(i for i in map(sum,combinations(c,3))if i<=M))