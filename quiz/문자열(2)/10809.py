#w1.find(인덱스)

w1=str(input())
r1=""
for i in range(97,123):
    k=w1.find(chr(i))
    r1+="{} ".format(k)
print(r1)