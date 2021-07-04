C=input()
A=int(C.split()[0])
B=int(C.split()[1])

if (B - 45)<0 :
    if A == 0 :
        A = 23
        B += 15
        print(A,B)
    else:
        A -=1
        B +=15
        print(A,B)

else:
    B -=45
    print(A,B)