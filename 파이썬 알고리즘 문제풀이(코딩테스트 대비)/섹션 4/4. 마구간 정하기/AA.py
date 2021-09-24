k, n = map(int, input().split())
a = []
for i in range(k):
    a.append(int(input()))

a.sort()
first = 1
last = (max(a) - min(a)) // (n - 1)


def checker(x):
    ncnt = 1
    a2 = 0
    a1 = 0
    while a2 < len(a) and ncnt < n:
        if a[a2] - a[a1] >= x:
            ncnt += 1
            a1 = a2
            a2 += 1
        else:
            a2 += 1
    #print(ncnt)
    if ncnt == n:
        return True
    else:
        return False


#print(checker(1))
#print(checker(2))
#print(checker(3))
#print(checker(8))

while first <= last:
    mid = (first + last) // 2
    if checker(mid):
        ans = mid
        first = mid + 1
    else:
        last = mid - 1

print(ans)