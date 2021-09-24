def DFS(v):
    if v > 7:
        return

    print(v)
    DFS(v * 2)
    DFS(v * 2 + 1)


def DFS_mid(v):
    if v > 7:
        return

    DFS_mid(v*2)
    print(v)
    DFS_mid(v*2+1)

def DFS_last(v):
    if v > 7:
        return
    else:
        DFS_last(v*2)
        DFS_last(v*2+1)
        print(v)

#DFS(1)
#DFS_mid(1)
DFS_last(1)