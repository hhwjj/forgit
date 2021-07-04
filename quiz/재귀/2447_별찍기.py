def star(n):
    if n==3:
        l=[["*"]*3 for i in range(3)]
        l[1][1]=" "
    b=[[" "]*(n//3) for i in range(n//3)]

    c=[[" "]*n for i in range(n)]
    for x in range(n):
        for y in range(n):
            c[x][y]=star(n//3)[(x//3)%3][(y//3)%3]

    
def out(l):
    k=""
    for a in range(l):
        for b in range(l):
            k+=l[a][b]
        k+="\n"
    print(k)
#print(star(27)[1][1])
out(star(3))