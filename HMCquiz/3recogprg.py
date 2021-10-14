N=int(input())
#set N
a=[]
for i in range(N):
    b=list(input())
    b=list(map(int,b))
    a.append(b)
#입력 정리

# for i in range(N):
#        print(a[i])

com=[]
#결과용 리스트
def find(k,i,j):
    k[i][j]=9
    global tmp
    tmp.append(1)
    if i < len(k)-1:
        if k[i+1][j] == 1:
            find(k,i+1,j)
    if j < len(k)-1:
        if k[i][j+1] ==1:
            find(k,i,j+1)
    if j >0:
        if k[i][j-1] ==1:
            find(k,i,j-1)
    if i>0:
        if k[i-1][j] ==1:
            find(k,i-1,j)
#판단용 재귀함수

# print("루프시작")
for x in range(N):
    for y in range(N) :
        tmp=[]
        if a[x][y] ==1:
            find(a,x,y)
            com.append(sum(tmp))
#입력 처리
for i in range(N):
       print(a[i])


com.sort()
print(type(com))
print(len(com))
for i in com:
    print(i)
            # 숫자환산고민해보기