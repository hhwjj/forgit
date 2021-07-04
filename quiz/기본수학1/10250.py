case=int(input())
#H: 층, W: 방수, N: 손님차례
for i in range(case):
    H,W,N=map(int,input().split())
    if H!=1 :
        if N%H != 0:
            room=str((N//H)+1).rjust(2,"0")
            flr=str(N%H)
            final="{}{}".format(flr,room)
            print(int(final))
        else:
            room=str((N//H)).rjust(2,"0")
            flr=str(H)
            final="{}{}".format(flr,room)
            print(int(final))
    else:
        room=str(N).rjust(2,"0")
        flr=1
        final="{}{}".format(flr,room)
        print(int(final))