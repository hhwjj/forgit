*s,=range(101)
print(s)
for i in s[2:]:
    print(i)
    print(s[2*i::i])
    s[2*i::i]=[0]*(100//i-1)
print(s)

#print(s[60:100])
#P={*s[int(input()):int(input())+1]}-{0,1}
#print(P,type(P))
#print(f"{sum(P)}\n{min(P)}"if P else-1)