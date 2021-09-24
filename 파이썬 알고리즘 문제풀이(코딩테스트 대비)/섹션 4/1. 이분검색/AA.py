#이진탐색!!
#
num, findnum= map(int,input().split())
a=list(map(int,input().split()))

a.sort()
mid = num // 2
last = len(a)
first = 0
while first<=last:
    mid=(first+last)//2
    if findnum>a[mid]:
        first=mid+1
    if findnum<a[mid]:
        last=mid-1
    if findnum==a[mid]:
        print(mid+1)
        break

