while 1:
    s=list(map(int,input().split()))
    if s == [0,0,0]:
        break
    l=max(s)
    s.remove(l)
    sum=0
    for i in s:
        sum+=i**2
    if sum==l**2:
        print("right")
    else:
        print("wrong")