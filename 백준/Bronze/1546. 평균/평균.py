n=int(input())
a=list(map(int,input().split()))
newscore=[]
maxscore=max(a)
for i in a:
    newscore.append(i*100/maxscore)
print(sum(newscore)/len(newscore))