###a.sort(key=lambda x : (x[1],x[0]))

num = int(input())
a = []
for i in range(num):
    k, n = map(int, input().split())
    a.append((k, n))

a.sort(key=lambda x: (x[1], x[0]))

'''print(a)
minend = 2147483647
temp = 2147483647
temp2 = 0
cnt = 0


def firstchoose(x):
    for start, end in x:
        global minend
        global cnt
        global temp
        global temp2
        if end <= minend:
            minend = end
            temp = start
            temp2 = end

    # print(x)
    # print((temp,minend))
    x.remove((temp, minend))
    cnt += 1
    # print('cnt is %d'%cnt)
    temp, minend = 2147483647, 2147483647


while len(a) != 0:
    firstchoose(a)
    # print(a)
    # print('temp2 is %d'%temp2)
    for start, end in a:
        b = []
        # print(start,end)
        if start < temp2:
            b.append((start, end))
        a = [x for x in a if x not in b]
        # print(a)

print(cnt)'''

et=0
cnt=0
for s, e in a:
    if s>=et:
        et=e
        cnt+=1
print(cnt)
