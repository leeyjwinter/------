a = [1]
num = int(input())


def two(x):
    if x == 1:
        return a
    two(x // 2)
    # print(x % 2)
    # print(x)
    a.append(x % 2)


two(num)
# print(a)

for x in a:
    print(x, end="")
