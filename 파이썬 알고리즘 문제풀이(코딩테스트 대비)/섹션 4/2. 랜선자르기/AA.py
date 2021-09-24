k, n = map(int, input().split())
a = []
for x in range(k):
    a.append(int(input()))


def checker(y, div):
    ans = 0
    for value in y:
        ans += value // div
    return ans


first = 1
last = max(a)
answerable = []

while first <= last:
    mid = (first + last) // 2
    if checker(a, mid) >= n:
        res=mid
        first = mid + 1
    if checker(a, mid) < n:
        last = mid - 1

print(res)
