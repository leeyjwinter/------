for i in range(1,6):
    print("i:",i,end=' ',sep='')
    for j in range(1,6):
        print("j:",j,end=' ',sep='')
    print()

for i in range(5):
    for t in range(5-i):
        print(" ",end=' ')
    for j in range(i):
        print("*",end=' ')
    print()