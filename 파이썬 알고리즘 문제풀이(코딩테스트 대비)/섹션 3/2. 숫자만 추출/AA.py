#x.isdecimal() : x가 0~9까지면 true 반환

string_a = input()
number = []

for i in range(len(string_a)):
    if string_a[i]<'A' and string_a[i]>='0':
        number.append(string_a[i])

while number[0]=='0':
    number.pop(0)
number=int(''.join(number))


def yaksu(x):
    cnt = 0
    if type(x**(1/2))=='int':
        for j in range(1,x**(1/2)+1):
            if x%j==0:
                cnt+=1
        cnt=cnt*2+1
    else:
        for j in range(1,round(x**(1/2))+1):
            if x%j==0:
                cnt+=1
        cnt=cnt*2
    return cnt


print(number)
print(yaksu(number))



