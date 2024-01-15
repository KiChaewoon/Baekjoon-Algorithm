k=int(input())
numlist=[]
for i in range(k):
    a=int(input())
    if a==0: numlist.pop()
    else: numlist.append(a)
print(sum(numlist))