from collections import deque

num, deleter = input().split()
deleter = int(deleter)
a=list(map(int,num))

#print(a)
#cnt=0
# for i in range(len(a)):
#     for j in range(i+1):
#         if a[j]<a[i]:
#             a.pop(j)
#             deleter-=1

i=0

while i<len(a):
    j = i-1
    while j>=0 and deleter>0:
        #print(a[j],a[i])
        if a[j]<a[i]:
            #print(j,i)
            a.pop(j)
            deleter-=1
            i-=1
            j-=1
            #print(a)
        else:
            j-=1
    i+=1


#print(a)
#print(deleter)
if deleter==0:
    for x in a:
        print(x,end='')
else:
    for x in a[:-deleter]:
        print(x,end='')
