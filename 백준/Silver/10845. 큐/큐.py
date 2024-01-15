import sys
n= int(sys.stdin.readline())
que=[]
for i in range(n):
    cmd=sys.stdin.readline().split()
    inp=cmd[0]
    if inp=="pop":
        if len(que)==0: print(-1)
        else: 
            print(que.pop(0))
    elif inp=="size": print(len(que))
    elif inp=="empty":
        if len(que)==0: print(1)
        else: print(0)
    elif inp=="front":
        if len(que)==0: print(-1)
        else:print(que[0])
    elif inp=="back":
        if len(que)==0: print(-1)
        else: print(que[-1])
    else:
        b=cmd[1]
        que=que+[b]