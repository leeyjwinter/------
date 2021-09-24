k, n = map(int, input().split())
a = list(map(int, input().split()))

first = 1
last = sum(a)


def checker(x):
    i = 0
    trial = 0
    while trial < n:
        sums = 0
        while i < len(a) and sums + a[i] <= x:
            sums += a[i]
            # print(f'sum untill {a[i]} is {sums} i = {i}')
            i += 1
        # print(f'trial is {trial}')
        trial += 1
    if i == len(a):
        return True
    else:
        return False


# print(checker(23))
# print(checker(17))
# print(checker(16))
# print(checker(2))
# print(checker(2))
res = 0
while first <= last:
    mid = (first + last) // 2
    if checker(mid):
        res = mid
        last = mid - 1
    else:
        first = mid + 1

print(res)
