m,n=map(int,input().split())
s=[]
for i in range(m):
    s.append(input())

j1="WBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBW"
j2="BWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWB"



fl=[]
for i in range(n-7):
    for k in range(m-7):
        t=""
        f2=0
        f3=0
        for l in range(8):
            t+=s[k+l][i:i+8]
        
        for z in range(len(j1)):
            if t[z] != j1[z] :f2+=1
        fl.append(f2)
        for x in range(len(j2)):
            if t[x] != j2[x] :f3+=1
        fl.append(f3)
print(min(fl))