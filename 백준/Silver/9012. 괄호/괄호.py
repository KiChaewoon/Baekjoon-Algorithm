n=int(input())
def queue(a):
    que=[]
    for cmd in a:
        if cmd=="(":
            que.append(1)
        elif cmd==")":
            if len(que)==0: return False
            else: que.pop()
    if len(que)==0: return True
    else:return False


for i in range(n):
    a=input()
    if queue(a): print("YES")
    else: print("NO")
