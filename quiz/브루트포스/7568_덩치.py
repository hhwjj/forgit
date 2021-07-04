cnt=int(input())
fl=[]
rank=[1]*cnt

for i in range(cnt):
    [a,b]=map(int,input().split())
    fl.append([a,b])


for i in range(cnt):
   for k in range(cnt):
       if fl[i][0] < fl[k][0]:
          if fl[i][1] < fl[k][1]:
            rank[i]+=1
print(" ".join(map(str,rank)))

