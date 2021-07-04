def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 1
    else:
        fn=fibo(n-1)+fibo(n-2)
    return fn

k=int(input())
print(fibo(k))