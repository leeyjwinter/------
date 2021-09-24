# 조건문 if(분기,중첩)

'''x=7
if x!=7:
    print("Lucky")
    print("ㅋㅋ")
'''
x=input()
x=int(x)
if x>0:
    if x<10:
        print("10보다 작은 자연수")

if x>0 and x<10:
    print("10보다 작은 자연수")

if 0<x<10:
    print("10보다 작은 자연수")

a=93
if a>=90:
    print('A')
if a>=80:
    print('B')
if a>=70:
    print("C")
