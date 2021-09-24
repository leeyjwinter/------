num = int(input())
score =map(int,input().split())
score=list(score)
newscore = score

ave = sum(score)/num
ave = round(ave)

minusabs = []
minscore = 100

for i in range(num):
    minusabs.append(abs(score[i]-ave))
    if abs(score[i]-ave)<abs(minscore-ave):
        minscore = score[i]
        minabs = abs(score[i]-ave)


indexes=[]
for index,value in enumerate(minusabs):
    if value==minabs:
        indexes.append(index)


if len(indexes)==1:
    print(f'{ave} {indexes[0]+1}')


else:
    maxscore=-1
    for x in indexes:
        if score[x]>=maxscore:
            maxscore=score[x]
    print(f'{ave} {score.index(maxscore)+1}')





