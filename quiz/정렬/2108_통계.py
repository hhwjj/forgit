import math
num=int(input())
s_num=list()
for i in range(num):
    j=int(input())
    s_num.append(j)
s_num.sort()
len_num=len(s_num)
avg=sum(s_num)/len_num
if avg<0:
    avg=math.ceil((avg)*(-1))*(-1)
    print("확인",avg)
else:avg=math.ceil(avg)

cen=int(num/2) #파이썬 0부터 시작 반영

range_num=s_num[len_num-1]-s_num[0]
init=0
init_num=0


print("합:",avg) #첫번째 문제
print("중앙값:",s_num[cen]) #두번째 문제
print("최빈값:",init_num)
print("범위:",range_num)