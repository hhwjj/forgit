def sum(n):
    i=int(n*0.5)
    while 1:
        r1=i
        for k in str(r1):
            r1=r1+int(k)
        
        if r1==n:
            print(i)
            break
        if i>n:
            print(0)
            break
        i=i+1

a=int(input())
sum(a)

n=int(input())
print([*[i for i in range(n)if n==i+sum(map(int,str(i)))],0][0])