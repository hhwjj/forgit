num=int(input())
s_num=list()
for i in range(num):
    j=int(input())
    s_num.append(j)
s_num.sort()
cen=int(num/2) #파이썬 0부터 시작 반영
print("합",int(sum(s_num))) #첫번째 문제
print("중앙값",s_num[cen]) #두번째 문제
s_pre=[0]*8000
s_cnt={}
for k in s_num:
    s_pre[k]=s_pre[k]+1
print("최빈값",s_pre.index(max(s_pre))