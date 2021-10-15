import sys

N = int(input())


li = [input()+" {}".format(_) for _ in range(N)]

print(li)

li.sort(key=lambda x: (int(x.split()[0]),int(x.split()[2])))

print(li)
for _ in li:
    _=_.split()
    print(_[0],_[1])